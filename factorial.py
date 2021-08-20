# Given a non-negative number, N, return the last digit of the factorial of N 

# Understand
# First of all we have to find the factorial of the said number
# We then have to find the last digit of the result and return it 


# Match
# Plan
# Implement
# Review
# Evaluate



#regular factorial code
#using a while loop
def fact(n):
  result = 1
  while n > 1:
    result = n * result
    n -= 1
  return result

#using a for loop

def facto(n):
  result = 1
  if n >= 1:
    for i in range(1, n+1):
      result = result * i
    return result
  else:
    print("N has to be a positive number!")

#using recursive solution, we need a base case and a recursive case

def factoriall(n):
  if n <= 1:
    return 1
  else:
    return n * factoriall(n-1)
  



print(factoriall(1))
print(factoriall(2))
print(factoriall(3))
print(factoriall(4))


