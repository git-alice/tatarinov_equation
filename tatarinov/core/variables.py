from sympy import IndexedBase, Idx, Matrix
from sympy import symbols, cos, sin
from sympy.physics.vector import dynamicsymbols

P = IndexedBase('P')
Q = IndexedBase('Q')
p = IndexedBase('p')
v = IndexedBase('v')
k = symbols('k', cls=Idx)
i = symbols('i', cls=Idx)

t = symbols('t')

# TODO Под вопросом:

def create_fs(smt):
    raise Exception('Что то пошло не так!')

_omega = IndexedBase('omega')
_v = IndexedBase('v')

