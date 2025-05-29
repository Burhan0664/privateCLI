
import configparser # like converter
from pathlib import Path # path configure

import typer

from cli import (
    DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name_ # neccesary file 
)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__)) #get the file path where is your hold in computer
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini" #hold the configuration file itself directly


#initialize and contain function of both of function like main func
def init_app(db_path: str) -> int: 
    """Initialize the application."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code
    return SUCCESS

#initialize config file and establish file itself your path
def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS


#open db and w command is commit on your path 
def _create_database(db_path: str) -> int:
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}
    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return DB_WRITE_ERROR
    return SUCCESS