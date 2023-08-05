import os
from pathlib import Path
from sys import argv

from .norm_func import normalize
from .archive_func import arch
from .file_replace import f_replace
from .list_app import feed_list
from .fold_remov import remove
from .fold_remov import ignored_folders
from . import list_app


#MAIN FUNCTION
def file_manager(path):
    os.chdir(path) #definig working location

    remove(path) # remove empty folders
    normalize(path)
    feed_list(path) # appending lists of files and formats
    arch(path) #unpacking archives to the folder "archives"
    f_replace(path)  #moving files to respective folders
    
    
    for file in os.listdir(): #recursive iteration in subfolders
            if file in ignored_folders: #ignorign certain folders
                continue
            if os.path.isdir(file):  # Check if the current item is a subfolder
                file_manager(os.path.join(path, file)) 

def main():
    path = Path(argv[1])
    file_manager(path)
    print(f'{"known formats: "}{list_app.known_formats_found}')
    print(f'{"unknown formats: "}{list_app.unknown_formats_found}')
    print(f'{"documents files: "}{list_app.documents}')
    print(f'{"audio files: "}{list_app.audio}')
    print(f'{"archives files: "}{list_app.archives}')
    print(f'{"video files: "}{list_app.video}')
    print(f'{"images files: "}{list_app.images}')
    print(f'{"unknown files: "}{list_app.others}')

if __name__ == "__main__":
    main()
          