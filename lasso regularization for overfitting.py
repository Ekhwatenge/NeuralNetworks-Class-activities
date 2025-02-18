from sklearn.linear_model import Lasso
import numpy as np

# Sample dataset
X = np.array([[0], [1], [2]])
y = np.array([0, 0.5, 1])

# Apply Lasso regression
lasso_model = Lasso(alpha=0.01)
lasso_model.fit(X,y)

print("Coefficients:", lasso_model.coef_)
