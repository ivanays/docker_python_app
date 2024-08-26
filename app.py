import os
#
print('Hello, Alice!')
#
dir_path = r'/home/ivanays/Изображения/Снимки экрана'

count = 0

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

print('Total number of files: ', count)

print('Top 10 lagests files (in KB): ')
count1 = 0
for path in os.scandir(dir_path):
    if count1 <= 10:
        if path.is_file():
            file_info = os.stat(path)
            file_size_kb = file_info.st_size / 1024
            print(f"{path}: {file_size_kb: .2f} KB")
    count1 += 1










          