import numpy as np

# Define sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1-x)

# Example inputs and true label for binary classification
input_vector = np.array([0])
true_label = 0 # Did not buy car

# Initial guess for weights and bias in logistic regression context
weights = np.array([0]) 
bias_term = 0 

# Forward pass calculation of predicted probability using sigmoid function
predicted_probability = sigmoid(np.dot(weights,input_vector)+bias_term)

# Error calculation using cross entropy loss for binary classification 
error_value=(true_label*np.log(predicted_probability)+(1-true_label)*np.log(1-predicted_probability))

# Backward pass: calculate gradient of cross entropy loss wrt weights 
gradient_wrt_weights=(predicted_probability-true_label)*input_vector[0]

print("Gradient wrt Weights:", gradient_wrt_weights)
