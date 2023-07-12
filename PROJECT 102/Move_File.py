import os
import shutil

from_dir = "D:/Downloads1"
to_dir = "D:/Document Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)


for i in list_of_files:
    name, extension = os.path.splitext(i)
    if extension == '':
        continue
    path1 = from_dir + '/'+ i

    path2 = to_dir 

    path3 = to_dir + '/' + i

    if os.path.exists(path2):
        print("Moving " + i + "...")

        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        print("Moving " + i + "...")
        shutil.move(path1, path3)



        