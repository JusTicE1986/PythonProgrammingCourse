import os
import shutil

dir = r'C:\Users\andre\OneDrive\Desktop\Umbenennen'

filelist = os.listdir(dir)
for file in filelist:
    file_splitted = file.split(' ')
    date_in_filename = file_splitted[0]
    year = date_in_filename[-4:]
    month = date_in_filename[3:5]
    day = date_in_filename[0:2]
    file_name = ''
    for parts in file_splitted[1:]:
        file_name += parts + " "
    filename_new = f'{year}-{month}-{day} {file_name}'

    os.rename(os.path.join(dir, file), os.path.join(dir, filename_new))

