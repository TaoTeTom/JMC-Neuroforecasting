# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import os
from Basic_Functions import count_file



dataframe1 = pd.read_csv(r"C:\Users\15the\OneDrive - California Institute of Technology\Selenium_JMC\Schools_List.csv")


school_list = dataframe1['School']
base_path = r"C:\Users\15the\OneDrive - California Institute of Technology\Selenium_JMC"

def iterate_over_files(list):
    school_paths = []
    for school in list:
        #print(school)
        school_path = base_path + '\\' + school
        school_paths.append(school_path)
    return school_paths

school_paths = iterate_over_files(school_list)
#print(type(school_paths), school_paths)

#print(os.listdir(school_paths[1]))

def get_candidate_folders(school_dir):
    #print("school")
    #print(school_dir)
    candidate_list = []
    school_candidate_count = 0
    #gets all candidate folders
    for file in os.listdir(school_dir):
        item = os.path.join(school_dir, file)
        if os.path.isdir(item): #checks if candidate is a folder vs the csv
            school_candidate_count+=1
            candidate_list.append(item)
    #print(candidate_list, school_candidate_count)
    return candidate_list, school_candidate_count

def count_documents(folder):
    count = 0
    # Iterate directory
    for file in os.scandir(folder):
        if os.path.isdir(file):  # checks if file is a folder vs the doc
            count += count_documents(file)
        else:
            count += 1
    return count

def get_candidate_file_count(candidate_folders):
    candidate_file_count = {}
    for candidate_folder in candidate_folders:
        #print(type(candidate_folders))
        name = candidate_folder.split('\\')[-1]
        #print("name", name)
        file_count = count_documents(candidate_folder)
        candidate_file_count[name] = [file_count]
    return candidate_file_count

school_val = {}
for school_folder in school_paths:
    school_name = school_folder.split('\\')[-1]
    candidate_folders, num_cand = get_candidate_folders(school_folder)
    #print("cand_fold", candidate_folders)
    candidate_file_count = get_candidate_file_count(candidate_folders)
    #print(candidate_file_count)
    school_val[school_name] = [candidate_file_count]
print(school_val['Tufts'])


# candidate, school_count = get_candidate_folders(school_paths[0])
# print("candidate", candidate[0], "school_count", school_count)
#
# doc_count = count_documents(candidate[1])
# print(doc_count)



#
# path = r"C:\Users\15the\OneDrive - California Institute of Technology\Selenium_JMC\Alabama\Li Zhang"
#
# file_count = count_file(path)
# print(file_count)