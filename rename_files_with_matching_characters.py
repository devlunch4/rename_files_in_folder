import os

folder_path = '/path/to/folder'  # path to the folder to be processed
folder_path = 'testPath'  # TEST path to the folder to be processed
for filename in os.listdir(folder_path):  # Get a list of files in a folder
    old_str = 'a'
    new_str = 'b'
    if old_str in filename:  # check if the file name contains the letter 'a'
        new_filename = filename.replace(old_str, new_str)  # replace the letter 'a' with 'b' in the file name
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))  # rename the file
print('\n>>> End')
