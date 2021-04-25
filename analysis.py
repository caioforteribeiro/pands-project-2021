#Program that reads Fisher's Iris data set,
#outputs the summary of each variable to a txt file,
#saves a histogram of each variable as png images,
#and outputs a scatter plot of each pair  of variables.
#Author: Caio Forte Ribeiro

#Import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set seaborn as default style
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

#Create list with only the measured attibrutes

attributes = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

#Iterate through the list and create histplots for each attribute
for attribute in attributes:
    sns.FacetGrid(data = iris, hue = "Species").map(sns.histplot, attribute).add_legend()
    #Saves each histplot to png files
    plt.savefig("histplot_"+attribute +".png")
    
    #Adds second attribute to be paired for scatterplots
    for pairAttribute in attributes:
        sns.FacetGrid(data = iris, hue = "Species").map(sns.scatterplot, attribute, pairAttribute).add_legend()
        #Saves scatterplots of each possible combination to png files
        plt.savefig("scatter_"+attribute+pairAttribute+".png")




