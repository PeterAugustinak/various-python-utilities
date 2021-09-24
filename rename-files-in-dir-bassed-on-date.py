import os
import os.path
import time

def rename_files_in_dir_based_on_date(path_to_dir, names):

    my_dir = os.chdir(path_to_dir)
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

            os.rename(file, new_file_name)

    # show result
    for file in os.listdir():
        print(file)


path_to_dir = 'D:/video/sntdo/source/'
names = {'Sep 26': 'garaz-', 'Sep 5': 'na-kupko-', 'Sep 19': 'hrat-fotbal-', 'Aug 23': 'do-dazda-', 'Sep 18': 'do-prace-'}
rename_files_in_dir_based_on_date(path_to_dir, names)