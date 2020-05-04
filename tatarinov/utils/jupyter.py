from IPython.display import display, Markdown
from typing import Any, Sequence
from tatarinov.utils.sympy import from_what
from sympy import Eq

def display_list(l: Sequence[Any], spaces: bool = False):
    """

    @param l: Sequence[Any], Последовательность объектов
    @param spaces: bool, Нужно ли разделительное пространство
    @return: None
    """
    for x in l:
        if spaces:
            display(Markdown('---'))
            # print('@@@'.center('_', 50))
        display(x)


def display_obj(obj: Any, description: str = None) -> None:
    """

    @param obj: Any
    @param description: str, Описание вывода
    @return: None
    """
    display(Markdown(f'__{description}__'))
    display(obj)


def debug_display(obj: Any = None, description: str = None) -> None:
    """

    @param obj: Any, Любой объект для промежуточного вывода
    @param description: str, Описание вывода
    @return: None
    """
    display(Markdown('_dubug output:_ '))
    display(Markdown(f'__{description}__')) if description else None
    display(obj) if obj is not None else None
    display(Markdown('---'))


def display_from_what(eq: Any) -> None:
    """

    @param eq:
    @return:
    """
    if isinstance(eq, Eq):
        display(eq.args[0])
        print(' ↓ ')
        display_list(from_what(eq.args[1]))
    else:
        display_list(from_what(eq))

def display_list_from_what(eqs: Sequence[Any]) -> None:
    """

    @param eqs:
    @return:
    """

    for eq in eqs:
        display_from_what(eq)
        display(Markdown('---'))