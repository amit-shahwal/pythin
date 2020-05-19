import os
import sys
import pandas
import time



while True:
    if os.path.exists('original.csv'):
        data =pandas.read_csv('original.csv')
        # print(data.mean()['st1'])
        print(data)
        print(data.sum())
        break
    else:
        print('not exist')
    time.sleep(5)    