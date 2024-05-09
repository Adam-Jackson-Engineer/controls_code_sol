# %%

import sympy as sp
import Param as P
import AllTaskKineticEnergyData as KE
import AllTaskPotentialEnergyData as PE
from sympy import symbols, Function
from GenerateKineticEnergy import compute_kinetic_energy
from GeneratePotentialEnergy import compute_potential_energy
from GenerateEoM import compute_eom_lagrangian
from Param import display_formula

sp.init_printing(use_latex='mathjax')

# %%

#------------------------------------------------------------------------------
#--------------------Design Study A: Single Link Robot Arm---------------------
#------------------------------------------------------------------------------

# System Parameters
num_bodies = 1
mass = symbols('m')
length = symbols('l')
t = symbols('t')
theta = Function('theta')(t)
tau = symbols('tau')
b = symbols('b')
generalized_coordinates = [theta]
generalized_forces = [tau]
generalized_damping = [b*P.theta_dot]

# Kinetic Energy
parameters = KE.Task_A(length, mass, theta, t)
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)

print("\nTask A Kinetic Energy:")
display_formula(ke_symbolic)

# Potential Energy
num_PE = 1
parameters = PE.Task_A(length, mass, theta)
pe_symbolic, pe_evaluate = compute_potential_energy(num_PE, parameters)

print("\nTask A Potential Energy:")
display_formula(pe_symbolic)

# Lagrangian
L_symbolic = ke_symbolic - pe_symbolic
print("\nTask A Lagrangian")
display_formula(L_symbolic)

# Equations of motion
EoM_symbolic = compute_eom_lagrangian(L_symbolic, generalized_coordinates, generalized_forces, generalized_damping, t)
print("\nTask A Equations of Motion")
for eom in EoM_symbolic:
    display_formula(eom)

# %%

#------------------------------------------------------------------------------
#----------------------Design Study B: Pendulum on Cart------------------------
#------------------------------------------------------------------------------

# System Parameters
num_bodies = 2
mass1 = symbols('m_1')
mass2 = symbols('m_2')
length = symbols('l')
z = Function('z')(t)
theta = Function('theta')(t)
force = symbols('F')
b = symbols('b')
generalized_coordinates = [z, theta]
generalized_forces = [force, 0]
generalized_damping = [b*P.z_dot, 0]

# Finding Kinetic Energy
parameters = KE.Task_B(length, mass1, mass2, theta, z, t)
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
    
print("\nTask B Kinetic Energy:")
display_formula(ke_symbolic)

# Finding Potential Energy
num_PE = 1
parameters = PE.Task_B(length, mass1, theta)
pe_symbolic, pe_evaluate = compute_potential_energy(num_PE, parameters)

print("\nTask B Potential Energy:")
display_formula(pe_symbolic)

L_symbolic = ke_symbolic - pe_symbolic
print("\nTask B Lagrangian")
display_formula(L_symbolic)

EoM_symbolic = compute_eom_lagrangian(L_symbolic, generalized_coordinates, generalized_forces, generalized_damping, t)
print("\nTask B Equations of Motion")
for eom in EoM_symbolic:
    display_formula(eom)

# %%

#------------------------------------------------------------------------------
#-----------------Design Study C: Satellite Attitude Control-------------------
#------------------------------------------------------------------------------

# System Parameters
num_bodies = 2
mass1 = symbols('m_1')
mass2 = symbols('m_2')
theta = Function('theta')(t)
phi = Function('phi')(t)
k = symbols('k')
tau = symbols('tau')
b = symbols('b')
generalized_coordinates = [theta, phi]
generalized_forces = [tau, 0]
generalized_damping = [b*(P.theta_dot - P.phi_dot),
                       b*(P.phi_dot - P.theta_dot)]

# Finding Kinetic Energy
parameters = KE.Task_C(mass1, mass2, theta, phi, t)
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)

print("\nTask C Kinetic Energy:")
display_formula(ke_symbolic)

# Finding Potential Energy
num_PE = 1
parameters = PE.Task_C(theta, phi, k)
pe_symbolic, pe_eveluate = compute_potential_energy(num_PE, parameters)

print("\nTask C Potential Energy:")
display_formula(pe_symbolic)

# Lagrangian
L_symbolic = ke_symbolic - pe_symbolic
print("\nTask C Lagrangian")
display_formula(L_symbolic)

