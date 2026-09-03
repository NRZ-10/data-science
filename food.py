import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

food = pd.read_csv("food.csv")
X = food[["Sweetness", "Crunchiness"]]
y = food["FoodType"]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

tomato = pd.DataFrame({"Sweetness": [6], "Crunchiness": [5]})
tomato_scaled = scaler.transform(tomato)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, y)
prediction = knn.predict(tomato_scaled)
print(f"The predicted food type for the tomato is: {prediction[0]}")