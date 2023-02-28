# -*- coding: utf-8 -*-
"""linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EaIdA85nQ5FmSby1RCszNDsieo932MUN
"""

# importing numpy and linear regression library
import numpy as np
from sklearn.linear_model import LinearRegression

# input values (yearl) to the linear regression model
x = np.array([2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]).reshape((-1, 1))

# ouput values to the linear regression model
y = np.array([43, 67, 34, 76, 71, 85, 88, 96])

# Training the linear regression model with given input dependent and independent variables.
model = LinearRegression().fit(x, y)

# predicting the output production values for the input new years.

y_pred = model.predict([[2014], [2015]])
y_pred

# import matplotlib library to line plot the input years and production values.
import matplotlib.pyplot as plt

# trainable dependent and indepenedent values
x = np.array([2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013])
y = np.array([43, 67, 34, 76, 71, 85, 88, 96])

# plotting the output values w.r.t input values.
plt.plot(x, y, 'o')

# calculate the slope and intercept for given input values to form line equation.
m, b = np.polyfit(x, y, 1)

# plot the line equation w.r.t input years.
plt.plot(x, m*x + b)

# plot the line equation and values.
plt.show()

# plot the given years and output values.

x = np.array([2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
y = [43, 67, 34, 76, 71, 85, 88, 96]

# added the predicted values of years 2014 and 2015 and plotted the graph
y.extend(list(y_pred))
y = np.array(y)
plt.plot(x, y, 'o')
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)
plt.show()