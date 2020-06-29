# Learning-Flask-with-simple-Hiring-Dataset
This is a learning demo project for learning Flask and its use. Basic Information of flask and its different requirements will be also mentioned.
<br/>
Flask-<br/> 
web application framework
<br/><br/>
Pickle module-<br/>
It is used for serialization and de-serialization a python object.<br/>
It serializes a object(list, dict) before writing to file.
<br/><br/>
<b>File Hierarchy</b><br/>
![Repository Hierarchy](folder_hierarchy.JPG)
<br/><br/>
<b>3 steps towards using Flask-</b><br/>
<b>1. Loading saved model and Initializing Flask app</b><br/>
Firstly, code of building a simple regression model and then saving the model by serializing it using pickle.<br/>
model.py- The Machine Learning model to predict employee salaries based on training data according to ‘hiring.csv’ file.<br/>
<b>2. Redirecting API to home page</b><br/>
app.py -  File with Flask APIs that receives employee details through GUI/API calls, computes the predicted value based on given model and returns it.<br/>
templates - This folder contains the HTML template (index.html) i.e., home page before and after predict.<br/>
index.html - The html file of home page which redirects.<br/>
<b>Redirecting to home page</b><br/>
![Input on home page](inputs.JPG)
<br/>
<b>3. Redirecting API to predict result</b>
<b>Redirecting to predict</b><br/>
![Predict result](predict.JPG)
<br/><br/>
