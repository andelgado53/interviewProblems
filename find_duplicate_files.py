import os, sys
from hashlib import md5
import os.path

def hash_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        hash_value = md5(data)
    return hash_value.hexdigest()


files = {}
duplicates = []
def find_duplicates(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            print('processing file: ' + file_path)
            exiting_file_hash = hash_file(file_path)
            if exiting_file_hash in files.keys():
                already_found_file = files[exiting_file_hash]
                if os.path.getctime(file_path) > os.path.getctime(already_found_file):
                    duplicates.append((file_path, already_found_file))
                else:
                    duplicates.append((already_found_file, file_path))
            else:
                files[exiting_file_hash] = file_path
        elif os.path.isdir(file_path):
            print('processing folder: ' +  file_path)
            find_duplicates(file_path)
    return

print(find_duplicates("/Users/andres/Documents/InterviewCake"))
print(duplicates)