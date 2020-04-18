from sympy import IndexedBase, symbols, Matrix, Idx
from sympy import cos, sin
from sympy.physics.vector import dynamicsymbols

J = IndexedBase('J')
v = IndexedBase('v')
omega = IndexedBase('omega')

k = symbols('k', cls=Idx)

nu1, nu2, nu3 = dynamicsymbols('nu1, nu2, nu3')
x, y = dynamicsymbols('x, y')
psi, theta, phi = dynamicsymbols('psi, theta, phi')
alpha = dynamicsymbols('alpha')

t, xi, eta, g = symbols('t, xi, eta, g')
L, m = symbols('L, m')
A, C = symbols('A, C')

# TODO: То что далее написано неверно, но не влияет на решение, так как используется только в получении Q,
#  которые в свою очередь зависят от F, которая в свою очередь нулевая

e = {
    'x': Matrix([1, 0]),
    'y': Matrix([0, 1]),
    'xi': Matrix([cos(alpha), sin(alpha)]),
    'eta': Matrix([-sin(alpha), cos(alpha)])
}

r = {}
r['s'] = x * e['x'] + y * e['y']
r['p'] = r['s'] + xi * e['xi'] + eta * e['eta']
