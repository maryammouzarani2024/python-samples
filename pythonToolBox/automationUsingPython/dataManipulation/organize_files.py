#This code orginizes the files in a directory according to their types into separate directories


import os 
from pathlib import Path

subdirectories={
    "Documents":['.pdf', ',rtf', '.txt'],
    "Audios":['.m4a','.m4b', '.mp3'],
    "Videos":['.mov', '.avi', '.mp4'],
    "Images":['.jpg', '.jpeg', '.png']

}


def find_directory(value):
    for category, suffixes in subdirectories.items():
        if value in suffixes:
            return category
        return "Misc"
    

def orginize_files():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath=Path(item)
        fileType=filePath.suffix.lower()
        directory=find_directory(fileType)
        directoryPath=Path(directory)
        if directoryPath.is_dir()!=True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


orginize_files()