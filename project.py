import pandas as pd
import matplotlib.pyplot as plt
#importing the dataset
Variables =pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
#Outputs a summary of each variable to a single text file
with open('variables_summary.txt', 'w') as f:
    f.write(Variables.describe().to_string()) 