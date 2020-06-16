# Given an array, rotate the array to the right by k steps, where k is non-negative

# Input:[1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]

# rotate 1 step to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]

# rotate 1 step to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Can be solved using multiple methods
# No need to return anything, modify the array in place

# Understand
# The key action in this problem is rotating the array to the right by k steps
# The input is a list and an integer k that is positive
# We are not returning something in this problem, we are just modifying the list in place   

# # Match
# We are repeating a process multiple times on an array and we can deduce from this that at some point we would need to use a loop

# Plan  
# for i in  range(1,k+1):
#   last_item = take the number at the end of the list
#   input_array.bring it to the beginning of the list




# Implement
def rotate_array(input_array, k):
  for i in range(1, k+1):
    variable = input_array.pop()
    input_array.insert(0, variable)

# Review 
# Evaluate

print(rotate_array([-1,-100,3,99], 2))