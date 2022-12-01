""" Scan a folder for image/video files, and create a CSV file with
    the filenames and the column headers
"""
import csv
import sys
from argparse import ArgumentParser
from datetime import datetime as dt
from pathlib import Path
import filetype

DEFAULT_MAIN_CSV = f"{dt.now():%Y-%m-%d_%H-%M}_descriptor.csv"
CSV_TEMPLATE = "template.csv"


def main(folder: Path, path_output: Path):
    """ Scan a folder and add filenames to a CSV with column headers """
    # Fetch the template CSV
    path_csv_template = Path(sys.path[0]) / CSV_TEMPLATE

    # Check paths
    assert path_csv_template.is_file(), FileNotFoundError(f"Couldn't find the CSV template at {path_csv_template}")
    assert folder.is_dir(), NotADirectoryError(f"Input folder doesn't exist or is not a directory: {folder}")
    path_output.parent.mkdir(exist_ok=True)

    # Fetch the file names
    media_files = (file for file in folder.iterdir()
                   if file.is_file() and (filetype.is_image(file) or filetype.is_video(file)))

    # Create the CSV
    n = 0
    with open(path_csv_template, "r") as csv_template, open(path_output, "w") as out_csv:
        template_reader = csv.reader(csv_template)
        output_writer = csv.writer(out_csv)

        # Write the default column headers
        output_writer.writerow(next(template_reader))

        # Write filename in each line
        for filename in media_files:
            output_writer.writerow(str(filename))
            n += 1

    print(f"Done. File with {n} filenames written at: {path_output}")


def is_dir_path(path: str) -> str:
    """ check that a path is a valid directory """
    if Path.is_dir(Path(path)):
        return path
    else:
        raise NotADirectoryError(path)


if __name__ == '__main__':
    parser = ArgumentParser(__doc__)
    parser.add_argument("-f", "--folder", help="Folder to scan for images/videos",
                        default=Path.cwd(), type=is_dir_path)
    parser.add_argument("-o", "--output", help="Output path for the CSV file",
                        default=Path.cwd() / DEFAULT_MAIN_CSV, type=str)

    args = parser.parse_args()
    main(Path(args.folder), Path(args.output))
