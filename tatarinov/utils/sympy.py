from sympy import Matrix, Eq, Add, symbols
from sympy.abc import t
from typing import Sequence


def _eqs_subs_vars_hack(eqs, vars):
    tmp_eqs = []
    tmp_vars = symbols(', '.join([f'tmp{i}' for i in range(len(vars))]))
    sub_tmp_vars = {v: tv for v, tv in zip(vars, tmp_vars)}
    for eq in eqs:
        tmp_eqs.append(eq.subs(sub_tmp_vars))
    return tmp_eqs, tmp_vars


def apply_hack(func, eqs, vars):
    tmp_eqs, tmp_vars = _eqs_subs_vars_hack(eqs, vars)
    func_res = func(tmp_eqs, tmp_vars)
    undo_subs_tmp_vars = {tv: v for v, tv in zip(vars, tmp_vars)}
    try:
        res = []
        for i in range(len(func_res)):
            res.append(func_res[i].subs(undo_subs_tmp_vars))
    except:
        res = func_res.subs(undo_subs_tmp_vars)
    return res


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
