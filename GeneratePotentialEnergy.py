import sympy as sp
from sympy import symbols, Matrix, diff, simplify
from sympy.physics.mechanics import dynamicsymbols

def compute_potential_energy(num_PE, parameters):
    """
    Computes the total potential energy of a system of rigid bodies by calculating both gravitational and elastic potential energy components for each body.
    
    Parameters:
    - num_PE: The number of methods of storing potential energy.
    - parameters: A dictionary containing the physical parameters (mass, position/velocity, inertia matrix, and angular velocity) for each body.
    
    Returns:
    - The symbolic total potential energy expression of the system.
    - A function to evaluate this potential energy by substituting numerical values for the symbolic variables.
    """
    # Initialize the total potential energy to zero
    total_potential_energy = 0
    g = symbols('g')
    
    # Iterate over each body to compute its contribution to the total potential energy
    for i in range(num_PE):
        # Use the correct equation for gravitational vs potential energy
        if parameters[i]['type'] == 'gravitational':
            mass = parameters[i]['mass']
            height = parameters[i]['height']
            total_potential_energy += mass*g*height
        elif parameters[i]['type'] == 'elastic':
            k = parameters[i]['k']
            stretch = parameters[i]['stretch']
            total_potential_energy += 1/2*k*stretch**2
        else:
            print("PE type not recognized")
    
    # Simplify the total kinetic energy expression for cleaner output
    total_potential_energy_simplified = simplify(total_potential_energy)
    
    # Define a function to evaluate the kinetic energy with numerical values
    def evaluate_potential_energy(**values):
        return total_potential_energy_simplified.evalf(subs=values)
    
    # Return the symbolic kinetic energy expression and the evaluation function
    return total_potential_energy_simplified, evaluate_potential_energy
