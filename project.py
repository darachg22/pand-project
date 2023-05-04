import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
iris_data = pd.read_csv('iris.csv') 
#solves the trucance issue
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('display.width', 999)
#Outputs a summary of each variable to a single text file
content = str(iris_data)
print(content, file=open('variables_summary.txt', 'w'))     
#creating histograms of variables
#Sepal Length Histogram
plt.hist(iris_data['sepal.length'], bins=15)
plt.title('Sepal Length')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()
#Sepal Width
plt.hist(iris_data['sepal.width'], bins=10)
plt.title('Sepal Width')
plt.xlabel('Width')
plt.ylabel('Frequency')
plt.show()
#Petal Lenght
plt.hist(iris_data['petal.length'], bins=10)
plt.title('Petal Length')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.show()
#Petal Width
plt.hist(iris_data['petal.width'], bins=10)
plt.title('Petal Width')
plt.xlabel('Width')
plt.ylabel('Frequency')
plt.show()

#create a scatter plot for each pair of variables
#Sepal Width vs Sepal Length
plt.scatter(iris_data['sepal.length'], iris_data['sepal.width'])
plt.title('Sepal Width vs Sepal Length')
plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.show()
#Petal Width vs Petal Length
plt.scatter(iris_data['petal.length'], iris_data['petal.width'])
plt.title('Petal Width vs Petal Length')
plt.xlabel('Petal.length')
plt.ylabel('Petal.width')
plt.show()