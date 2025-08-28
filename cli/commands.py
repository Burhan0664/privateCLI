from typing import Optional

import typer

from cli.__init__ import __app_name__, __version__ , ERRORS 
from . import config, database
#first thin when you start the your cli and recursive all the time for begin of project
app = typer.Typer()
@app.command()
def init(
    db_path: str =typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="to-do database location?",
    ),
) -> None:
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The to-do database is {db_path}", fg=typer.colors.GREEN)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

#command is a parameter of typer library for create any command whatever you want 
@app.command()
def githubInformation(name:str , password:str):
    print(f"Github name : {name}")
    print(f"Github password : {password}")
    typer.echo(f"Welcome to my CLI {name}")
    # get the data from db and match input parameters

#callback is a parameter of typer library for recursive the main func
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        "--vers",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    


    return
