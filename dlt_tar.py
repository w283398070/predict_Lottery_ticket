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
    return data.values.tolist()

def matching_degree(src_list, dst_list):
    src_red = src_list[:5]
    src_blue = src_list[:-2]
    dst_red = dst_list[:5]
    dst_blue = dst_list[:-2]
    src_set = set(src_red)
    dst_set = set(dst_red)
    count = len(src_set.intersection(dst_set))
    if src_blue[0] in dst_blue:
        count += 1
    if src_blue[1] in dst_blue:
        count += 1
    return count


def cacl_match(data_list):
    tar_list = [2, 24, 26, 30, 34, 6, 7]
    for sublist in data_list:
        degree = matching_degree(sublist, tar_list)
        if degree >= 3:
            print('count:' + str(degree))
            print(sublist)

print('start')
data_list = read_predict_data()
cacl_match(data_list)
print('end')
