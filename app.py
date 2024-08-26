import os
import datetime

print('Hello, Alice!')

current_time = datetime.datetime.now()

print("Current time: ", current_time)

dir_path = r'/home/ivanays/Изображения/Снимки экрана'

count = 0

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

print('Total number of files: ', count)

print('Top 10 lagests files (in KB): ')

list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_path, x)),
                        os.listdir(dir_path) )

list_of_files = sorted( list_of_files,
                        key =  lambda x: os.stat(os.path.join(dir_path, x)).st_size)

list_of_files = list(reversed(list_of_files))
count1 = 0

for file_name in list_of_files:
    if count1 < 10:
        file_path = os.path.join(dir_path, file_name)
        file_size  = os.stat(file_path).st_size
        file_size_kb = file_size / 1024
        print(f"{file_path}: {file_size_kb: .2f} KB")
    count1 += 1










          