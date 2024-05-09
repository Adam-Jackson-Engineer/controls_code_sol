import sympy as sp
from sympy import symbols, Function, Matrix, diff, simplify
from GenerateInertiaMatrix import generate_inertia_matrix
from GenerateKineticEnergy import compute_kinetic_energy

sp.init_printing(use_latex='mathjax')

# %%

#------------------------------------------------------------------------------
#--------------------Design Study A: Single Link Robot Arm---------------------
#------------------------------------------------------------------------------

num_bodies = 1
shape = 'thin_rod_x'
mass = symbols('m')
length = symbols('l')
t = symbols('t')
theta = Function('theta')(t)
theta_dot = symbols(r'\dot{\theta}')

inertia_dimensions = {'l': length}
inertia_matrix = generate_inertia_matrix(shape,mass,inertia_dimensions)
parameters = {
    0: {
        'mass': mass,
        'position': [length/2*sp.cos(theta),
                     length/2*sp.sin(theta), 
                     0],
        'inertia_matrix': inertia_matrix,
        'angular_velocity': [0, 0, diff(theta, t)],
    }
}

ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
ke_symbolic_dot_notation = ke_symbolic.subs(diff(theta, t), theta_dot)

print("Task A Kinetic Energy:")

try:
    display(sp.nsimplify(ke_symbolic_dot_notation))
except:
    sp.pprint(ke_symbolic)
    input("Hit ENTER to move on")

# %%

#------------------------------------------------------------------------------
#----------------------Design Study B: Pendulum on Cart------------------------
#------------------------------------------------------------------------------
num_bodies = 2
shape1 = 'thin_rod_x'
shape2 = 'point_mass'
mass1 = symbols('m1')
mass2 = symbols('m2')
length1 = symbols('l')
t = symbols('t')
theta = Function('theta')(t)
theta_symbol = symbols('theta')
theta_dot = symbols(r'\dot{\theta}')
z = Function('z')(t)
z_symbol = symbols('z')
z_dot = symbols(r'\dot{z}')

inertia1_dimensions = {'l': length}
inertia1_matrix = generate_inertia_matrix(shape1,mass1,inertia1_dimensions)
inertia2_dimensions = {}
inertia2_matrix = generate_inertia_matrix(shape2,mass2,inertia2_dimensions)
parameters = {
    0: {
        'mass': mass1,
        'position': [z + length1/2*sp.sin(theta),
                     length1/2*sp.cos(theta), 
                     0],
        'inertia_matrix': inertia1_matrix,
        'angular_velocity': [0, 0, diff(theta, t)],
    },
    1: {
        'mass': mass2,
        'position': [z,
                     0,
                     0],
        'inertia_matrix': inertia2_matrix,
        'angular_velocity': [0,0,0],
    }
}

substitutions = [(diff(theta, t),theta_dot),
(diff(z,t), z_dot),
(theta, theta_symbol),
(z, z_symbol)]
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
ke_symbolic_dot_notation = ke_symbolic.subs(substitutions)

print("Task B Kinetic Energy:")
try:
    display(sp.nsimplify(ke_symbolic_dot_notation))
except:
    sp.pprint(ke_symbolic)
    input("Hit ENTER to move on")
# %%

#------------------------------------------------------------------------------
#-----------------Design Study C: Satellite Attitude Control-------------------
#------------------------------------------------------------------------------

num_bodies = 2
mass1 = symbols('m1')
mass2 = symbols('m2')
t = symbols('t')
theta = Function('theta')(t)
theta_symbol = symbols('theta')
theta_dot = symbols(r'\dot{\theta}')
phi = Function('phi')(t)
phi_symbol = symbols('phi')
phi_dot = symbols(r'\dot{\phi}')

