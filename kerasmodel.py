# Code adapted from: 
# https://github.com/keras-team/keras-io/blob/master/guides/serialization_and_saving.py

# Neural networks
import tensorflow.keras as kr
import pandas as pd
import numpy as np

# Read Dataset into Dataframe
ds = pd.read_csv("powerproduction.csv")

# Create Keras Seq Model
class KerasModel: 
    def kerasPrediction(x):         
        model = kr.models.Sequential()
        model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
        model.compile(optimizer='adam', loss='mean_squared_error')

        
        model.fit(ds['speed'], ds['power'], epochs=500, batch_size=10)

        predict = model.predict([x])

        
        result = round(np.ndarray.item(predict[0]),10)

        return {"value": result} 