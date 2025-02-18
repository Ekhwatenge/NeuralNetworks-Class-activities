import numpy as np

# True Label One-Hot Vector
true_label_vector = np.array([1., .5]) # Simplified example; actual would include third 
#element too but not needed here since other elements don't contribute due being multiplied by 
# zero in formula 

# Predicted Probabilities Vector 
predicted_prob_vector = np.array([.4,.6])

# Calculate Cross Entropy Loss (simplified)
def cross_entropy_loss(true_label_vector,predicted_prob_vector):
    return -np.sum(true_label_vector * np.log(predicted_prob_vector))

loss_value=cross_entropy_loss(true_label_vector,predicted_prob_vector)

print("Loss:",loss_value)

#This code illustrates calculating cross entropy loss between predicted probabilities 
# and actual labels using Python/Numpy libraries though note real scenarios 
# involve more complex architectures typically implemented via frameworks like TensorFlow/Keras!
