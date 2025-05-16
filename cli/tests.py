from typer.testing import CliRunner
from cli.cli import app
from cli.__init__ import __app_name__, __version__

runner = CliRunner()

def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
