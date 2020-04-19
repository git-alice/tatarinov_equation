from termcolor import cprint
from pprint import pprint
from typing import Any


def cpprint(obj: Any, color: str = 'magenta', pr_str: str = '***', line_symbs: int = 150):
    """
    печатает объект, перед этим напечатав поясняющую цветную строку

    @param obj:
    @param color:
    @param pr_str:
    @param line_symbs:
    @return:
    """
    cprint('\n' + ('[' + pr_str + ']').center(line_symbs, '.') + '\n', color)
    pprint(obj)
