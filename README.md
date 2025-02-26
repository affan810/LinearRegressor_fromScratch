# LinearRegressor_fromScratch

# Implementation 1 : Vector
### The above is the python implementation of Linear regression from Scratch using Numpy and visualised using Matplot lib
#### the lectured followed for the vector implementation is https://youtu.be/ltXSoduiVwY?si=2V7ZSxrqhk2Rl8xk by AssemblyAi

# Impletemtation 2 : Linear Regression using mean slope and intercept
### The core idea behind this implementation is to take all pairs of points, draw a line connecting the points, take average of slopes and intercepts and then draw a line using averages.
### Time complexity : Big-Oh(n^2) 
#### can be improved by considers all the points that lay on the same line all at once. and increases weight of the line by (number of dots on the line)/2 
#### Bias and varience : we take a pair of points, draw a line through them like normal, instead of just taking points that are on the line we introduce a varience to each point in form of a range()
##### eg. for the line (calculated from pair of points) the line passes through [1, 3] but we have a point at [1, 2.5] with a varience of range(0.5) then the give point will be considered on the line 
