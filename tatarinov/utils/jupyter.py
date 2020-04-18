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


def display_obj(obj: Any, description: str = None) -> None:
    """

    @param obj: Any
    @param description: str, Описание вывода
    @return: None
    """
    display(Markdown(f'__{description}__'))
    display(obj)


def debug_display(obj: Any, description: str = None) -> None:
    """

    @param obj: Any, Любой объект для промежуточного вывода
    @param description: str, Описание вывода
    @return: None
    """
    display(Markdown('_dubug output ↓_'))
    display(Markdown(f'__{description}__'))
    display(obj)
    display(Markdown('---'))
