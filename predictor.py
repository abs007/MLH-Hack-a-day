#loading dataset
import pandas as pd
import numpy as np
# data preprocessing
from sklearn.preprocessing import StandardScaler
# data splitting
from sklearn.model_selection import train_test_split
# data modelling
from sklearn.neighbors import KNeighborsClassifier

import warnings
warnings.filterwarnings("ignore")

import pickle


data = pd.read_csv('heart.csv')

#Model Preparation 

Y_train = data["target"]
X = data.drop('target',axis=1)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)


scaler = StandardScaler()
X_train = scaler.fit_transform(X)
#X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, Y_train)

#test_data = np.array(user_data)
#test_data = test_data.reshape((1,-1))

pickle.dump(knn,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


def training_scaler(X_train=X_train):

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    return scaler