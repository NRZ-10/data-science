from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Naive Bayes Classification")
print("--------------------------")
print(confusion_matrix(y_test, y_pred))

new_flower = [[1.5,3.5,1.4,0.2]]
prediction = model.predict(new_flower)

print("\nPredicted class:", iris.target_names[prediction[0]])