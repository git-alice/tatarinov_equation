from sympy import IndexedBase, symbols, Matrix, Idx
from sympy import cos, sin
from sympy.physics.vector import dynamicsymbols, ReferenceFrame, Point

J = IndexedBase('J')
v = IndexedBase('v')
omega = IndexedBase('omega')

k = symbols('k', cls=Idx)

nu1, nu2, nu3 = dynamicsymbols('nu1, nu2, nu3')
x, y, z = dynamicsymbols('x, y, z')
psi, theta, phi = dynamicsymbols('psi, theta, phi')
alpha = dynamicsymbols('alpha')

t, xi, eta, g = symbols('t, xi, eta, g')
L, m = symbols('L, m')
A, C = symbols('A, C')

# TODO: Доделать используя встреонные возможности sympy mechanics.

S1 = ReferenceFrame('S1') # изначалаьная система координа
S2 = S1.orientnew('S2', 'Body', (phi, psi, theta), '123') # система координат ориентированная углами Эйлера

S1toS2 = S2.dcm(S1)  # The direction cosine matrix between frames. |  Матрица поворота между системами координат


# TODO: То что далее написано неверно, но не влияет на решение, так как используется только в получении Q,
#  которые в свою очередь зависят от F, которая в свою очередь нулевая.

r = {
    'p': Matrix([0, 0])
}