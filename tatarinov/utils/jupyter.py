from IPython.display import display, Markdown
from typing import Any, Sequence


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


def display_obj(obj: Any) -> None:
    """

    @type obj: object
    """
    display(obj)
