#Program that reads Fisher's Iris data set,
#outputs the summary of each variable to a txt file,
#saves a histogram of each variable as png images,
#and outputs a scatter plot of each pair  of variables.
#Author: Caio Forte Ribeiro

#Import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#seaborn as default style
sns.set()

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


summary = "\t\t\tIris setosa\n"+ sumSet + "\n\n" + \
        "\t\t\tIris versicolor\n" + sumVers + "\n\n" + \
        "\t\t\tIris virginica\n" + sumVirg

#species distribution
#sees if species count is balanced or unbalanced
sampleSize = str(iris.groupby("Species").size())

#write summary of each variable to txt
#included species distribution at the end 
with open("summary.txt", "w") as f:
        f.write(summary + "\n\n\t\t\tSample Distribution\n" + sampleSize)

#histograms for each variable
#differentiate species by color
sns.FacetGrid(data = iris,hue = "Species").map(sns.histplot,"Petal Length").add_legend()
sns.FacetGrid(data = iris,hue = "Species").map(sns.histplot,"Petal Width").add_legend()
sns.FacetGrid(data = iris,hue = "Species").map(sns.histplot,"Sepal Length").add_legend()
sns.FacetGrid(data = iris,hue = "Species").map(sns.histplot,"Sepal Width").add_legend()

#scatterplots
sns.FacetGrid(iris, hue = "Species").map(plt.scatter, "Sepal Length", "Sepal Width").add_legend()
sns.FacetGrid(iris, hue = "Species").map(plt.scatter, "Petal Length", "Petal Width").add_legend()
sns.FacetGrid(iris, hue = "Species").map(plt.scatter, "Sepal Length", "Petal Width").add_legend()
sns.FacetGrid(iris, hue = "Species").map(plt.scatter, "Petal Length", "Sepal Width").add_legend()
sns.FacetGrid(iris, hue = "Species").map(plt.scatter, "Sepal Length", "Petal Length").add_legend()
sns.FacetGrid(iris, hue = "Species").map(plt.scatter, "Petal Width", "Sepal Width").add_legend()
 

plt.show()


