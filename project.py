import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import os 
# Create a folder that keeps the output files
if not os.path.exists('Results'):
    os.makedirs('Results')
#importing the dataset
iris_data = pd.read_csv('iris.csv') 
#solves the trucance issue
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('display.width', 999)
#Outputs a summary of each variable to a single text file
content = str(iris_data)
print(content, file=open('Results/variables_summary.txt', 'w'))     
#creating histograms of variables
for col in iris_data.columns[:-1]:
    plt.hist(iris_data[col], bins=10)
    plt.title(col)
    plt.xlabel('measurement')
    plt.ylabel('frequency')
    plt.savefig(f'Results/{col}_histogram.png')
    plt.show()
#create a scatter plot for each pair of variables
#Petal Width vs Petal Length
sns.scatterplot(x='petal.length', y='petal.width',
                hue='variety', data=iris_data, )
plt.legend(bbox_to_anchor=(1, 1), loc=2) 
plt.savefig('Results/Scatterplot_petallength_petalwidth.png')
plt.show()
#Sepal Width vs Sepal Length
sns.scatterplot(x='sepal.length', y='sepal.width',
                hue='variety', data=iris_data, )
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig('Results/Scatterplot_sepallength_sepalwidth.png')
plt.show()
#Creating a Pairplot
sns.pairplot(iris_data.drop(['sepal.length'], axis = 1),
             hue='variety', height=2)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig('Results/Pairplot.png')
plt.show()
# Creating boxplot
plt.boxplot(iris_data)
plt.savefig('Results/Boxplot.png')
plt.show()