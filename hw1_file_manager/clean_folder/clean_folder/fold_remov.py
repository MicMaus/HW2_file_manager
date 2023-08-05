import os
ignored_folders = ['archives', 'video', 'audio', 'documents', 'images']
def remove(path):
    os.chdir(path) #definig working location
    for file in os.listdir():
            if file in ignored_folders: #ignorign certain folders
                continue
            if file in os.listdir():  #DELETING EMPTY FOLDER
                full_path = os.path.join(os.getcwd(), file) #creating full path to the file
                if os.path.isdir(full_path): #check it is folder, not file
                    if not os.listdir(full_path): #if list of files is empty
                        os.rmdir(full_path)  #delete folder
