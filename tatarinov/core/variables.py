from sympy import IndexedBase, Idx, Matrix
from sympy import symbols, cos, sin
from sympy.physics.vector import dynamicsymbols

p = IndexedBase('p')
P = IndexedBase('P')
Q = IndexedBase('Q')
v = IndexedBase('v')
_omega = IndexedBase('omega')
_v = IndexedBase('v')
k = symbols('k', cls=Idx)
i = symbols('i', cls=Idx)
t, alpha = symbols('t, alpha')

x, y = dynamicsymbols('x, y')

e = {
    'x': Matrix([1, 0]),
    'y': Matrix([0, 1]),
    'xi': Matrix([cos(alpha), sin(alpha)]),
    'eta': Matrix([-sin(alpha), cos(alpha)])
}


def create_fs(smt):
    raise Exception('Что то пошло не так!')
