def forward_pass(a, b, c):
    # Compute intermediate values
    d = 2 * b
    e = a + d
    
    # Compute output (loss)
    L = c * e
    
    return L, d, e

def backward_pass(a, b, c):
    # Forward pass to get intermediate values
    _, d, e = forward_pass(a, b, c)
    
    # Backward pass: compute derivatives of L w.r.t each variable
    partial_L_c = e  # ∂L/∂c = e
    
    partial_L_e = c  # ∂L/∂e = c
    
    partial_e_d = 1  # ∂e/∂d = 1
    partial_d_b = 2   # ∂d/∂b = 2
    
    partial_L_d = partial_L_e * partial_e_d  
                  # Since ∇l/d=(ce)/e*(de/d) but here it simplifies to just (ce)*(1).
    
                  # However we should correctly apply chain rule as follows:
                  # Given that L=c*e and then considering path through 'e' which is correct.
    
                  # But since our goal is to find how changes in 'b' affect 'L', we need:
    
                  # So for clarity let's directly calculate it step by step without confusion.
    
                  ## Correctly applying chain rule for derivative w.r.t. 'd':
                  ## We know that 
                  
                  ## For derivative of L with respect to 'b', using chain rule properly:
                  
      ### Chain Rule Application Explained in Steps Below This Line ###
      
      ### Step-by-Step Calculation of Derivative w.r.t. 'a'
      ### Since we have: 
      ###   - \( \frac{\partial{L}}{\partial{a}} \) which equals \( \frac{\partial{L}}{\partial{e}} \times \frac{\partial{e}}{\partial{a}} \)
      
      partial_e_a=1
      
      ### Hence,
      
      partial_L_a=partial_L_e*partial_e_a
      
      
     ### Similarly for Derivative w.r.t. 'b'
     ###### First find derivative of \( L \) with respect to \( d \), then apply chain rule again.
     ## Now correctly calculating derivative w.r.t. 'b':
      
   
   return {
           "Partial of L/c": f"{c}*(-2)",
           "Partial of L/e": f"{c}",
           "Partial of E/D": f"1",
           "Partial D/B": f"2",
           
           "Derivative Partial(L/a)":f"{c}*({1})={c}",
           
           

           


          }
# Example usage with specific values like a=3,b=1,c=-2,d=a+d,e=a+d,L=c*e
   
values={
        "a":3,
        "b":1,
        "c":-2
        
}
forward_result,L,d,e=forward_pass(values["a"],values["b"],values["c"]),None,None,None

print
