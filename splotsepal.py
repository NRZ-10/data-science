import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
sepal_length = iris.data[:, 0]
sepal_width = iris.data[:, 1]
plt.scatter(sepal_length, sepal_width, color="green", marker='o')
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.show()