import sympy as sp
from sympy import Function, symbols, diff

t = symbols('t')

theta = Function('theta')(t)
theta_symbol = symbols('theta')
theta_dot = symbols(r'\dot{\theta}')
theta_ddot = symbols(r'\ddot{\theta}')
z = Function('z')(t)
z_symbol = symbols('z')
z_dot = symbols(r'\dot{z}')
z_ddot = symbols(r'\ddot{z}')
phi = Function('phi')(t)
phi_symbol = symbols('phi')
phi_dot = symbols(r'\dot{\phi}')
phi_ddot = symbols(r'\ddot{\phi}')
h = Function('h')(t)
h_symbol = symbols('h')
h_dot = symbols(r'\dot{h}')
h_ddot = symbols(r'\ddot{h}')

substitutions = [
(diff(theta, t, t), theta_ddot),
(diff(phi, t, t), phi_ddot),
(diff(z, t, t), z_ddot),
(diff(h, t, t), h_ddot),
(diff(theta, t),theta_dot),
(diff(phi, t),phi_dot),
(diff(z,t), z_dot),
(diff(h,t), h_dot),
(theta, theta_symbol),
(phi, phi_symbol),
(z, z_symbol),
(h, h_symbol),]


def display_formula(symbolic):
    try:
        symbolic_simp = sp.simplify(symbolic)
        symbolic_interactive = symbolic_simp.subs(substitutions)
        display(sp.nsimplify(symbolic_interactive))
    except:
        symbolic_simp = sp.simplify(symbolic)
        sp.pprint(symbolic_simp)
        input("Hit ENTER to continue...")
