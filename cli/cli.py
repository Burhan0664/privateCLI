from typing import Optional

import typer

from __init__ import __app_name__, __version__

#first thin when you start the your cli and recursive all the time for begin of project
app = typer.Typer()
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
