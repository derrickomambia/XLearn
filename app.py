from flask import Flask, render_template, request, redirect, url_for, session, flash
import database
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a secure key in production

# Configure Gemini API using .env variable
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please set it.")
genai.configure(api_key=api_key)

# Function to generate lecture notes for a question
def generate_lecture_note(question_text, options, correct_answer):
    prompt = f"Question: {question_text}\n"
    if options and options.strip():
        prompt += f"Options: {options}\n"
    prompt += f"Correct Answer: {correct_answer}\n"
    prompt += f"""
Generate a detailed lecture note for a beginner in electromagnetism that explains the concept behind this question, with a strong focus on the correct answer and the most effective method to arrive at it. The lecture note should be structured as follows:

1. **Introduction**: Briefly introduce the concept related to the question and its relevance to electromagnetism.
2. **Definitions**: Define any key terms or jargon used in the question or explanation, ensuring clarity for beginners.
3. **Explanation**: Provide a clear and detailed explanation of the underlying principles, using simple language and avoiding advanced terminology. Anticipate and address potential questions or confusions a beginner might have.
4. **Examples**: Include at least two examples: one simple example to illustrate the basic idea and another more complex example to show its application in a real-world context.
5. **Most Effective Solution**: Present the most efficient and straightforward method to solve the question step by step, emphasizing why this approach is optimal. Clearly explain how it leads to the correct answer: '{correct_answer}'. Highlight any key shortcuts, logical reasoning, or practical tips that make this method effective.
6. **Correct Answer Confirmation**: Explicitly state the correct answer ('{correct_answer}') and explain why it is correct, reinforcing the solution with the underlying concept.
7. **Options Analysis** (if applicable): If options are provided, analyze each incorrect option, explaining why it’s wrong and linking mistakes to common errors or misunderstandings.
8. **Common Misconceptions**: Address any frequent misconceptions or pitfalls beginners might encounter with this concept or solution method.
9. **Further Reading**: Suggest additional resources or topics for the user to explore next.
10. **Challenge**: Pose a thought-provoking question or challenge related to the concept to encourage deeper thinking.

Throughout the lecture note, use a friendly and encouraging tone, addressing the reader directly with 'you' and 'your'. Include analogies or real-world examples to make the concept relatable. Where appropriate, describe any diagrams or visual aids that could help illustrate the concept or solution method. Include a brief historical note or interesting fact about the concept to make the content engaging. Ensure all information is accurate and based on established scientific principles. Aim for a lecture note that is approximately 500-700 words, with the correct answer and most effective solution method as the central focus.
"""
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Home route: Displays available units
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    units = database.get_units()
    return render_template('homepage.html', units=units)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = database.get_user(username, password)
        if user:
            session['user_id'] = user[0]  # Store user_id in session
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('login.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if database.add_user(username, password):
            return redirect(url_for('login'))
        flash('Username already exists')
    return render_template('register.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# View lecture notes for a selected unit
@app.route('/lecture_notes/<int:unit_id>')
def lecture_notes(unit_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    questions = database.get_questions(unit_id)
    if not questions:
        flash(f"No questions available for this unit (Unit ID: {unit_id}). Please add some questions.")
        return redirect(url_for('index'))
    
    lecture_notes = []
    for question in questions:
        question_id, unit_id, question_text, options, correct_answer = question
        try:
            note = generate_lecture_note(question_text, options, correct_answer)
            lecture_notes.append({
                'question_text': question_text,
                'lecture_note': note
            })
        except Exception as e:
            lecture_note = f"Error generating lecture note: {str(e)}"
            lecture_notes.append({
                'question_text': question_text,
                'lecture_note': lecture_note
            })
    
    return render_template('lecture_notes.html', unit_id=unit_id, lecture_notes=lecture_notes)

if __name__ == '__main__':
    # database.init_db()  # Initialize database (comment out after first run to keep your questions)
    app.run(debug=True)