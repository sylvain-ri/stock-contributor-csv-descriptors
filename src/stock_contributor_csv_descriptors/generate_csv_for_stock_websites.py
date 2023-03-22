"""
From a media descriptor CSV, filled by the user, generate a CSV specific to each contributor platform.
That media descriptor can be created by the other script, populate_file_names_to_main_csv.py
"""

from argparse import ArgumentParser
from pathlib import Path

from src.stock_contributor_csv_descriptors.common import is_dir_path, DEFAULT_MAIN_CSV, PATH_CSV_TEMPLATE, is_file_path


def main(descriptor_path: Path, output_dir: Path):
    pass


def cli():
    """ Parse the arguments """
    parser = ArgumentParser(__doc__)
    parser.add_argument("descriptor", help="General media descriptor file (default: %(default)s)",
                        default=Path.cwd() / DEFAULT_MAIN_CSV, type=is_file_path)
    parser.add_argument("-o", "--output", help="Base directory for the specific descriptors (default: %(default)s)",
                        default=Path.cwd(), type=is_dir_path)

    args = parser.parse_args()
    main(Path(args.descriptor), Path(args.output))


if __name__ == '__main__':
    cli()