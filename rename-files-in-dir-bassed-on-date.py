import os
import os.path
import time


my_dir = 'D:/video/sntdo/source/'
# print(os.getcwd())
new_dir = os.chdir(my_dir)


names = {'Sep 26': 'garaz-', 'Sep 5': 'na-kupko-', 'Sep 19': 'do-karanteny-', 'Aug 23': 'do-dazda-', 'Sep 18': 'do-prace-'}

# lst = [' '.join(time.ctime(os.path.getmtime(name)).split()[1:3]) for name in os.listdir('.') if os.path.isfile(name)]
# print(set(lst))

files = os.listdir(new_dir)

for index, file in enumerate(files):
    file_date = ' '.join(time.ctime(os.path.getmtime(file)).split()[1:3])
    try:
        if file_date != current_file_date:
            index = 1
    except NameError:
            pass

    current_file_date = file_date
    
    if file_date in names.keys():
        print(''.join([f'{names[file_date]}{index}', '.mp4']))


        # os.rename(os.path.join(my_dir, file), os.path.join(my_dir, ''.join([f'{names[file_date]}{index}', '.mp4'])))

