from sklearn.linear_model import ElasticNetCV
from sklearn.model_selection import KFold
import numpy as np

# Sample dataset
X = np.array([[0], [1], [2]])
y = np.array([0, 0.5, 1])

# Define custom CV object with fewer splits (e.g., KFold with n_splits=2)
kfolds = KFold(n_splits=2)

# Apply Elastic Net regression with custom CV object
elastic_net_cv = ElasticNetCV(cv=kfolds)
elastic_net_cv.fit(X,y)

print("Best Parameters:", elastic_net_cv.alpha_)
