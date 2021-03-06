# David Markham
# 06-01-2021
# Development of a Web Application. 
# Deploy our Deep Learning model for anyone in the world to access it.
# Flask provides you with tools, libraries and technologies,
# that allow you to build a web application. 

# Flask for web app.
import flask as fl
from kerasmodel import KerasModel as km
import numpy as np
import sys
import os

sys.path.append(os.path.abspath("kerasmodel"))

# Create a new web app.
# Setting variable to call function.
app = fl.Flask(__name__, static_url_path="",static_folder="static")  # __name__ is built in variable, the main script in program. 

# Add root route.
# @app. route("/") is a Python decorator that Flask provides to assign URLs.
# Home page route
@app.route("/") # flask command enables function below to have diff mech for input and output.
def home(): # Index page 
  return app.send_static_file('index.html')


# Here we request from our model we previously created.
@app.route('/api/kerasPrediction/<string:wind>', methods = ['GET', 'POST']) 
def KerasModelPredict(wind): 
    wind = float(wind)
    return km.kerasPrediction(wind) 



if __name__ == '__main__':
    app.run()


# References
# https://towardsdatascience.com/deploying-a-keras-deep-learning-model-as-a-web-application-in-p-fc0f2354a7ff 
# https://www.tensorflow.org/guide/keras/save_and_serialize 
# https://github.com/keras-team/keras-io/blob/master/guides/serialization_and_saving.py 
# https://www.pytorials.com/deploy-keras-model-to-production-using-flask/ 
# https://getbootstrap.com/
# https://www.w3schools.com/html/ 