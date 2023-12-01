import os

def read_file_to_array(filepath):
    """Reads a text file and returns its contents as an array of lines."""
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as file:
                return file.read().splitlines()
        except IOError as e:
            print(f"Error reading file: {e}")
            return []
    else:
        print(f"File {filepath} does not exist.")
        return []