import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('hiring.csv')
print(dataset)

#replacing nan values with 0
dataset['experience'] = dataset['experience'].replace(np.nan, 0)
dataset['test_score(out of 10)'] = dataset['test_score(out of 10)'].replace(np.nan, 0)

print(dataset)

print('Reading csv successful')
# first 3 i.e., experience, test score, interview score
x = dataset.iloc[:, :3]
#salary
y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(x, y)
print('Model fit successful')

#saving model
pickle.dump(regressor, open('model.pkl','wb'))
print('Model dumped successful as model.pkl')