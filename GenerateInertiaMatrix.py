import sympy as sp

def generate_inertia_matrix(shape, mass, dimensions):
    """
    Generates a symbolic inertia matrix for common engineering shapes.
    
    Parameters:
    - shape (str): The type of the shape ('sphere', 'cylinder', 'ring', 'rectangular_prism', 'thin_plate', 'thin_rod').
    - mass (sympy.Symbol): The mass of the object, can be symbolic or numeric.
    - dimensions (dict): A dictionary of the dimensions of the object, where keys and values depend on the shape.
    
    Returns:
    - sympy.Matrix: The symbolic inertia matrix for the given shape.
    """
    # Define variables for inertia components
    I_xx, I_yy, I_zz = 0, 0, 0
    
    if shape == 'sphere':
        # Sphere: dimensions should contain the radius 'r'
        r = dimensions['r']
        I = 2/5 * mass * r**2
    
    elif shape == 'cylinder':
        # Cylinder: dimensions should contain the radius 'r' and height 'h'
        r, h = dimensions['r'], dimensions['h']
        I_zz = 1/2 * mass * r**2
        I_xx = I_yy = 1/12 * mass * (3*r**2 + h**2)
    
    elif shape == 'ring':
        # Ring (Thin-Walled Tube): dimensions should contain the radius 'r' and height 'h'
        r, h = dimensions['r'], dimensions['h']
        I_zz = mass * r**2
        I_xx = I_yy = 1/12 * mass * (6*r**2 + h**2)
    
    elif shape == 'rectangular_prism':
        # Rectangular Prism: dimensions should contain width 'w', height 'h', and depth 'd'
        w, h, d = dimensions['w'], dimensions['h'], dimensions['d']
        I_xx = 1/12 * mass * (h**2 + d**2)
        I_yy = 1/12 * mass * (w**2 + d**2)
        I_zz = 1/12 * mass * (w**2 + h**2)
    
    elif shape == 'thin_plate':
        # Thin Plate: dimensions should contain width 'w' and height 'h'
        w, h = dimensions['w'], dimensions['h']
        I_xx = 1/12 * mass * h**2
        I_yy = 1/12 * mass * w**2
        I_zz = 1/12 * mass * (w**2 + h**2)
        
    elif shape == 'thin_rod_x':
        # Thin Rod: dimensions should contain length 'l'
        l = dimensions['l']
        I_zz = I_yy = 1/12 * mass * l**2
        I_xx = 0

    elif shape == 'thin_rod_z':
        # Thin Rod: dimensions should contain length 'l'
        l = dimensions['l']
        I_xx = I_yy = 1/12 * mass * l**2
        I_zz = 0

    elif shape == 'point_mass':
        # Point mass
        I_xx = I_yy = I_zz = 0

    else:
        raise ValueError("Shape not recognized.")
    
    if 'I' in locals():
        # Sphere has a uniform inertia matrix
        inertia_matrix = sp.Matrix([[I, 0, 0], [0, I, 0], [0, 0, I]])
    else:
        inertia_matrix = sp.Matrix([[I_xx, 0, 0], [0, I_yy, 0], [0, 0, I_zz]])
    
    return inertia_matrix