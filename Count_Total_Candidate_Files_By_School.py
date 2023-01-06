# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import os
import numpy as np
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
candidates_per_school = []
for school_folder in school_paths:
    school_name = school_folder.split('\\')[-1]
    candidate_folders, num_cand = get_candidate_folders(school_folder)
    #print("cand_fold", candidate_folders)
    candidate_file_count = get_candidate_file_count(candidate_folders)
    candidate_file_count = pd.DataFrame.from_dict(candidate_file_count)
    #print(candidate_file_count)
    school_val[school_name] = [candidate_file_count]
    candidates_per_school.append(num_cand)
#print(school_val['Tufts'])

print('Average file_count per candidate by school')
school_avg = []
sch_name = []
for item in school_val.items():
    length = len(item[1][0].columns)
    if length == 0:
        val = 0
    else:
        val = (sum(item[1][0].sum())) / (len(item[1][0].columns))
    #print(item[0],"Average # of files:", val)
    school_avg.append(val)
    sch_name.append(item[0])

data = pd.DataFrame(
    {'School Name': sch_name,
     'Average FIles Per Candidate': school_avg,
     'Number of Candidates': candidates_per_school
    })

print(data)
data.to_csv("Avg Files.csv", index=False)
