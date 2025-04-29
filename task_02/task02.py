#Task 02
#Explore the Data Structure

from sklearn.datasets import load_iris
import iris_data_print as idp

iris_data = load_iris()

#The data has 150 iris flowers in it, with each having 4 features, as shown by the shape
idp.iris_features_shape(iris_data)
#This showcases the first 5 rows of data, and the last 5 rows of data
idp.iris_firstrow_data(iris_data)
idp.iris_lastrow_data(iris_data)
#The features are the sepal length and width, and the petal length and width (4 total)
idp.iris_features_names(iris_data)
#The flowers are categorized into 3 different spieces: setosa, versicolor, virginica
idp.iris_target_names(iris_data)