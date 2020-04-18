from sympy import latex
import timeago
from datetime import datetime
from typing import List

from tatarinov.database.pickle import Pickled
from tatarinov.database.singleton import db

db.set_root('../data/body_with_F/')


def all_equations() -> List[Pickled]:
    data = db.load_all()
    for item in data:
        item.latex = latex(item.obj)
        item.str_when_saved = item.when_saved.strftime("%Y-%m-%d %H:%M:%S")
        item.str_saved_time_ago = timeago.format(item.when_saved, datetime.now())
    return data


def equation_by_name(name: str) -> Pickled:
    """

    @param name: str, Имя объекта
    @return: Pickled, Объект
    """
    return db.load(name)


def all_equation_names() -> List[str]:
    """

    @return: List[str], Список имен
    """
    return db.get_all_names()