# Equations of motion
EoM_symbolic = compute_eom_lagrangian(L_symbolic, generalized_coordinates, generalized_forces, generalized_damping, t)
print("\nTask C Equations of Motion")
for eom in EoM_symbolic:
    display_formula(eom)

# %%

#------------------------------------------------------------------------------
#-----------------Design Study D: Mass Spring Damper-------------------
#------------------------------------------------------------------------------

# System Parameters
num_bodies = 1
mass = symbols('m')
k = symbols('k')
z = Function('z')(t)
F = symbols('F')
b = symbols('b')
generalized_coordinates = [z]
generalized_forces = [F]
generalized_damping = [b*P.z_dot]

# Finding Kinetic Energy
parameters = KE.Task_D(mass, z)
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)

print("\nTask D Kinetic Energy:")
display_formula(ke_symbolic)

# Finding Potential Energy
num_PE = 1
parameters = PE.Task_D(k, z)
pe_symbolic, pe_evaluate = compute_potential_energy(num_PE, parameters)

print("\nTask D Potential Energy")
display_formula(pe_symbolic)

# Lagrangian
L_symbolic = ke_symbolic - pe_symbolic
print("\nTask D Lagrangian")
display_formula(L_symbolic)

# Equations of motion
EoM_symbolic = compute_eom_lagrangian(L_symbolic, generalized_coordinates, generalized_forces, generalized_damping, t)
print("\nTask D Equations of Motion")
for eom in EoM_symbolic:
    display_formula(eom)

# %%

#------------------------------------------------------------------------------
#----------------------Design Study E: Block on Beam------------------------
#------------------------------------------------------------------------------

# System Parameters
num_bodies = 2
mass1 = symbols('m_1')
mass2 = symbols('m_2')
length = symbols('l')
theta = Function('theta')(t)
z = Function('z')(t)
F = symbols('F')
generalized_coordinates = [theta, z]
generalized_forces = [F*length*sp.cos(theta), 0]
generalized_damping = [0,0]

# Finding Kinetic Energy
parameters = KE.Task_E(mass1, mass2, length, theta, z, t)
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)

print("\nTask E Kinetic Energy:")
display_formula(ke_symbolic)

# Finding Potential Energy
num_PE = 2
parameters = PE.Task_E(mass1, mass2, length, theta, z)
pe_symbolic, pe_evaluate = compute_potential_energy(num_PE, parameters)

print("\nTask E Potential Energy")
display_formula(pe_symbolic)

# Lagrangian
L_symbolic = ke_symbolic - pe_symbolic
print("\nTask E Lagrangian")
display_formula(L_symbolic)

# Equations of motion
EoM_symbolic = compute_eom_lagrangian(L_symbolic, generalized_coordinates, generalized_forces, generalized_damping, t)
print("\nTask E Equations of Motion")
for eom in EoM_symbolic:
    display_formula(eom)

# %%

#------------------------------------------------------------------------------
#----------------------Design Study F: Block on Beam------------------------
#------------------------------------------------------------------------------

# System Parameters
num_bodies = 3
massc = symbols('m_c')
# massr = symbols('mr')
# massl = symbols('ml')
massr = massl = symbols('m_r')
distance = symbols('d')
Jc = symbols('J_c')
z = Function('z')(t)
h = Function('h')(t)
theta = Function('theta')(t)
fl = symbols('f_l')
fr = symbols('f_r')
b = symbols('b')
mu = symbols('mu')
generalized_coordinates = [z, h, theta]
generalized_forces = [-(fl+fr)*sp.sin(theta), (fl+fr)*sp.cos(theta), (fr-fl)*distance]
generalized_damping = [mu*P.z_dot, 0.0, 0.0]

# Finging Kinetic Energy
parameters = KE.Task_F(massr, massl, massc, distance, Jc, z, h, theta, t)
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)

print("\nTask F Kinetic Energy:")
display_formula(ke_symbolic)

# Finding Potential Energy
num_PE = 3
parameters = PE.Task_F(massr, massl, massc, h, distance, theta)
pe_symbolic, pe_evaluate = compute_potential_energy(num_PE, parameters)

print("\nTask F Potential Energy")
display_formula(pe_symbolic)

# Lagrangian
L_symbolic = ke_symbolic - pe_symbolic
print("\nTask F Lagrangian")
display_formula(L_symbolic)

# Equations of motion
EoM_symbolic = compute_eom_lagrangian(L_symbolic, generalized_coordinates, generalized_forces, generalized_damping, t)
print("\nTask F Equations of Motion")
for eom in EoM_symbolic:
    display_formula(eom)

# %%