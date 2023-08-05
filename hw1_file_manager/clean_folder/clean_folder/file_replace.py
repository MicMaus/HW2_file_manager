import os
from pathlib import Path
import shutil

dic = {'.jpeg': 'images', '.png': 'images', '.jpg': 'images', '.svg': 'images', '.avi': 'video', '.mp4': 'video', '.mov': 'video', '.mkv': 'video', '.doc': 'documents', '.docx': 'documents', '.txt': 'documents', '.pdf': 'documents', '.xlsx': 'documents', '.pptx': 'documents', '.xls': 'documents', '.mp3': 'audio', '.ogg': 'audio', '.wav': 'audio', '.amr': 'audio', '.zip': 'archives', '.gz': 'archives', '.tar': 'archives'}

def f_replace(path):
    for file in os.scandir(path):  #path.iterdir()
        if file.is_dir(): #ignoring folders
            continue
        file_path = Path(file)
        file_format = file_path.suffix.lower()
        if file_format in dic:
            directory_path = Path(dic[file_format])
            directory_path.mkdir(exist_ok=True)
            shutil.move(file_path, f'{path}/{directory_path}')
            
