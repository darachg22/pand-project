import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
iris_data = pd.read_csv('iris.csv') 
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('display.width', 999)
#Outputs a summary of each variable to a single text file
content = str(iris_data)
print(content, file=open('variables_summary.txt', 'w'))     



#with open('variables_summary.txt', 'w') as f:
 #   f.write(iris_data.describe().to_string()) 