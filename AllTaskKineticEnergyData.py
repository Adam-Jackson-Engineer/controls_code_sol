import Param as P
import sympy as sp
from GenerateInertiaMatrix import generate_inertia_matrix
from sympy import diff, symbols

def Task_A(length, mass, theta, t):
    shape = 'thin_rod_x'
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
    return parameters

def Task_B(length, mass1, mass2, theta, z, t):
    shape1 = 'thin_rod_x'
    shape2 = 'point_mass'
    inertia1_dimensions = {'l': length}
    inertia1_matrix = generate_inertia_matrix(shape1,mass1,inertia1_dimensions)
    inertia2_dimensions = {}
    inertia2_matrix = generate_inertia_matrix(shape2,mass2,inertia2_dimensions)
    parameters = {
        0: {
            'mass': mass1,
            'position': [z + length/2*sp.sin(theta),
                        length/2*sp.cos(theta), 
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
    return parameters

def Task_C(mass1, mass2, theta, phi, t):
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
    return parameters

def Task_D(mass, z):
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
    return parameters

def Task_E(mass1, mass2, length, theta, z, t):
    shape1 = 'point_mass'
    shape2 = 'thin_rod_x'
    inertia1_dimensions = {}
    inertia1_matrix = generate_inertia_matrix(shape1,mass1,inertia1_dimensions)
    inertia2_dimensions = {'l':length}
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
            'position': [length/2*sp.cos(theta),
                        length/2*sp.sin(theta),
                        0],
            'inertia_matrix': inertia2_matrix,
            'angular_velocity': [0,0,diff(theta,t)],
        }
    }
    return parameters

def Task_F(massr, massl, massc, distance, Jc, z, h, theta, t):
    shaper = 'point_mass'
    shapel = 'point_mass'
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
    return parameters