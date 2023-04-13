# -*- coding:utf-8 -*-
import os
import datetime
import pandas as pd
from config import *
from common import get_current_number

def read_predict_data(win):
    filepath = "{}{}/".format(predict_path, "dlt")
    #fileadd = "{}{}_{}{}".format(filepath, 'predict', filename, ".csv")
    fileadd = "{}{}_{}_{}{}".format(filepath, 'predict', get_current_number("dlt"), win, ".csv")
    print(fileadd)
    if not os.path.exists(fileadd):
        return [],[]
    data = pd.read_csv(fileadd)
    print(data)
    return data.values.tolist()

def matching_degree(src_list, dst_list):
    src_red = src_list[:5]
    src_blue = src_list[5:]
    dst_red = dst_list[:5]
    dst_blue = dst_list[5:]
    src_set = set(src_red)
    dst_set = set(dst_red)
    intersect = src_set.intersection(dst_set)
    #print(intersect)
    count = len(intersect)
    #print(src_blue)
    #print(dst_blue)
    if src_blue[0] in dst_blue:
        count += 1
    if src_blue[1] in dst_blue:
        count += 1
    return count


def cacl_match(data_list):
    tar_list = [4,5,18,22,30,5,12]
    for sublist in data_list:
        degree = matching_degree(sublist, tar_list)
        if degree >= 4:
            print('count:' + str(degree))
            print(sublist)

print('start')
data_list = read_predict_data(3)
cacl_match(data_list)
data_list = read_predict_data(5)
cacl_match(data_list)
data_list = read_predict_data(7)
cacl_match(data_list)
print('end')
