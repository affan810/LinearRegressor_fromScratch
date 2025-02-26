from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from utils.line_calculate import line_calculate

'''
This method takes every pair of points to constructing line connecting the two points.
maintains a lists of all slopes and intercepts.
at the end returns a line that has slope equal to average of all the slops and intercept equal to average of all the intercepts
'''

#creates a dataset of 100 datapoints having 1 feature
X, Y = datasets.make_regression(
    n_samples= 100,
    n_features= 1,
    noise= 20,
    random_state = 69
)

#Plotting the given generated datapoints
fig  = plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], Y, color = "b", marker= "o", s = 30)
plt.plot(X, Y, "ko")
#plt.show()

# Convert X and Y into a list of (x, y) pairs
points = list(zip(X.flatten(), Y))

#Lists that will hold all the slopes and intercepts 
all_slope = list()
all_intercept = list()



'''
nested loop to check for all the pairs of points
'''
for i, (x1, y1) in enumerate(points):  # Loop over all pairs
    point1 = (x1, y1)
    for j in range(i + 1, len(points)):  # Start from the next index
        x2, y2 = points[j]
        point2 = (x2, y2)
        if x2 > x1:
            temp = point1
            point1 = point2
            point2 = temp
        m, c = line_calculate(point1, point2)  # m, c are the slope and intercept of the line connecting the points, respectively 
        all_slope.append(m)
        all_intercept.append(c)

x_range = (-2, 2)
x = np.linspace(x_range[0], x_range[1], 100)

avg_slope = np.mean(all_slope) #mean of all slopes
avg_intercept = np.mean(all_intercept) #mean of all interceots

y = avg_slope * x + avg_intercept #calculating all the y values using the average intercept and slopes

#plotting of the line of mean slope and intercept
plt.plot(x, y, label=f"y = {avg_slope}x + {avg_intercept}")
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Plot")

# Show plot
plt.show()
