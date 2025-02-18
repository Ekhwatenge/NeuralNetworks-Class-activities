from sklearn.linear_model import ElasticNet
import numpy as np

# Sample dataset
X = np.array([[0], [1], [2]])
y = np.array([0, 0.5, 1])

# Apply Elastic Net regression directly without CV (specify alpha manually)
elastic_net_model = ElasticNet(alpha=0.01) # Choose an appropriate alpha value here.
elastic_net_model.fit(X,y)

print("Coefficients:", elastic_net_model.coef_)
