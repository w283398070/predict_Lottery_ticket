# -*- coding:utf-8 -*-
import os
import datetime, shutil
import pandas as pd
from config import *
from common import get_current_number


def clean_modeling_data():
    dlt_model_path = os.path.join(model_path, 'dlt')
    if os.path.exists(dlt_model_path):
        shutil.rmtree(dlt_model_path)
    os.makedirs(dlt_model_path)
    return

def read_predict_data():
    filename = datetime.datetime.now().strftime('%Y%m%d')
    filepath = "{}{}/".format(predict_path, "dlt")
    fileadd = "{}{}{}".format(filepath, filename, ".csv")
    if not os.path.exists(fileadd):
        return []
    data = pd.read_csv(fileadd)
    print(data)
    return data.values.tolist()
def predict_total(predict_list, win):
    filepath = "{}{}/".format(predict_path, "dlt")
    fileadd = "{}{}_{}_{}{}".format(filepath, 'predict', get_current_number("dlt"), win, ".csv")
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    df = pd.DataFrame(predict_list, columns=['red1', 'red2', 'red3', 'red4', 'red5', 'blue1', 'blue2'])
    df.to_csv(fileadd, encoding="utf-8", mode='a', header=False, index=False)

def train_and_predict(train_count):
    print('train_and_predict start')
    #os.system('python run_train_model.py --name dlt  --windows_size 3,5,7 --red_epochs 666 --blue_epochs 666 --batch_size 1')
    train_cmd = "{}{}{}{}{}".format("python run_train_model.py --name dlt  --windows_size 3,5,7 --red_epochs ", train_count, " --blue_epochs ", train_count, " --batch_size 1")
    os.system(train_cmd)
    os.system('python run_predict.py  --name dlt --windows_size 3,5,7')
    print('train_and_predict end')

print('start')
count = 0
train_count = 1
while(count < 1000):
    train_and_predict(train_count)
    predict_data_list = read_predict_data()
    predict_total([predict_data_list[0]], 3)
    predict_total([predict_data_list[1]], 5)
    predict_total([predict_data_list[2]], 7)
    count += 1
    train_count += 1

print('end')