# -*- coding:utf-8 -*-
import os
import datetime
import pandas as pd
from config import *
from common import get_current_number

def get_current_number_ex():
    data_list = read_data(0)
    return data_list[1]

def write_predict_data(predict_list, win):
    filepath = "{}{}/".format(predict_path, "dlt")
    fileadd = "{}{}_{}_{}{}".format(filepath, 'predict', get_current_number_ex(), win, "_filter.csv")
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    df = pd.DataFrame(predict_list, columns=['red1', 'red2', 'red3', 'red4', 'red5', 'blue1', 'blue2'])
    df.to_csv(fileadd, encoding="utf-8", mode='a', header=False, index=False)

def read_predict_data(win):
    filepath = "{}{}/".format(predict_path, "dlt")
    fileadd = "{}{}_{}_{}{}".format(filepath, 'predict', get_current_number_ex(), win, ".csv")
    #print(fileadd)
    if not os.path.exists(fileadd):
        return [],[]
    data = pd.read_csv(fileadd)
    #print(data)
    return data.values.tolist()

def matching_degree(src_list, dst_list):
    src_red = src_list[:5]
    src_blue = src_list[-2:]
    dst_red = dst_list[:5]
    dst_blue = dst_list[-2:]
    src_set = set(src_red)
    dst_set = set(dst_red)
    intersect = src_set.intersection(dst_set)
    count = len(intersect)
    if src_blue[0] in dst_blue:
        count += 1
    if src_blue[1] in dst_blue:
        count += 1
    return count

def read_data(index):
    filepath = "{}/{}/".format('data', "dlt")
    fileadd = "{}{}".format(filepath, data_file_name)
    #print(fileadd)
    if not os.path.exists(fileadd):
        return []
    data = pd.read_csv(fileadd)
    df = data.loc[index]
    return df.values.tolist()

def read_data_list(index):
    data_list = read_data(index)
    return data_list[-7:]

def history_match(cur_list):
    tar_list = read_data_list(0)
    his1 = read_data_list(1)
    his2 = read_data_list(2)
    his3 = read_data_list(3)
    his4 = read_data_list(4)
    cur_degree = matching_degree(cur_list, tar_list)
    his1_d = matching_degree(cur_list, his1)
    his2_d = matching_degree(cur_list, his2)
    his3_d = matching_degree(cur_list, his3)
    his4_d = matching_degree(cur_list, his4)
    isadd = (cur_degree == 0 and his1_d <= 1 and his2_d <= 1 and his3_d <= 1 and his4_d <= 1)
    '''
    if not isadd:
        print(cur_list)
        print(tar_list)
        print(his1)
        print(his2)
        print(his3)
        print(his4)
        print(his5)
        print(cur_degree)
        print(his1_d)
        print(his2_d)
        print(his3_d)
        print(his4_d)
        print(his5_d)
    '''
    return isadd

def filter_data(win):
    data_list = read_predict_data(win)
    new_list = []
    for sublist in data_list:
        if history_match(sublist):
            new_list.append(sublist)
    write_predict_data(new_list, win)

print('start')
filter_data(3)
filter_data(5)
filter_data(7)
print('end')
