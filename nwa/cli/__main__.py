"""Main
"""
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Callable, Dict

from nwa import settings
from nwa.cli.base_command import BaseCommand
from nwa.cli.commands import COMMANDS
from nwa.logger import LOGGER, setup_logger


def main():  # pylint: disable=R1710
    """Entry point to CLI.

    Sets up logger, output directory,
    registers `nwa` command along with
    all the available CLI command modules as subcommands.
    """
    instantiated_commands = [C() for C in COMMANDS]
    subcommands_map = {command.name: command for command in instantiated_commands}

    parser = configure_parser(subcommands_map)
    args = parser.parse_args()

    setup_logger(args.verbosity)
    bin_dir = Path(~settings.BIN_DIR)
    bin_dir.mkdir(parents=True, exist_ok=True)

    # Show help message if no subcommand is given
    if not getattr(args, "subcommand", False):
        return parser.print_help()

    # Map command name to run method
    subcommand = subcommands_map[args.subcommand]
    run(subcommand, args)


def run(command: BaseCommand, args: Namespace) -> Callable:
    """Entry point of a command."""
    LOGGER.debug(f"Run CLI command {command.name}")
    all_settings = [getattr(settings, s) for s in settings.__dict__]
    app_settings = list(
        filter(lambda o: isinstance(o, settings.NwaSetting), all_settings)
    )
    LOGGER.debug("Settings:")
    for setting in app_settings:
        LOGGER.debug(f'"{setting.name}": {setting.value}')

    self_cleaning_class = getattr(command, "self_cleaning", False)
    try:
        if self_cleaning_class:
            with command as com:
                return com.run(args)
        return command.run(args)
    except SystemError as error:
        LOGGER.critical(error)


def configure_parser(subcommands_map: Dict[str, BaseCommand]) -> ArgumentParser:
    """Set up argument parser along with subcommands.

    Args:
        subcommands_map: A dict mapping of instantiated command names to their
            corresponding python objects.

    Returns:
        The configured ArgumentParser object.
    """
    parser = ArgumentParser(prog="nwa", description="Command parser for nwa module")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        dest="verbosity",
        default=0,
        help="verbose output (repeat for increased verbosity)",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_const",
        const=-1,
        default=0,
        dest="verbosity",
        help="quiet output (show errors only)",
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    for name, subcommand in subcommands_map.items():
        subparser = subparsers.add_parser(name)
        subcommand.add_args(subparser)

    return parser


if __name__ == "__main__":
    main()
