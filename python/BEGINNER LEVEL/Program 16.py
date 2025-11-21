# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

def largest_of_three(a, b, c):
    # Assume a is the largest to start
    largest = a
    
    if b > largest:
        largest = b
    if c > largest:
        largest = c
        
    return largest
