from datetime import datetime
from sympy import Eq

class Serializable:
    def __init__(self):
        pass

    def _save_data_hook(self):
        pass

    def _load_data_hook(self):
        pass


class SEq(Serializable, Eq):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        self.when_saved: datetime = datetime.now()
        self.description: str = 'Описание отсутствует.'

    def _save_data_hook(self, **kwargs: dict) -> None:
        self.when_saved = datetime.now()
        self.description = kwargs['description']

