# pand-project

A data analysis project looking at Fisher's Iris Dataset

Introduction: 
Fisher's Iris data set is a famous data set introduced by the British statistician and biologist Ronald Fisher in 1936. The data set consists of measurements on the length and width of sepals and petals of three varieties of iris flowers: Setosa, Versicolor, and Virginica.
There are 50 samples for each species, making a total of 150 samples. The measurements are in centimeters and consist of sepal length, sepal width, petal length, and petal width.
The data set is often used for statistical analysis, visualization, and machine learning algorithms, such as classification and clustering. It is also used as a benchmark data set for evaluating new methods and algorithms. Fisher's Iris data set is considered a classic example of exploratory data analysis and is widely used in data science education and research.

This Code:
When this code is ran, it will first create a folder titled 'Results' containing information surrounding the Iris Dataset. Within this folder there will be 8 files (seven .png files and one .txt file). These files contain analysis of the dataset. The dataset, explained in the introudction, is the Iris dataset, which contains measurements of four features (sepal length, sepal width, petal length, and petal width) for three different species of Iris flowers (setosa, versicolor, and virginica). The dataset is loaded from a CSV file named `iris.csv`.

To Run:
Run the script using a Python interpreter (e.g., `python iris_analysis.py`).

The Files:
The generated results can be found in the `Results` folder after running the script. The folder will contain the following files:
- `variables_summary.txt`: A summary of each variable in the dataset.
- `colname_histogram.png`: Histograms for each variable, where `colname` corresponds to the column name in the dataset.
- `Scatterplot_petallength_petalwidth.png`: Scatter plot of petal length versus petal width.
- `Scatterplot_sepallength_sepalwidth.png`: Scatter plot of sepal length versus sepal width.
- `Pairplot.png`: Pair plot showing the relationships between different variables.

For a step by step of count of my creating this script, please see pand-project.ipynb jupyter notebook file within this repository. 