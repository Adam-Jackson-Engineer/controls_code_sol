import sympy as sp
from sympy import symbols, Matrix, diff, simplify
from sympy.physics.mechanics import dynamicsymbols

def compute_eom_lagrangian(lagrangian, generalized_coordinates, generalized_forces, generalized_damping, t):
    """
    Computes the symbolic equations of motion for the given generalized coordinates
    
    Parameters:
    - lagrangian: The symbolic lagrangian of the system calculated as T-U (KE-PE)
    - generalized_coordinates: The coordinates used to describe the energy storage of the system
    - generalized_forces: The forces in the directions of the generalized coordinates
    - generalized_damping: Damping forces acting in the directions of the generalized coordinates
    - t: The symbolic time
    
    Returns:
    - A Matrix of the equations of motion
    """
    
    eom = []
    
    for i, coordinate in enumerate(generalized_coordinates):
        # Derivative of coordinate with respect to time (velocity)
        coordinate_dot = diff(coordinate, t)
        
        # Partial derivatives of Lagrangian with respect to coordinate and its velocity
        dL_dq = diff(lagrangian, coordinate)
        dL_dq_dot = diff(lagrangian, coordinate_dot)
        
        # Time derivative of dL/dq_dot
        d_dt_dL_dq_dot = diff(dL_dq_dot, t)
        
        # Equation of motion for this coordinate, including damping and external force
        eq_motion = d_dt_dL_dq_dot - dL_dq + generalized_damping[i] - generalized_forces[i]
        
        eom.append(eq_motion)
        
    return Matrix(eom)
