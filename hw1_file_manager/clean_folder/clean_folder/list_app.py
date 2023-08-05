from pathlib import Path

#lists of files to be fed 
images = []
video = []
documents = []
audio = []
archives = []
others = []
dic = {'.jpeg': images, '.png': images, '.jpg': images, '.svg': images, '.avi': video, '.mp4': video, '.mov': video, '.mkv': video, '.doc': documents, '.docx': documents, '.txt': documents, '.pdf': documents, '.xlsx': documents, '.pptx': documents, '.xls': documents, '.mp3': audio, '.ogg': audio, '.wav': audio, '.amr': audio, '.zip': archives, '.gz': archives, '.tar': archives}

known_formats_found = set()
unknown_formats_found = set()

def feed_list(path):
    path = Path(path)
    for file in path.iterdir():
        if file.is_file():
            if file.suffix.lower() in dic: #if ext in dic
                known_formats_found.add(file.suffix.lower()) #add ext to set of exten
                (dic[(file.suffix.lower())]).append(file.name)  #add file name to respective list
            else:
                unknown_formats_found.add(file.suffix.lower()) #add ext to set of exten
                (others).append(file.name)  #add file name to respective list