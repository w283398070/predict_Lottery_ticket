# -*- coding:utf-8 -*-
import os
import datetime
import pandas as pd
from config import *


def read_predict_data():
    filename = datetime.datetime.now().strftime('%Y%m%d')
    filepath = "{}{}/".format(predict_path, "dlt")
    fileadd = "{}{}{}".format(filepath, filename, ".csv")
    if not os.path.exists(fileadd):
        return []
    data = pd.read_csv(fileadd)
    print(data)
    return data.values.tolist()
def predict_total(predict_list):
    filename = datetime.datetime.now().strftime('%Y%m%d')
    filepath = "{}{}/".format(predict_path, "dlt")
    fileadd = "{}{}_{}{}".format(filepath, 'predict', filename, ".csv")
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    df = pd.DataFrame(predict_list, columns=['red1', 'red2', 'red3', 'red4', 'red5', 'blue1', 'blue2'])
    df.to_csv(fileadd, encoding="utf-8", mode='a', header=False, index=False)

def train_and_predict():
    print('train_and_predict start')
    os.system('python run_train_model.py --name dlt  --windows_size 3,5,7 --red_epochs 1 --blue_epochs 1 --batch_size 1')
    os.system('python run_predict.py  --name dlt --windows_size 3,5,7')
    print('train_and_predict end')

print('start')
count = 0
while(count < 100):
    train_and_predict()
    predict_total(read_predict_data())
    count += 1

print('end')