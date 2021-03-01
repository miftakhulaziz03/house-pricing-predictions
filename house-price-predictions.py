import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df_train = pd.read_csv('datasets/train.csv')
df_test = pd.read_csv('datasets/test.csv')

df_train.head()
df_train.shape

df_test.head()
df_test.shape

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

