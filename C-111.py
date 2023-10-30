import os
import shutil
os.getcwd()
#os.mkdir("C:/Users/Guru/Desktop/Games")
from_dir="C:/Users/Guru/Desktop"
list=os.listdir(from_dir)
print(list)

path1="C-110.py"
root,extension=os.path.splitext(path1)
print("The name of the file is",root)
print("The extension of your file is",extension)

source="C:/Users/Guru/Desktop/Games/darjeeling 2.jpg"
destination="C:/Users/Guru/Desktop/Games/darjeeling1212.jpg"
dest=shutil.copy(source,destination)
print("The file is copied successfully!")
