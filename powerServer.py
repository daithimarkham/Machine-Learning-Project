# David Markham
# 06-01-2021
# Development of a Web Application. 
# Deploy our Deep Learning model for anyone in the world to access it.
# Flask provides you with tools, libraries and technologies,
# that allow you to build a web application. 

# Flask for web app.
import flask as fl
# Numpy for numerical work.
import numpy as np 
from tensorflow import keras 



# Create a new web app.
# Setting variable to call function.
app = fl.Flask(__name__, static_url_path="",static_folder="static")  # __name__ is built in variable, the main script in program. 

# Add root route.
# @app. route("/") is a Python decorator that Flask provides to assign URLs,
# in our app to functions easily.
@app.route("/") # flask command enables function below to have diff mech for input and output.
def home(): # Index page 
  return app.send_static_file('index.html')


# Add normal route.
@app.route('/api/normal') # gen random numbers centred around 0 minus or positive.
def normal(): 
  return {"value": np.random.normal()} # Return Numpy random normal number from Python Dictionary.s


if __name__ == '__main__':
    app.run()


# References
# https://towardsdatascience.com/deploying-a-keras-deep-learning-model-as-a-web-application-in-p-fc0f2354a7ff 
# https://www.tensorflow.org/guide/keras/save_and_serialize 
# https://getbootstrap.com/
# https://www.w3schools.com/html/ 