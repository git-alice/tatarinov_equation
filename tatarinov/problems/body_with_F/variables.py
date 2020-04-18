from sympy import IndexedBase, symbols, Matrix, Idx
from sympy import cos, sin
from sympy.physics.vector import dynamicsymbols

# L, m, x, y, t, alpha = symbols('L, m, x, y, t, alpha')
p = IndexedBase('p')
J = IndexedBase('J')
v = IndexedBase('v')
omega = IndexedBase('omega')

k = symbols('k', cls=Idx)

x, y, alpha = dynamicsymbols('x, y , alpha')

t, xi, eta = symbols('t, xi, eta')
L, m = symbols('L, m')
W, T = symbols('W, T')
s = symbols('s')
nu1, nu2, nu3 = dynamicsymbols('nu1, nu2, nu3')


e = {
    'x': Matrix([1, 0]),
    'y': Matrix([0, 1]),
    'xi': Matrix([cos(alpha), sin(alpha)]),
    'eta': Matrix([-sin(alpha), cos(alpha)])
}

r = {}
r['s'] = x * e['x'] + y * e['y']
r['p'] = r['s'] + xi * e['xi'] + eta * e['eta']