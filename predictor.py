#loading dataset
import pandas as pd
import numpy as np
# data preprocessing
from sklearn.preprocessing import StandardScaler
# data splitting
from sklearn.model_selection import train_test_split
# data modelling
from sklearn.neighbors import KNeighborsClassifier


def heart_attack_prediction(user_data):

    data = pd.read_csv('heart.csv')

    #Model Preparation 

    y = data["target"]
    X = data.drop('target',axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=10)
    knn.fit(X_train, y_train)
    
    test_data = np.array(user_data)
    test_data = test_data.reshape((1,-1))

    return knn.predict(X_test)
