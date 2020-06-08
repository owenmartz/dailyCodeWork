# Be sure to use the UMPIRE method to solve all these problems

# Determine if a non-negative number n, is a power of 3

# #Understand
# The prompt is asking us to establish whether the given number, which the user will provide, is a factor of 3

# A number is a power of 3 only if it can be divided by 3 continously until the answer is 1, so we shall take the number and continously divide it until we get a number that is equal to or less than 1

# The input is a number n, which is an integer, the output is going to be a boolean 

# The following would be the test cases:
# Non-negative numbers include but are not limited to 0, 1, 2, 3 ....

# 0 == False 
# 1 == True because 3^0 = 1
# 2 == False because nothing can be raised to 3 to give it a figure
# 3 == True because 3^1 = 3 
# 9 == True because 3^2 = 9
# 81 == True because 3^4 = 81
# #Match

# # In terms of seeing a similar problem to this, I can remember a similar one being the prime factorization tree in Math, or even trying to count the number of prime numbers in a range, repeating a process, raising an exponent
# #Plan

# The reason we would use a while loop here is because we do not know how many iterations we are gonna take

# We use for loops once we know how many steps we are bound to take

#def isPowerOfThree(n) --> Boolean
# while the number n is greater than 1
#   divide n by 3 until answer is equal to one or it is zero
  
#   check to see whether answer is equal to one and return True otherwise it is False


#Implement

def isPowerOfThree(n):
  while n > 1:
    n = n / 3
  if n == 1:
    return True
  else:
    return False

print(isPowerOfThree(0))


#Review
#Evaluate