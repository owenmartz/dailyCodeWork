# Given an unsorted integer array, find the first missing positive integer. 

# Example:
# Given [1,2,0] returns 3
# [3, 4, -1, 1] return 2
# [-8, -7, -6] returns 1
# Your algorithm should run in O(n) and use constant space

# Understand
# Our key action is trying to find the first missing positive integer
# It is worth noting that because the prompt does not state whether the integers will be signed or unsigned, we should expect to find both positive and negative integers
# The input in this case is a list of integers
# The output is going to be a positive integer

# # Match
# Repeating a process for a list of integers, we have to compare the integers in order to determine which value is to be output
# At some point we would definitely need to use a for loop

# # Plan     
# Let us analyze the list [3, 4, -1, 1]

# Going through the list, we have the numbers below, any negative numbers are ignored because they do not influence the output
# --
# 1 - True
# 2 - False
# 3 - True
# 4 - True
 
# Create an empty list
# for each number in the input list
#   if the number is smaller than 0, ignore the number
#   if the number is larger than the current length of the empty list, resize the list to be of that length
#   set the value of the place in the list corresponding with that integer to True 

# Implement

def first_missing_positive_integer(integers):

  found_integers = []
  for integer in integers:
    if integer < 0:
      continue #ignore the number
    if integer + 1 > len(found_integers):
      extend_size = integer - len(found_integers) + 1
      # The extend function in python allows us to take two rays and combine them into one list. It does not return a new list, it just changes the original list since in python, lists are mutable. The extend function takes a list as a parameter
      found_integers.extend([False] * extend_size)
    found_integers[integer] = True

  #Second planning phase
  # for position in found_integers:
  #   ignore the 0th index
  #   check to see if the value in the list is False,
  #   if so return the index
  missing_integer = 0
  for position in range(1,len(found_integers)):
    if found_integers[position] == False:
      missing_integer = position
      return missing_integer
  if missing_integer == 0 and len(found_integers) == 0:
    return 1
  elif missing_integer == 0 and len(found_integers) > 0:
    return len(found_integers)  

print(first_missing_positive_integer([1,2,4]))
     
       




# Review


# Evaluate
