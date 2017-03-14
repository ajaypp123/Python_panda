# read csv file
import pandas as pd

data = pd.read_csv('sample.csv')

print(data.describe())
print("********************************************")
print(data)
print("********************************************")
print(len(data))
print("********************************************")
print(data.head(2))
print("********************************************")
print(data.tail(2))

