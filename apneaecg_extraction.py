import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import wfdb
import matplotlib.pyplot as plt
import os
import sys

import pathlib

data_path = './apnea-ecg/'

record = wfdb.rdrecord(data_path + 'a01') 
list_data_experiment = record.p_signal.tolist()
print (len(list_data_experiment))
with open ('output.txt','w') as _f:
    for _str in list_data_experiment:
        _f.write(str(_str).strip('[]') + '\n')

