import os
from pathlib import Path
from distutils.dir_util import copy_tree
from termcolor import colored


BASE_DIR = Path(__file__).resolve().parent
# Add your destination path here
DIST_DIR = BASE_DIR / ""  


def copy_dir_content(source_dir: str, dist_dir: Path):
    """copy all the directory tree to the destination directory.

    Args:
        directory (Path): source directory
    """
    copy_tree(source_dir, str(dist_dir))


def main():
    # Get current directory content
    dir_content = os.listdir(BASE_DIR)
    for file in dir_content:
        if os.path.isdir(file) and file != DIST_DIR:
            copy_dir_content(file, DIST_DIR)
            print(colored(file, "yellow"),
                  colored(f"Directory content is copied successfully to [{DIST_DIR}]", "green")
                 )


if __name__ == "__main__":
    main()
