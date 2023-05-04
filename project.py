import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

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
plt.hist(iris_data['sepal.length'], bins=7)
plt.title('Sepal Length')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.savefig('sepal_length_histogram.png')
plt.show()
#Sepal Width
plt.hist(iris_data['sepal.width'], bins=5)
plt.title('Sepal Width')
plt.xlabel('Width')
plt.ylabel('Frequency')
plt.savefig('sepal_width_histogram.png')
plt.show()
#Petal Lenght
plt.hist(iris_data['petal.length'], bins=6)
plt.title('Petal Length')
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.savefig('petal_length_histogram.png')
plt.show()
#Petal Width
plt.hist(iris_data['petal.width'], bins=6)
plt.title('Petal Width')
plt.xlabel('Width')
plt.ylabel('Frequency')
plt.savefig('petal_width_histogram.png')
plt.show()

#create a scatter plot for each pair of variables
#Petal Width vs Petal Length
sns.scatterplot(x='petal.length', y='petal.width',
                hue='variety', data=iris_data, )
plt.legend(bbox_to_anchor=(1, 1), loc=2) 
plt.show()

#Sepal Width vs Sepal Length
sns.scatterplot(x='sepal.length', y='sepal.width',
                hue='variety', data=iris_data, )
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()