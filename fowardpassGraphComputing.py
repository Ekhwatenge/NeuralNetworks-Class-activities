def forward_pass(a,b,c):
    # Step-by-step computation following the graph structure
    d=2*b # Multiplication step
    e=a+d # Addition step
    L=c*e # Final multiplication step
    
    return L

# Example usage with specific inputs:
a_value=3; b_value=1; c_value=-2;
output_result=forward_pass(a_value,b_value,c_value)
print("Output:",output_result)
