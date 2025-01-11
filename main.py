import os
import sys
from pathlib import Path

from PIL import Image


def convert_to_png(input_file, output_image_file_name) -> None:
    print("Converting",input_file)
    try:
        with Image.open(input_file) as input_image:
            input_image.save(output_image_file_name, "PNG")
    except FileNotFoundError as err:
        print("File not found\n\n")
        print(f"{err}")
    else:
        print("\tFile converted successfully\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <input_dir>")
        sys.exit(1)

    input_dir = Path(sys.argv[1]).resolve()

    if not input_dir.is_dir():
        print("Input directory isn't a directory\n\n")
        sys.exit(1)

    output_dir_name = input_dir.name + "-png"
    output_dir = input_dir / output_dir_name
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_entry in os.scandir(input_dir):
        if file_entry.is_file() and not file_entry.name.lower().endswith(".png"):
            # input_image_file = file_entry.path
            input_image_file = Path(file_entry.path).resolve()
            modified_input_image_file = input_image_file.stem + ".png"
            output_image_file_name = output_dir / modified_input_image_file
            convert_to_png(input_image_file, output_image_file_name)

            # input_image_file = file_entry.path
            # output_image_file = output_dir / file_entry.name
            # convert_to_png(input_image_file, output_image_file)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print("An error occurred\n\n")
        print(err)
        sys.exit(1)
    else:
        sys.exit(0)