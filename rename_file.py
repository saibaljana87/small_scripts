#!/usr/bin/env python3

import os
import argparse

def file_rename(directory, old_base_name, new_base_name):
    for filename in os.listdir(directory):
        old_filepath = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(old_filepath):
            continue

        # Split filename into name and extension
        name, extension = os.path.splitext(filename)

        # Check if the base name matches
        if name == old_base_name:
            new_filename = new_base_name + extension
            new_filepath = os.path.join(directory, new_filename)

            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files by replacing old base name with new base name.")
    parser.add_argument("old", help="Old base name (without extension)")
    parser.add_argument("new", help="New base name (without extension)")
    parser.add_argument("-d", "--directory", default=".", help="Target directory (default: current directory)")
    args = parser.parse_args()

    file_rename(args.directory, args.old, args.new)

