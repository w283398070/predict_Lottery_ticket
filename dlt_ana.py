# -*- coding:utf-8 -*-
import os
import datetime
import pandas as pd
from config import *

def read_predict_data():
    filename = datetime.datetime.now().strftime('%Y%m%d')
    filepath = "{}{}/".format(predict_path, "dlt")
    fileadd = "{}{}_{}{}".format(filepath, 'predict', filename, ".csv")
    if not os.path.exists(fileadd):
        return [],[]
    data = pd.read_csv(fileadd)
    print(data)
    return data.iloc[:, :5].values.tolist(), data.iloc[:, -2:].values.tolist()

def cacl_probability(data_list):
    # Iterate through each element in the list and update the count in the dictionary
    count_dict = {}
    for sublist in data_list:
        for num in sublist:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

    # Sort the dictionary by value in descending order
    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))

    # Print out the result
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

def count_and_print_probabilities(lst):
    counts = {}
    total_count = 0
    for row in lst:
        for num in row:
            counts[num] = counts.get(num, 0) + 1
            total_count += 1
    #sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    #for num, count in sorted_dict.items():
    for num, count in sorted(counts.items()):
        probability = count / total_count
        print(f"{num:02}: {probability:.2%}")

print('start')
red_list, blue_list = read_predict_data()
#print(red_list)
#print(blue_list)
print("red:")
count_and_print_probabilities(red_list)
print("blue:")
count_and_print_probabilities(blue_list)
print('end')
