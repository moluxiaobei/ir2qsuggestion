import lambda_mart as lm
import pandas as pd
import os
from datetime import datetime

experiment = 'next_query'
file_name = '../data/lamdamart_data_next_query.csv'
file_name_val = '../data/lamdamart_data_next_query_val.csv'
file_name_test = '../data/lamdamart_data_next_query_test.csv'

time = datetime.now().strftime('%d-%m %H:%M:%S')
print("[%s: Loading sessions feature file...]" % time)
if os.path.isfile(file_name) and os.path.isfile(file_name_val) and os.path.isfile(file_name_test):
    df = pd.read_csv(file_name)
    df_val = pd.read_csv(file_name_val)
    df_test = pd.read_csv(file_name_test)
else:
    print('Could not find ' + file_name)
time = datetime.now().strftime('%d-%m %H:%M:%S')
print("[%s: Loaded train features...]" % time)

# Uncomment to cast the labels to 0 and 1 and save this in the csv

df = df.drop('Unnamed: 0', 1)
df_val = df_val.drop('Unnamed: 0', 1)
df_test = df_test.drop('Unnamed: 0', 1)

print("casting -1 to 0 and 1 to 1, df")
df["target"] = df["target"].map({'-1.0': 0.0, '1.0': 1.0})
print("casting -1 to 0 and 1 to 1, df_val")
df_val["target"] = df_val["target"].map({'-1.0': 0.0, '1.0': 1.0})
print("casting -1 to 0 and 1 to 1, df_test")
df_test["target"] = df_test["target"].map({'-1.0': 0.0, '1.0': 1.0})

df.to_csv(file_name)
print("saved df")
df_val.to_csv(file_name_val)
print("saved df_val")
df_test.to_csv(file_name_test)
print("saved df_test")

df = df.drop('Unnamed: 0', 1)
df_val = df_val.drop('Unnamed: 0', 1)
df_test = df_test.drop('Unnamed: 0', 1)
lambdamart_data = df.get_values()
lambdamart_data_val = df_val.get_values()
lambdamart_data_test = df_test.get_values()
time = datetime.now().strftime('%d-%m %H:%M:%S')
print("[%s: Training LambdaMART with HRED features]" % time)
lm.lambdaMart(lambdamart_data, lambdamart_data_val, lambdamart_data_test, experiment + '_HRED')

df = df.drop('HRED', 1)
df_val = df_val.drop('HRED', 1)
df_test = df_test.drop('HRED', 1)
lambdamart_data = df.get_values()
lambdamart_data_val = df_val.get_values()
lambdamart_data_test = df_test.get_values()
time = datetime.now().strftime('%d-%m %H:%M:%S')
print("[%s: Training LambdaMART without HRED features]" % time)
lm.lambdaMart(lambdamart_data, lambdamart_data_val, lambdamart_data_test, experiment)