from sympy import Matrix

from IPython.display import display, Markdown

def MatrixElDerivative(mat):
    return Matrix([x.diff(t) for x in mat])


def subs_Eqs(eq, Eqs):
    """
        Например: x = z+2*y
        Это eq.subs({x: z+2*y})
    """
    for Eq in Eqs:
        left, right = Eq.args[0], Eq.args[1]
        eq = eq.subs({left: right})
    return eq


def display_list(l, spaces: bool = False):
    for x in l:
        if spaces:
            display(Markdown('---'))
            # print('@@@'.center('_', 50))
        display(x)
