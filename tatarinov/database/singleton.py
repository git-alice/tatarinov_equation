from tatarinov.database.pickle import Pickled
import cloudpickle as pickle
from pathlib import Path
from typing import Dict, Any, Union, Generator, List


class Database:
    root: Path = Path('./')
    debug: bool = True

    @classmethod
    def set_root(cls, root: str) -> None:
        """

        @param root: str, Корень базы данных
        @return: None
        """
        cls.root = Path(root)

    @classmethod
    def save(cls, obj: Pickled, filename: str, **kwargs: Dict[str, Any]) -> None:
        """

        @param filename: str
        @param obj: Pickled
        @param kwargs: Dict[str, Any]
        @return: None
        """
        print(f'PWD: {Path.cwd()}, Database root: {cls.root}') if cls.debug else None
        cls.root.mkdir(parents=True, exist_ok=True)
        filename = Path(f'{filename}.pickle')

        try:
            pobj = Pickled(obj=obj)
            pobj._save_data_hook(**kwargs)
            with open(cls.root / filename, 'wb') as f:
                pickle.dump(pobj, f)
        except Exception as e:
            print('Тип данных не соответвует базе данных')
            print('isinstance: ', isinstance(obj, SEq))
            print('type: ', type(obj))
            print(e)

    @classmethod
    def load(cls, filename: str) -> Pickled:
        """

        @param filename: str, Путь к файлу относительно корня базы данных
        @return: Pickled
        """
        filename = Path(f'{filename}.pickle')
        print(f'Loading from: {cls.root / filename}') if cls.debug else None
        with open(cls.root / filename, 'rb') as f:
            return pickle.load(f)

    @classmethod
    def get_all_names(cls, ext: str = 'pickle') -> Generator[Path, None, None]:
        """

        @param ext: str, Расширение файлов
        @return: List[str], Список названия файлов
        """
        return cls.root.glob(f'*.{ext}')

    @classmethod
    def load_all(cls) -> List[Pickled]:
        objs = [cls.load(f.stem) for f in cls.get_all_names() if f.is_file()]
        return objs


db = Database
