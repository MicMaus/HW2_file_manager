from pathlib import Path
import shutil

def arch(path):
    path = Path(path)
    for file in path.iterdir():  #ARCHIVES
        if file.is_file(): #check if "file" is file, to ignore folders and reduce load
            file_format = file.suffix.lower()
            if file_format in (".zip", ".gz", ".tar", ".rar"):
                unpack_dir = Path(path, "archives", file.stem)
                shutil.unpack_archive(file, unpack_dir)
