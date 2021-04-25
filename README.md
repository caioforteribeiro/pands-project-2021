# Fisher's Iris data set

**Author:** Caio Forte Ribeiro

**Course:** Programming and Scripting (2021) - GMIT Data Analytics


## Summary
Fisher's Iris data set records petal and sepal lenghts and widths in centimetres from 3 related Iris flower species (Iris setosa, Iris versicolor, and Iris virginica). It was first published in 1936 by the biologist and statistician Ronald Fischer, as part of his paper *The use of multiple measurements in taxonomic problems* (available [here](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)). The data set contains a total of 150 samples, 50 of each flower species. Based on a linear combination of the 4 measured features (lenghts and widths of petals and sepals), Fischer developed a statistical method to distinguish between the 3 species of Iris. The data set is still widely used as a test case for machine learning techniques. 


## Task
Write a program (**analysis.py**) that reads Fisher's Iris data set, outputs the summary of each variable to a text file, saves a histogram of each variable as png images, and outputs a scatter plot of each pair of variables.

## Code
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

col_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

iris = pd.read_csv("iris.data", header = None, names = col_names)

setosa = iris[iris["Species"] == "Iris-setosa"]
versicolor = iris[iris["Species"] == "Iris-versicolor"]
virginica = iris[iris["Species"] == "Iris-virginica"]

sumSet = str(setosa.describe())
sumVers = str(versicolor.describe())
sumVirg = str(virginica.describe())

summary = "\t\t\tIris setosa\n"+ sumSet + "\n\n" + \
        "\t\t\tIris versicolor\n" + sumVers + "\n\n" + \
        "\t\t\tIris virginica\n" + sumVirg

sampleSize = str(iris.groupby("Species").size())

with open("summary.txt", "w") as f:
        f.write(summary + "\n\n\t\t\tSample Distribution\n" + sampleSize)

attributes = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

for attribute in attributes:
    sns.FacetGrid(data = iris, hue = "Species").map(sns.histplot, attribute).add_legend()
    plt.savefig("histplot_"+attribute +".png")
    for pairAttribute in attributes:
        sns.FacetGrid(data = iris, hue = "Species").map(sns.scatterplot, attribute, pairAttribute).add_legend()
        plt.savefig("scatter_"+attribute+pairAttribute+".png")

```


## Explaining the code
### Importing libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
```
For this project, 3 libraries were used:

