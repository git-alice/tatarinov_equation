from sympy import Matrix, Eq, Add
from sympy.abc import t
from typing import Sequence


def MatrixElDerivative(mat: Matrix) -> Matrix:
    """

    @param mat: Matrix
    @return: Matrix

    например Matrix([x(t)**2, sin(x(t))]) -> Matrix([2*x(t), cos(x(t))])
    """
    return Matrix([x.diff(t) for x in mat])


def subs_Eqs(eq: Add, eqs: Sequence[Eq]) -> Add:
    """
        TODO: Проверить какой класс является базовым для всех выражений sympy
        @param eq: expression
        @param eqs: Eq
        @return: expression

        Например: x = z+2*y
        Это eq.subs({x: z+2*y})
    """
    for eq in eqs:
        left, right = eq.args[0], eq.args[1]
        eq = eq.subs({left: right})
    return eq
