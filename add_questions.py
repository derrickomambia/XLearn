from database import add_question

# Add questions to Electromagnetism (unit_id = 1)
unit_id = 1

# QUESTION ONE
add_question(unit_id, 'Explain the meaning of Electromagnetism.', '', 'Electromagnetism is the study of the interactions between electric and magnetic fields.')
add_question(unit_id, 'Explain the meaning of Electromagnetic force.', '', 'Electromagnetic force is the force between charged particles due to their electric and magnetic fields.')
add_question(unit_id, 'Explain the meaning of Electromagnetic induction.', '', 'Electromagnetic induction is the process of generating an electromotive force (EMF) in a conductor by changing the magnetic field around it.')
add_question(unit_id, 'State Faraday’s Law of electromagnetism.', '', 'Faraday’s Law states that the induced EMF in a closed loop is equal to the negative rate of change of magnetic flux through the loop.')
add_question(unit_id, 'Explain how electromagnetic waves are propagated.', '', 'Electromagnetic waves are propagated by the oscillation of electric and magnetic fields perpendicular to each other and to the direction of wave propagation.')
add_question(unit_id, 'A TV requires 15000V and 0.01 A to accelerate the electron beam. The outlet supplies 120V, and the primary coil has 100 turns. Determine the number of turns the secondary coil should have.', '', '1250')
add_question(unit_id, 'A TV requires 15000V and 0.01 A to accelerate the electron beam. The outlet supplies 120V. How much current does the TV draw from the outlet?', '', '1.25 A')
add_question(unit_id, 'A 2 m wire is in a 2×10^-6 T magnetic field pointing into the page and carries 2 A of current flowing up. Determine the force on the wire.', '', '8×10^-6 N')
add_question(unit_id, 'A simple electric motor needs to supply a maximum torque of 10 Nm using 0.1 A of current in a 0.02 T magnetic field. The coil is a circle with a radius of 2 cm. Determine the number of turns in the coil.', '', '796')

# QUESTION TWO
add_question(unit_id, 'Explain the term electromagnetic field.', '', 'An electromagnetic field is a physical field produced by electrically charged objects, consisting of electric and magnetic components.')
add_question(unit_id, 'Explain the nature of electric charges and magnetic poles.', '', 'Electric charges can be positive or negative and exert forces on each other. Magnetic poles come in pairs (north and south) and exert forces on each other.')
add_question(unit_id, 'A rectangular wire loop of sides 10 cm and 5 cm with a small cut is moving out of a 0.2 T magnetic field at 5 cm/s normal to the shorter side. Determine the emf developed across the cut.', '', '0.01 V')
add_question(unit_id, 'A rectangular wire loop of sides 10 cm and 5 cm with a small cut is moving out of a 0.2 T magnetic field at 5 cm/s normal to the longer side. Determine the emf developed across the cut.', '', '0.005 V')
add_question(unit_id, 'A long solenoid has 200 turns per cm and carries a current of 2.5 A. What is the magnetic field at its center?', '', '0.628 T')
add_question(unit_id, 'State three applications of electromagnetic waves.', '', 'Communication, medical imaging, and remote sensing.')

# QUESTION THREE
add_question(unit_id, 'State Coulomb’s law of electrostatics.', '', 'Coulomb’s law states that the force between two point charges is directly proportional to the product of their charges and inversely proportional to the square of the distance between them.')
add_question(unit_id, 'Determine the electrostatic force between two charges of 2 C and -1 C separated by 1 m in air.', '', '-1.8×10^10 N')
add_question(unit_id, 'State Faraday’s law of electromagnetic induction.', '', 'Faraday’s law states that the induced EMF in a closed loop is equal to the negative rate of change of magnetic flux through the loop.')
add_question(unit_id, 'The magnetic flux linked with a coil changes from 2 Wb to 0.2 Wb in 0.5 seconds. Calculate the induced EMF.', '', '3.6 V')
add_question(unit_id, 'A circular coil of radius 10 cm and 50 turns is rotated at 20 rad/s in a 0.05 T magnetic field. Obtain the maximum EMF induced in the coil.', '', '15.71 V')
add_question(unit_id, 'A circular coil of radius 10 cm and 50 turns is rotated at 20 rad/s in a 0.05 T magnetic field. Obtain the average EMF induced in the coil over a full rotation.', '', '0 V')
add_question(unit_id, 'A circular coil of radius 10 cm and 50 turns is rotated at 20 rad/s in a 0.05 T field with a resistance of 20 Ω. Calculate the maximum value of current in the coil.', '', '0.785 A')
add_question(unit_id, 'A circular coil of radius 10 cm and 50 turns is rotated at 20 rad/s in a 0.05 T field with a resistance of 20 Ω. Calculate the average power loss due to Joule heating.', '', '12.32 W')

# QUESTION FOUR
add_question(unit_id, 'State Gauss’s law for magnetism.', '', 'Gauss’s law for magnetism states that the net magnetic flux through any closed surface is zero.')
add_question(unit_id, 'State Gauss’s law in electrostatics.', '', 'Gauss’s law in electrostatics states that the net electric flux through any closed surface is equal to the enclosed charge divided by the permittivity of free space.')
add_question(unit_id, 'Write the differential form of Gauss’s theorem for the electric field.', '', '∇ • E = ρ / ε₀')
add_question(unit_id, 'Explain the meaning of a Gaussian surface.', '', 'A Gaussian surface is a closed surface used in Gauss’s law to calculate the flux of an electric or magnetic field.')
add_question(unit_id, 'Find the total flux enclosed by a surface with charges 4 C, 7 C, and 2 C.', '', '1.47×10^12 Nm²/C')
add_question(unit_id, 'A circular coil with 5 loops of diameter 1.0 m carries 4.0 A in a 0.5 T field, experiencing a torque of 3.93 N-m. Determine the magnetic moment of the coil.', '', '5 A m²')
add_question(unit_id, 'A circular coil with 5 loops of diameter 1.0 m carries 4.0 A in a 0.5 T field, experiencing a torque of 3.93 N-m. Determine the angle between the normal to the plane of the coil and the magnetic field.', '', '51.3°')

# QUESTION FIVE
add_question(unit_id, 'An inductor has a self-induced EMF of 0.016 V when the rate of change of current is 0.064 A/s. Determine the inductance of the inductor.', '', '0.25 H')
add_question(unit_id, 'A 400-turn solenoid has an inductance of 0.25 H. Determine the magnetic flux through each turn when the current is 0.720 A.', '', '4.5×10^-4 Wb')

print("Questions added to unit_id 1 (Electromagnetism).")