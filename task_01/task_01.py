#Task 01 of PDA
#Source the Data Set

from sklearn.datasets import load_iris

#loading iris dataset
iris_data = load_iris()

#The Iris dataset contains information on different samples of iris flowers, first used by Fisher
print(iris_data)