import os
import os.path
import time


path_to_dir = 'D:/video/sntdo/source/'
my_dir = os.chdir(path_to_dir)

names = {'Sep 26': 'garaz-', 'Sep 5': 'na-kupko-', 'Sep 19': 'do-karanteny-', 'Aug 23': 'do-dazda-', 'Sep 18': 'do-prace-'}
files = os.listdir(my_dir)

index = 0
current_file_date = ''

for file in files:
    file_date = ' '.join(time.ctime(os.path.getmtime(file)).split()[1:3])
    if file_date in names.keys():
        # if there is different date on a file as previous one, the renaming name must be different, so also index count is reseted
        if file_date != current_file_date:
            index = 0

        index = int(index) + 1
        index = f'0{index}' if index < 10 else index
        
        current_file_date = file_date
        new_file_name = f'{names[file_date]}{index}.mp4'

        print(new_file_name)
        #os.rename(os.path.join(my_dir, file), os.path.join(my_dir, new_file_name))

#print(os.listdir())

