from sklearn.linear_model import Ridge
import numpy as np

# Sample dataset
X = np.array([[0], [1], [2]])
y = np.array([0, 0.5, 1])

# Apply Ridge regression
ridge_model = Ridge(alpha=0.01)
ridge_model.fit(X,y)

print("Coefficients:", ridge_model.coef_)
