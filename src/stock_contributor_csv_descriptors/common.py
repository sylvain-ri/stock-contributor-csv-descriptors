from datetime import datetime as dt
from pathlib import Path


DEFAULT_MAIN_CSV = f"{dt.now():%Y-%m-%d_%H-%M}_Descriptor-Master.csv"
PATH_CSV_TEMPLATE = "../../CSV_Samples/MasterTemplate.csv"


def is_dir_path(path: str) -> str:
    """ check that a path is a valid directory """
    if Path.is_dir(Path(path)):
        return path
    else:
        raise NotADirectoryError(path)


def is_file_path(path: str) -> str:
    """ check that a path is a valid file path """
    if Path.is_file(Path(path)):
        return path
    else:
        raise FileNotFoundError(path)