1. [pandas](https://pandas.pydata.org/): a library for data manipulation and data analysis in Python. In this project, `pandas`was used to read the original data set and store it in a dataframe.
2. [matplotlib.pyplot](https://matplotlib.org/): matplotlib is an open source library for data visualization in Python, and `pyplot` is a useful matplotlib-based API with plotting functionalities similar to [Matlab](https://www.mathworks.com/products/matlab.html). In this project, `matplotlib.pyplot` was used to output (save) plots as image files (.png).
3. [seaborn](https://seaborn.pydata.org/index.html): a library built on top of `matplotlib` and which provides integration with `pandas` data structures to create stilish and informative data plots. `seaborn` styles were set as default using `sns.set()` - this makes seaborn's stylesheet to overwrite pyplot's.

All imported libraries are included in the [Anaconda3 package](https://docs.anaconda.com/anaconda/). They can also be installed using `pip.install`(which is also included in Anaconda3). More information on `pip.install` can be found [here](https://pip.pypa.io/en/stable/cli/pip_install/).

### Reading the data set

```python
col_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

iris = pd.read_csv("iris.data", header = None, names = col_names)
``` 
The [original data set](https://github.com/caioforteribeiro/pands-project-2021/blob/main/iris.data) featured only the data. Column headers were missing from the original file, so a `list` object (`col_names`) was created to store these headers and make it easier to manipulate the data. The data set was read as a csv file using `pandas.read_csv`, and `col_names` was passed as the array type value for the `names` attribute. This assigned the string values in the list as the names of the columns of the resulting dataframe (`iris`).

### Writing the summary in a text file

```python
setosa = iris[iris["Species"] == "Iris-setosa"]
versicolor = iris[iris["Species"] == "Iris-versicolor"]
virginica = iris[iris["Species"] == "Iris-virginica"]
```
We start by selecting each of the species from the column "Species" in our `iris` dataframe, and storing each in a corresponding variable.

```python
sumSet = str(setosa.describe())
sumVers = str(versicolor.describe())
sumVirg = str(virginica.describe())
```
The `pandas.describe()` method is then called for each species, returning a summary of their numeric attributes (Petal Length and Width; Sepal Length and Width). This summary includes statistical information of each attribute (mean, std, percentiles, etc). However, `describe()`returns an array object, so we needed to convert the results into strings, so they could be written to a txt file.

```python
summary = "\t\t\tIris setosa\n"+ sumSet + "\n\n" + \
        "\t\t\tIris versicolor\n" + sumVers + "\n\n" + \
        "\t\t\tIris virginica\n" + sumVirg

sampleSize = str(iris.groupby("Species").size())

with open("summary.txt", "w") as f:
        f.write(summary + "\n\n\t\t\tSample Distribution\n" + sampleSize)
```
To write the summaries of each species and some basic information on distribution (using `pandas.size()`) into a text file ([summary.txt](https://github.com/caioforteribeiro/pands-project-2021/blob/main/summary.txt)), `with open()` method was used in `w` (write) mode. Some basic formatting (`\n` and `\t`) was added to improve readability.

### Plotting histograms and scatterplots
```python
attributes = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

for attribute in attributes:
    sns.FacetGrid(data = iris, hue = "Species").map(sns.histplot, attribute).add_legend()
    plt.savefig("histplot_"+attribute +".png")
    for pairAttribute in attributes:
        sns.FacetGrid(data = iris, hue = "Species").map(sns.scatterplot, attribute, pairAttribute).add_legend()
        plt.savefig("scatter_"+attribute+pairAttribute+".png")
```
We start by calling out the list of attributes that will be plotted for each species. For both the histograms and the scatterplots, `seaborn.Facetgrid` class was used and the "Species" columns in the data set was set as the parameter for differenting hues. This approach allows us to plot selected data from all the three species into the same set of axes. It also facilitates visualization and allows us to get quick insights from the data distribution, as the species are easily distinguishable from each other by colour. A `for` statement was used to avoid unnecessary repetitions in the code and keep it concise. It basically iterates through the list of attributes, and generates a `seaborn.histplot`for each attribute, saving the resulting histograms in the current directory. 

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/histplot_Petal%20Length.png" alt = "Petal Length">

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/histplot_Petal%20Width.png" alt = "Petal Width">

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/histplot_Sepal%20Length.png" alt = "Sepal Length">

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/histplot_Sepal%20Width.png" alt = "Sepal Width">

The same approach is repeated for the scatterplots, but since they require 2 arguments (an attribute and a pair attribute),another `for` statement was nested inside the first one to iterate through 2 attributes each time. Below are some examples of the generated plots (the full set of images can be found in the [repository](https://github.com/caioforteribeiro/pands-project-2021)):

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/scatter_Petal%20LengthPetal%20Width.png" alt = "Petal Length vs Petal Width">

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/scatter_Sepal%20LengthSepal%20Width.png" alt = "Sepal Length vs Sepal Width">

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/scatter_Petal%20LengthSepal%20Width.png" alt = "Petal Length vs Sepal Width">

<img src = "https://github.com/caioforteribeiro/pands-project-2021/blob/main/scatter_Petal%20WidthSepal%20Width.png" alt = "Petal Width vs Sepal Width">

## Discussion
There are several posssible approaches to the tasks required for this project. We could, for instance, have written a summary of the whole data set instead of having one for each species of flower. However, it wouldn't give us any useful insight of the flowers's attributes as statistical determinants for the observed species, so a discriminated summary was preferred. Information about distribution ("Sample size") was included only for additional clarity, as the `describe()` method already outputs the "count" of each data class. We could also have defined a function for reading and writing the summary into a text file, but this would add unnecessary lines to our code or would require a separate script for storing the function(s).

For the histograms and scatterplots, a more efficient approach - and one which would give us the same amount of information but in a more concise way - 


## References

- Iris Dataset: http://archive.ics.uci.edu/ml/datasets/Iris
- CSV with PANDAS: https://realpython.com/python-csv/
- https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
- [Fischer, R A: The use of multiple measurements in taxonomic problems](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x_)
- Iris dataset methods of analysis: https://www.kaggle.com/kamrankausar/iris-dataset-ml-and-deep-learning-from-scratch
- https://www.kaggle.com/kamrankausar/iris-dataset-ml-and-deep-learning-from-scratch
- https://seaborn.pydata.org/tutorial/axis_grids.html
- https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib
- https://stackoverflow.com/questions/38082602/plotting-multiple-different-plots-in-one-figure-using-seaborn
- https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
- https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette
- https://seaborn.pydata.org/generated/seaborn.pairplot.html
- https://seaborn.pydata.org/generated/seaborn.regplot.html
- https://dev.to/thalesbruno/subplotting-with-matplotlib-and-seaborn-5ei8
- https://www.kaggle.com/dcstang/how-to-do-subplots-iris-dataset
- https://seaborn.pydata.org/generated/seaborn.histplot.html
- https://seaborn.pydata.org/generated/seaborn.scatterplot.html
- https://stackoverflow.com/questions/67150094/how-can-i-condense-a-series-of-seaborn-scatterplots-using-for-loops
- https://seaborn.pydata.org/generated/seaborn.set.html
