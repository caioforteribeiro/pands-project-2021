#Program that reads Fisher's Iris data set,
#outputs the summary of each variable to a txt file,
#saves a histogram of each variable as png images,
#and outputs a scatter plot of each pair  of variables.
#Author: Caio Forte Ribeiro

#Import pandas
import pandas as pd

col_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

#Reads dataset as csv with Species as index column
iris = pd.read_csv("iris.data", header = None, names = col_names)

#Takes each species to be described
setosa = iris[iris["Species"] == "Iris-setosa"]
versicolor = iris[iris["Species"] == "Iris-versicolor"]
virginica = iris[iris["Species"] == "Iris-virginica"]

#Convert array to str so we can use write mode
sumSet = str(setosa.describe())
sumVers = str(versicolor.describe())
sumVirg = str(virginica.describe())

summary = "Iris setosa\n"+ sumSet + "\n\n" + "Iris versicolor\n" + sumVers + "\n\n" + "Iris virginica\n" + sumVirg

with open("summary.txt", "w") as f:
        f.write(summary)



