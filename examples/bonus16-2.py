import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            print(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["bonus1.py", "bonus15.py"], dest_dir="/../files")