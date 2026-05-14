import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
# Train the linear regression model
model = LinearRegression()
model.fit(X, y)
# Make predictions
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)
# Plot the data points and the linear regression line

plt.scatter(X, y, color='blue')
plt.plot(X_new, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()