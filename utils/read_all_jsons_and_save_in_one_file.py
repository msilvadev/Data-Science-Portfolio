import os, json
import glob

print(os.getcwd())
filepath = os.getcwd() + '/utils/song_data'

file_path_list = []
for root, dirs, files in os.walk(filepath):
    file_path_list = glob.glob(os.path.join(root,'*'))

dict = []
for i in file_path_list:
    with open(i, 'r') as f:
        dict.append(json.load(f))
        # json.dump(data, f)


with open('utils/song_data.json', 'a+') as f:
    for line in dict:
        json.dump(line, f)
        f.write('\n')