import Param as P
import sympy as sp
from GenerateInertiaMatrix import generate_inertia_matrix
from sympy import diff

# Finding Kinetic Energy
def Task_A(length, mass, theta):
    parameters = {
        0: {
            'type': 'gravitational',
            'mass': mass,
            'height': length/2*sp.sin(theta)
        }
    }
    return parameters

def Task_B(length, mass1, theta):
    parameters = {
        0: {
            'type': 'gravitational',
            'mass': mass1,
            'height': length/2*(sp.cos(theta)-1)
        }
    }
    return parameters

def Task_C(theta, phi, k):
    parameters = {
        0: {
            'type': 'elastic',
            'k': k,
            'stretch': phi-theta
        }
    }
    return parameters

def Task_D(k, z):
    parameters = {
        0: {
            'type': 'elastic',
            'k': k,
            'stretch': z
        }
    }
    return parameters

def Task_E(mass1, mass2, length, theta, z):
    parameters = {
    0: {
        'type': 'gravitational',
        'mass': mass1,
        'height': z*sp.sin(theta),
    },
    1: {
        'type': 'gravitational',
        'mass': mass2,
        'height': length/2*sp.sin(theta),
    }
}
    return parameters

def Task_F(massr, massl, massc, h, distance, theta):
    parameters ={
        0: {
            'type': 'gravitational',
            'mass': massc,
            'height': h,
        },
        1: {
            'type': 'gravitational',
            'mass': massl,
            'height': h-distance*sp.sin(theta),
        },
        2: {
            'type': 'gravitational',
            'mass': massr,
            'height': h+distance*sp.sin(theta),
        }
    }
    return parameters