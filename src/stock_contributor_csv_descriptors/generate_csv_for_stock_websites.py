"""
From a master media descriptor CSV, filled by the user, generate a specific CSV to each contributor platform.
That master file can be created by the other script, populate_file_names_to_main_csv.py
"""

from argparse import ArgumentParser
from pathlib import Path

from src.stock_contributor_csv_descriptors.common import is_dir_path, DEFAULT_MAIN_CSV, PATH_CSV_TEMPLATE, is_file_path


# Constants
PLATFORMS = ("adobe", "pond5", "shutterstock")
PLATFORMS_DEFAULT = ",".join(PLATFORMS)


def main(descriptor_path: Path, output_dir: Path, platforms: tuple[str]):
    # Load the master media descriptor

    # Load the Template and Format descriptor

    # Check the values of the Master csv from by user with the Format descriptor

    # Use the Platform Specific templates to generate each file
    for platform in platforms:
        pass
    pass


def cli():
    """ Parse the arguments """
    parser = ArgumentParser(__doc__)
    parser.add_argument("master", help="Master media descriptor file (default: %(default)s)",
                        default=Path.cwd() / DEFAULT_MAIN_CSV, type=is_file_path)
    parser.add_argument("-o", "--output", help="Base directory for the specific descriptors (default: %(default)s)",
                        default=Path.cwd(), type=is_dir_path)
    parser.add_argument("-p", "--platforms", help="Target platforms, comma separated (default: %(default)s)",
                        default=PLATFORMS_DEFAULT, type=str)
    # todo: use "choices" with multiple values for the ArgParse?

    args = parser.parse_args()
    platforms = args.platforms.split(",")

    main(Path(args.master), Path(args.output), args.platforms)


if __name__ == '__main__':
    cli()

