# import  modules and variables
from encodings.base64_codec import base64_decode
from pathlib import Path
import shutil

# base  directory
base_dir = Path("/home/amirmiri/Desktop")
target_dir = base_dir / "sorted"

# declare categories and extensions
FILE_CATEGORIES = {
    "images": [".jpj", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp" ],
    "documents":[".pdf" ,".doc" ,".dox" , ".txt",".xls" ,".xlsx" ,".ppt" ,".pptx"],
    "videos": [ ".mp4" ,".mkv" ,".avi" ,".mov" ,".wmv" ],
    "audio": [ ".mp3",  ".wav", ".aac" , ".flac" , ".ogg"],
    "archives": [ ".zip",  ".rar" , ".tar" , ".gz", ".7z"]
}

# create directories based on the categories
def create_categories_directories():
    for category , _ in FILE_CATEGORIES.items():
        (target_dir / category).mkdir(exist_ok=True , parents=True)