parameters = {
    0: {
        'mass': mass1,
        'position': [0,
                     0, 
                     0],
        'inertia_matrix': [[symbols('J1xx'), 0, 0], 
                           [0, symbols('J1yy'),0], 
                           [0, 0, symbols('Js')]],
        'angular_velocity': [0, 0, diff(theta, t)],
    },
    1: {
        'mass': mass2,
        'position': [0,
                     0,
                     0],
        'inertia_matrix': [[symbols('J2xx'), 0, 0], 
                           [0, symbols('J2yy'),0], 
                           [0, 0, symbols('Jp')]],
        'angular_velocity': [0,0,diff(phi,t)],
    }
}


substitutions = [(diff(theta, t),theta_dot),
(diff(phi,t), phi_dot),
(theta, theta_symbol),
(phi, phi_symbol)]

ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
ke_symbolic_dot_notation = ke_symbolic.subs(substitutions)

print("Task C Kinetic Energy:")
try:
    display(sp.nsimplify(ke_symbolic_dot_notation))
except:
    sp.pprint(ke_symbolic)
    input("Hit ENTER to move on")

# %%

#------------------------------------------------------------------------------
#-----------------Design Study D: Mass Spring Damper-------------------
#------------------------------------------------------------------------------

num_bodies = 1
mass = symbols('m')
z = Function('z')(t)
z_symbol = symbols('z')
z_dot = symbols(r'\dot{z}')

parameters = {
    0: {
        'mass': mass,
        'position': [0,
                     0, 
                     z],
        'inertia_matrix': [[0, 0, 0], 
                           [0, 0, 0], 
                           [0, 0, 0]],
        'angular_velocity': [0, 0, 0],
    }
}

print("Task D Kinetic Energy:")
substitutions = [(diff(z,t), z_dot),
(z, z_symbol)]
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
ke_symbolic_dot_notation = ke_symbolic.subs(substitutions)

try:
    display(sp.nsimplify(ke_symbolic_dot_notation))
except:
    sp.pprint(ke_symbolic)
    input("Hit ENTER to move on")

# %%

#------------------------------------------------------------------------------
#----------------------Design Study E: Block on Beam------------------------
#------------------------------------------------------------------------------
num_bodies = 2
shape1 = 'point_mass'
shape2 = 'thin_rod_x'
mass1 = symbols('m1')
mass2 = symbols('m2')
length2 = symbols('l')
t = symbols('t')
theta = Function('theta')(t)
theta_symbol = symbols('theta')
theta_dot = symbols(r'\dot{\theta}')
z = Function('z')(t)
z_symbol = symbols('z')
z_dot = symbols(r'\dot{z}')

inertia1_dimensions = {}
inertia1_matrix = generate_inertia_matrix(shape1,mass1,inertia1_dimensions)
inertia2_dimensions = {'l':length2}
inertia2_matrix = generate_inertia_matrix(shape2,mass2,inertia2_dimensions)
parameters = {
    0: {
        'mass': mass1,
        'position': [z*sp.cos(theta),
                     z*sp.sin(theta),
                     0],
        'inertia_matrix': inertia1_matrix,
        'angular_velocity': [0, 0, diff(theta, t)],
    },
    1: {
        'mass': mass2,
        'position': [length2/2*sp.cos(theta),
                     length2/2*sp.sin(theta),
                     0],
        'inertia_matrix': inertia2_matrix,
        'angular_velocity': [0,0,diff(theta,t)],
    }
}

substitutions = [(diff(theta, t),theta_dot),
(diff(z,t), z_dot),
(theta, theta_symbol),
(z, z_symbol)]
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
ke_symbolic_dot_notation = ke_symbolic.subs(substitutions)

print("Task E Kinetic Energy:")
try:
    display(sp.nsimplify(ke_symbolic_dot_notation))
except:
    sp.pprint(ke_symbolic)
    input("Hit ENTER to move on")

# %%

#------------------------------------------------------------------------------
#----------------------Design Study F: Block on Beam------------------------
#------------------------------------------------------------------------------
num_bodies = 3
shaper = 'point_mass'
shapel = 'point_mass'
massc = symbols('mc')
massr = symbols('mr')
massl = symbols('ml')
distance = symbols('d')
Jc = symbols('Jc')

