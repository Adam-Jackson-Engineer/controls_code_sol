import sympy as sp
from sympy import symbols, Matrix, diff, simplify
from sympy.physics.mechanics import dynamicsymbols

def compute_velocity(position):
    """
    Computes the symbolic velocity vector from a given position vector by differentiating each component of the position vector with respect to time.
    
    Parameters:
    - position: A list or Matrix of symbolic expressions representing the position vector of a body.
    
    Returns:
    - A Matrix representing the velocity vector of the body.
    """
    # Retrieve the symbol representing time from one of the dynamic symbols
    t = symbols('t')  # Assuming 't' is the symbol for time used in your dynamic symbols
    
    # Differentiate each component of the position vector with respect to time to compute velocity
    velocity = Matrix([diff(component, t) for component in position])
    return velocity

def compute_kinetic_energy(num_bodies, parameters):
    """
    Computes the total kinetic energy of a system of rigid bodies by calculating both translational and rotational kinetic energy components for each body.
    
    Parameters:
    - num_bodies: The number of rigid bodies in the system.
    - parameters: A dictionary containing the physical parameters (mass, position/velocity, inertia matrix, and angular velocity) for each body.
    
    Returns:
    - The symbolic total kinetic energy expression of the system.
    - A function to evaluate this kinetic energy by substituting numerical values for the symbolic variables.
    """
    # Initialize the total kinetic energy to zero
    total_kinetic_energy = 0
    
    # Iterate over each body to compute its contribution to the total kinetic energy
    for i in range(num_bodies):
        # Extract the parameters for the i-th body
        mass = parameters[i]['mass']
        inertia_matrix = Matrix(parameters[i]['inertia_matrix'])
        angular_velocity = Matrix(parameters[i]['angular_velocity'])
        
        # If velocity is not directly provided, compute it from position
        if 'velocity' not in parameters[i]:
            position = Matrix(parameters[i]['position'])
            velocity = compute_velocity(position)
            # Store the computed velocity back in the parameters dictionary
            parameters[i]['velocity'] = velocity
        else:
            velocity = Matrix(parameters[i]['velocity'])
        
        # Compute translational kinetic energy: 1/2 * mass * (velocity dot product with itself)
        translational_ke = 1/2 * mass * velocity.dot(velocity)
        
        # Compute rotational kinetic energy: 1/2 * angular_velocity.T * inertia_matrix * angular_velocity
        rotational_ke = 1/2 * angular_velocity.T * inertia_matrix * angular_velocity
        
        # Add the translational and rotational kinetic energy of the body to the total kinetic energy
        total_kinetic_energy += translational_ke + rotational_ke[0]
    
    # Simplify the total kinetic energy expression for cleaner output
    total_kinetic_energy_simplified = simplify(total_kinetic_energy)
    
    # Define a function to evaluate the kinetic energy with numerical values
    def evaluate_kinetic_energy(**values):
        return total_kinetic_energy_simplified.evalf(subs=values)
    
    # Return the symbolic kinetic energy expression and the evaluation function
    return total_kinetic_energy_simplified, evaluate_kinetic_energy
