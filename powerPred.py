# David Markham
# 22-12-2020
# Development of a Web Application. 
# Flask provides you with tools, libraries and technologies,
# that allow you to build a web application.
# Here is a script that runs a web application that gives you back random uniform or normal number.

# Flask for web app.
import flask as fl

# Numpy for numerical work.
import numpy as np 

# Import 

# Create a new web app.
# Setting variable to call function.
app = fl.Flask(__name__)  # __name__ is built in variable, the main script in program. 

# Add root route.
# @app. route("/") is a Python decorator that Flask provides to assign URLs,
# in our app to function easily.
@app.route("/") # flask command enables function below to have diff mech for input and output.
def home(): # 
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()} # Return uniform numbers from 0 to 1. 

# Add normal route.
@app.route('/api/normal') # gen random numbers centred around 0 minus or positive.
def normal(): 
  return {"value": np.random.normal()} # Return Numpy random normal number from Python Dictionary.s