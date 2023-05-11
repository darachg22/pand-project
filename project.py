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
#Outputs a summary of each variable to a text file
with open('Results/variables_summary.txt', 'w') as f:
    print (str(iris_data), file=f)
#Send print statements to the file
    print("The number of observations for each variable for each Iris variety are: \n", file=f)
    print(iris_data.groupby("variety").count(), file=f)
    f.write("\n\n")
    print("The mean of each Iris Variety in the dataset is: \n\n", file=f)
    print(iris_data.groupby('variety').mean(), file=f)
    f.write("\n\n")
    print("The highest value for each Class in the Iris dataset is: \n\n", file=f)
    print(iris_data.groupby("variety").max(), file=f)
    f.write("\n\n")
    print("The minimum value for each Class in the Iris dataset is: \n\n", file=f)
    print(iris_data.groupby("variety").min(), file=f)
#creating histograms of variables
for col in iris_data.columns[:-1]:
    plt.hist(iris_data[col], bins=50)
    plt.title(col)
    plt.xlabel('measurement cm')
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

