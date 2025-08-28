from . import commands
from . import __app_name__


def main():
    commands.app(prog_name = __app_name__)

if __name__ == "__main__":
    main()
