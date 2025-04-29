#Task 01 of PDA
#Source the Data Set

from sklearn.datasets import load_iris
import iris_data_print as idp

#loading iris dataset
iris_data = load_iris()

#The Iris dataset contains information on different samples of iris flowers, first used by Fisher
print(iris_data)
#The data has 150 iris flowers in it, with each having 4 features, as shown by the shape
idp.iris_features_shape(iris_data)
#The features are the sepal length and width, and the petal length and width (4 total)
idp.iris_features_names(iris_data)
#The flowers are categorized into 3 different spieces: setosa, versicolor, virginica
idp.iris_target_names(iris_data)