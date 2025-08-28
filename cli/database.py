"""This module provides the RP To-Do database functionality."""
# rptodo/database.py

import configparser
from pathlib import Path

from cli.__init__ import DB_WRITE_ERROR, SUCCESS


DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
) 

#
def get_database_path(config_file: Path) -> Path: #paths is a parameter and return a path
    """Return the current path to the to-do database."""
    config_parser = configparser.ConfigParser() #represents object path to database 
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"]) 

def init_database(db_path: Path) -> int: #return a int by take database path object and create a json empty list
    """Create the to-do database."""
    try:
        db_path.write_text("[]")  # Empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR