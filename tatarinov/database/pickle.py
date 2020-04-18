from datetime import datetime
from sympy import Eq, Matrix


class Pickled:
    def __init__(self, obj):
        self.obj = obj
        self.when_saved: datetime = datetime.now()
        self.description: str = 'Описание отсутствует'

    def _save_data_hook(self, **kwargs: dict) -> None:
        self.when_saved = datetime.now()
        self.description: str = kwargs.get('description')

    def _load_data_hook(self):
        pass


# class SEq(Pickled, Eq):
#     """
#     Равенство которое можно пинуть
#     """
#
#     def __new__(cls, *args, **kwargs):
#         print('Fla1g')
#         print(args)
#         print(kwargs)
#         return super().__new__(cls, *args, **kwargs)
#
#     def __init__(self, *args, **kwargs):
#         print('Fla2g')
#         self.when_saved: datetime = datetime.now()
#         self.description = 'Описание отсутствует.'
#
#     def _save_data_hook(self, **kwargs: dict) -> None:
#         print(kwargs)
#         print(kwargs['description'])
#         self.when_saved = datetime.now()
#         self.description: str = kwargs['description']
#
#
# class SMatrix(Pickled, Matrix):
#     """
#     Матрица которую можно пикнуть
#     """
#
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, *args, **kwargs)
#
#     def __init__(self, *args, **kwargs):
#         self.when_saved: datetime = datetime.now()
#         self.description: str = 'Описание отсутствует.'
#
#     def _save_data_hook(self, **kwargs: dict) -> None:
#         self.when_saved = datetime.now()
#         self.description = kwargs.get('description')
