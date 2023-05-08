# pand-project
A data analysis project looking at Fisher's Iris Dataset
Introduction: 

Fisher's Iris data set is a famous multivariate data set introduced by the British statistician and biologist Ronald Fisher in 1936. The data set consists of measurements on the length and width of sepals and petals of three species of iris flowers: Setosa, Versicolor, and Virginica.
There are 50 samples for each species, making a total of 150 samples. The measurements are in centimeters and consist of sepal length, sepal width, petal length, and petal width.
The data set is often used for statistical analysis, visualization, and machine learning algorithms, such as classification and clustering. It is also used as a benchmark data set for evaluating new methods and algorithms.
Fisher's Iris data set is considered a classic example of exploratory data analysis and is widely used in data science education and research.
References: https://www.angela1c.com/projects/iris_project/the-iris-dataset/ , 


the project:
importing the dataset: 
best way was online. The in file ones were tempermental.alternative dataframe used in iris.cv. I realised (once again) that my terminal was in the wrong location for accessing the files I need. Once this was rectified, the importing and analysing of the data improved drastically. 

exporting the variables to text file: similar to the 'Es' task. Need to give headings for the types. Headings resource found: https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/. update: once I used the csv version the files headings were created anyway. resources used to export: https://blog.finxter.com/python-convert-csv-to-text-file-csv-to-txt/. When exported the text file was shortened significantly. I learned about truncation and implemented the steps needed to prevent it. Reference used: https://nadeauinnovations.com/post/2021/05/python-tips-how-to-stop-a-pandas-data-table-from-being-truncated-when-printed/ 

creating the histogram: I have created an individual histogram for each of the columns using matplot. I need to now update the x and y axis and make this more readable i.e. put height along the side and width along the bottom for symmetry. Also I may need to consider using a loop to shorten the code. Research to follow. After re-reading the project paramenters I realised I needed to save each histogram to a png file. I achieved this by adding the 'plot.savefig' function to each histogram.

creating the scatter plot for both pairs of variables: Need to find a way to change the colors of the scatterplots. I find them difficult to read at the moment. update: using seaborn as a means to improve the visuals and ended up finding a better to undertsand and tidier code here: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/. 


Tidying up the code:
how do i send this to a created folder:
make the histrogram more readable
shorten the histogram section (using while,if loops) 
