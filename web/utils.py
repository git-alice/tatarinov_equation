import cloudpickle as pickle
from pathlib import Path

data_dir = Path('/home/alice/Documents/Course/tatarinov_equation/triangle_platform/data')

def load(name):
    with open(data_dir.joinpath(f'{name}.pickle'), 'rb') as f:
        data = pickle.load(f)
    return data
