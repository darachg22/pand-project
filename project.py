import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#importing the dataset
iris_data = pd.read_csv('iris.csv') 
#data=iris_data.describe
#print (data)
#solves the trucance issue
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('display.width', 999)
#Outputs a summary of each variable to a single text file
content = str(iris_data)
print(content, file=open('variables_summary.txt', 'w'))     
#creating histograms of variables
for col in iris_data.columns[:-1]:
    plt.hist(iris_data[col], bins=10)
    plt.title(col)
    plt.xlabel('measurement')
    plt.ylabel('frequency')
    plt.savefig(f'{col}_histogram.png')
    plt.show()

#create a scatter plot for each pair of variables
#Petal Width vs Petal Length
sns.scatterplot(x='petal.length', y='petal.width',
                hue='variety', data=iris_data, )
plt.legend(bbox_to_anchor=(1, 1), loc=2) 
plt.savefig('Scatterplot_petallength_petalwidth.png')
plt.show()

#Sepal Width vs Sepal Length
sns.scatterplot(x='sepal.length', y='sepal.width',
                hue='variety', data=iris_data, )
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig('Scatterplot_sepallength_sepalwidth.png')
plt.show()