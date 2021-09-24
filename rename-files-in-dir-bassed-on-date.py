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

index = 0
current_file_date = ''

for file in files:
    file_date = ' '.join(time.ctime(os.path.getmtime(file)).split()[1:3])
    if file_date in names.keys():
        if file_date != current_file_date:
            index = 0

        index = int(index) + 1
        index = f'0{index}' if index < 10 else index
        current_file_date = file_date
        new_file_name = f'{names[file_date]}{index}.mp4'

        os.rename(os.path.join(my_dir, file), os.path.join(my_dir, new_file_name))

print(os.listdir())

