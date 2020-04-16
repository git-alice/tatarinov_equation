from tatarinov.database.serialize import Serializable, SEq
import cloudpickle as pickle
from pathlib import Path
from typing import Dict, Any


class Database:
    root: Path = Path('./')

    @classmethod
    def save(cls, obj: Serializable, filename: str, **kwargs: Dict[sqtr, Any]) -> None:
        """

        @param filename: str
        @param obj: Serializable
        @param kwargs: Dict[str, Any]
        @return: None
        """
        if isinstance(obj, SEq):
            obj._save_data_hook(**kwargs)
            with open(f'{filename}.pickle', 'wb') as f:
                pickle.dump(obj, f)
        else:
            raise Exception('Тип данных не соответвует базе данных')

    @classmethod
    def load(cls, obj_name: Path) -> Serializable:
        """

        @param obj_name: Path
        @return: Serializable
        """
        return pickle.load(cls.root / obj_name)
