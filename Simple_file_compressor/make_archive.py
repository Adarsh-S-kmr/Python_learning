import zipfile
import pathlib

def mak(filepaths,dest):
    dest_path = pathlib.Path(dest,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname = filepath.name)


if "__main__"==__name__:
    mak(filepaths=["todo.py","comp.py"],dest = 'destination')
