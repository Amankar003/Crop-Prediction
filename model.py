import pickle

import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('Crop_recommendation.csv')

df.head(5)

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

x_train

model = RandomForestClassifier()
model.fit(x_train, y_train)

Prediction = model.predict(x_test)

pickle.dump(model, open("model.pkl", "wb"))

accuracy = model.score(x_test, y_test)
print("Accuracy Score : ", accuracy)

new_features = [[117, 32, 43, 26.7635743, 52.12345678,6.123456789, 129.1234567]]
predicted_crop = model.predict(new_features)
print("Preedicted Crop :", predicted_crop)