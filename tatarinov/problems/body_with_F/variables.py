from sympy import IndexedBase, symbols, Matrix, Idx
from sympy import cos, sin

L, m, x, y, t, alpha = symbols('L, m, x, y, t, alpha')
nu1, nu2, nu3 = symbols('nu1, nu2, nu3')
W, T = symbols('W, T')
s = symbols('s')
P = IndexedBase('P')
p = IndexedBase('p')
omega = IndexedBase('omega')
v = IndexedBase('v')
Q = IndexedBase('Q')
k = symbols('k', cls=Idx)
J = IndexedBase('J')

xi, eta = symbols('xi, eta')
e = {
    'x': Matrix([1, 0]),
    'y': Matrix([0, 1]),
    'xi': Matrix([cos(alpha), sin(alpha)]),
    'eta': Matrix([-sin(alpha), cos(alpha)])
}
