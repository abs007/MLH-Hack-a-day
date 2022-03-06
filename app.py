import pickle
import numpy as np
from predictor import scaler

model = pickle.load(open('model.pkl','rb'))


def predict(*args):
    #int_features= args
    int_features=[int(x) for x in args]

    user_data = np.array(int_features).reshape((1,-1))
    
    user_data_scaled = scaler.transform(user_data)

    prediction = model.predict(user_data_scaled)
    print (prediction)

