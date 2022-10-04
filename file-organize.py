import os, pathlib, shutil

SUBDIR = {
    "Documents" : [".pdf" , ".doc", ".text", ".txt", ".docx"],
    "Images" : [".jpg", ".jpeg", ".png"],
    "Audio" : [".mp3", ".flac"],
    "Video" : ["mp4", ".mkv", ".avi"] 
}

def selectDir(value):
    for category, suffixes in SUBDIR.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "Misc"

def organizeDir():
    obj = os.scandir()
    for item in obj:
        if not os.path.isfile(item):
            continue
            
        filePath = pathlib.Path(item)
        fileType = filePath.suffix.lower()
        directory = selectDir(fileType)
        
        if not os.path.exists(directory):
            os.mkdir(directory)

        directoryPath = pathlib.Path(directory)
        shutil.move(filePath, directory)

    obj.close()

    
if __name__ == "__main__":
    organizeDir()
