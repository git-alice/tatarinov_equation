from sympy import latex
import timeago
from datetime import datetime
from typing import List, Union
from pathlib import Path

from tatarinov.database.pickle import Pickled
from tatarinov.database.singleton import db

db_root = Path('../data/')


def preprocess_item(item: Pickled) -> Pickled:
    if isinstance(item.obj, list):
        latex_seq = ''
        for sub_item in item.obj:
            latex_seq += f'$$ {latex(sub_item)} $$ \n'
        item.latex = latex_seq
    else:
        item.latex = f'$$ {latex(item.obj)} $$ \n'

    print(item.latex)
    print(item.latex)
    item.str_when_saved = item.when_saved.strftime("%Y-%m-%d %H:%M:%S")
    item.str_saved_time_ago = timeago.format(item.when_saved, datetime.now())
    return item


def all_equations(problem_path: Union[str, Path] = 'body_with_F') -> List[Pickled]:
    problem_path = Path(problem_path) if type(problem_path) != Path else problem_path
    db.set_root(db_root / problem_path)
    data = db.load_all()
    return [preprocess_item(item) for item in data]


def equation_by_name(problem_path: Union[str, Path], name: str) -> List[Pickled]:
    """

    @param problem_path: Union[str, Path], Папка с данными по задаче
    @param name: str, Имя объекта
    @return: Pickled, Объект
    """
    problem_path = Path(problem_path) if type(problem_path) != Path else problem_path
    db.set_root(db_root / problem_path)
    return [preprocess_item(db.load(name))]


def all_equation_names(problem_path: Union[str, Path] = 'body_with_F') -> List[str]:
    """

    @param problem_path: Union[str, Path], Папка с данными по задаче
    @return: List[str], Список имен
    """
    problem_path = Path(problem_path) if type(problem_path) != Path else problem_path
    db.set_root(db_root / problem_path)
    return db.get_all_names()


def all_problems() -> List[str]:
    """

    @return: List[str], Список задач
    """
    db.set_root(db_root)
    return db.all_problems()