t = symbols('t')
z = Function('z')(t)
z_symbol = symbols('z')
z_dot = symbols(r'\dot{z}')
h = Function('h')(t)
h_symbol = symbols('h')
h_dot = symbols(r'\dot{h}')
theta = Function('theta')(t)
theta_symbol = symbols('theta')
theta_dot = symbols(r'\dot{\theta}')

inertiar_dimensions = {}
inertiar_matrix = generate_inertia_matrix(shaper,massr,inertiar_dimensions)
inertial_dimensions = {}
inertial_matrix = generate_inertia_matrix(shapel,massl,inertial_dimensions)
parameters = {
    0: {
        'mass': massc,
        'position': [z,
                     h,
                     0],
        'inertia_matrix': [[0, 0, 0], 
                           [0, 0, 0], 
                           [0, 0, Jc]],
        'angular_velocity': [0, 0, diff(theta, t)],
    },
    1: {
        'mass': massr,
        'position': [z + distance * sp.cos(theta),
                     h + distance * sp.sin(theta),
                     0],
        'inertia_matrix': inertiar_matrix,
        'angular_velocity': [0,0,diff(theta,t)],
    },
    2: {
        'mass': massl,
        'position': [z - distance * sp.cos(theta),
                     h - distance * sp.sin(theta),
                     0],
        'inertia_matrix': inertial_matrix,
        'angular_velocity': [0,0,diff(theta,t)],
    }
}

substitutions = [(diff(theta, t),theta_dot),
(diff(z,t), z_dot),
(diff(h,t), h_dot),
(theta, theta_symbol),
(z, z_symbol),
(h, h_symbol)]
ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
ke_symbolic_dot_notation = ke_symbolic.subs(substitutions)

print("Task F Kinetic Energy:")
try:
    display(sp.nsimplify(ke_symbolic_dot_notation))
except:
    sp.pprint(ke_symbolic)
    input("Hit ENTER to move on")

# %%

#------------------------------------------------------------------------------
#--------------------------------Generic Case----------------------------------
#------------------------------------------------------------------------------

# Generic 2 body system: Example of defining a system with two bodies and their parameters
num_bodies = 2
parameters = {
    0: {
        'mass': symbols('m1'),
        'position': [Function('x1')(t), Function('y1')(t), Function('z1')(t)],
        'inertia_matrix': [[symbols('I1xx'), symbols('I1xy'), symbols('I1xz')], 
                           [symbols('I1xy'), symbols('I1yy'), symbols('I1yz')], 
                           [symbols('I1xz'), symbols('I1yz'), symbols('I1zz')]],
        'angular_velocity': [symbols('w1x'), symbols('w1y'), symbols('w1z')],
    },
    1: {
        'mass': symbols('m2'),
        'velocity': [symbols('v2x'), symbols('v2y'), symbols('v2z')],
        'inertia_matrix': [[symbols('I2xx'), symbols('I2xy'), symbols('I2xz')], 
                           [symbols('I2xy'), symbols('I2yy'), symbols('I2yz')], 
                           [symbols('I2xz'), symbols('I2yz'), symbols('I2zz')]],
        'angular_velocity': [symbols('w2x'), symbols('w2y'), symbols('w2z')],
    }
}

ke_symbolic, ke_evaluate = compute_kinetic_energy(num_bodies, parameters)
ke_symbolic

values = {'m1': 1, 'v1x': 1, 'v1y': 0, 'v1z': 0, 'I1xx': 1, 'I1yy': 1, 'I1zz': 1, 'x1': 1, 'y1': 0, 'z1': 0,
          'm2': 2, 'v2x': 0, 'v2y': 1, 'v2z': 0, 'I2xx': 2, 'I2yy': 2, 'I2zz': 2, 'w2x': 0, 'w2y': 1, 'w2z': 0}
ke_evaluate(**values)
