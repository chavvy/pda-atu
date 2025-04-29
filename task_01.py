#Task 01 of PDA
#Source the Data Set

from sklearn.datasets import load_iris

#loading iris dataset
iris_data = load_iris()

#functions for displaying data

def iris_keys(data):
    keys = data.keys()
    print(keys)

def iris_features(data):
    features = data['data']
    print(features)

def iris_features_shape(data):
    features_shape = data['data'].shape
    print(features_shape)

def iris_target(data):
    target = data['target']
    print(target)

def iris_shape(data):
    target_shape = data['target'].shape
    print(target_shape)

def iris_target_names(data):
    target_names = data['target_names']
    print(target_names)

def iris_features_names(data):
    features_names = data['feature_names']
    print(features_names)

#The Iris dataset contains information on different samples of iris flowers, first used by Fisher
print(iris_data)
#The data has 150 iris flowers in it, with each having 4 features, as shown by the shape
iris_features_shape(iris_data)
#The features are the sepal length and width, and the petal length and width (4 total)
iris_features_names(iris_data)
#The flowers are categorized into 3 different spieces: setosa, versicolor, virginica
iris_target_names(iris_data)