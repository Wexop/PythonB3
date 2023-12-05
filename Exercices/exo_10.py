import glob
import os
import time

files = glob.glob('*.jpeg')

for i in range(len(files)):
    file = files[i]
    os.rename(file, file.replace('jpeg', 'jpg'))

print('DONE')

time.sleep(10)

print('RENAME IN 10 SEC')

files = glob.glob('*.jpg')

for i in range(len(files)):
    file = files[i]
    os.rename(file, file.replace('jpg', 'jpeg'))
