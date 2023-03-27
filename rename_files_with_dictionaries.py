import os

folder_path = '/path/to/folder'  # path to the folder to be processed
folder_path = 'testPath'  # TEST path to the folder to be processed

file_dict = {'old_phrase_1': 'new_phrase_1', 'old_phrase_2': 'new_phrase_2'}  # dictionary of phrases to be changed
file_dict = {'alpha': 'charlie', 'apple': 'banana'}

for filename in os.listdir(folder_path):  # loop through each file in the folder
    for old_phrase, new_phrase in file_dict.items():  # loop through each key-value pair in the dictionary
        if old_phrase in filename:  # check if the old phrase exists in the file name
            new_filename = filename.replace(old_phrase,
                                            new_phrase)  # replace the old phrase with the new phrase in the file name
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))  # rename the file
            break  # break out of the loop to avoid renaming the file multiple times
print('\n>>> End')
