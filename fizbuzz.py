# Given an input, print all numbers up to and including that input, unless they are divisible by 3, then print "fizz" instead, or if they are divisible by 5, print "buzz". If the number is divisible by both, print "fizzbuzz"

# Understand
# The prompt requires us to scan and print numbers in a particular range including the last number, we then have to meet the declared conditions once we encounter numbers that satisfy the provisions above

# Key actions involve printing the words, fizz, buzz or fizbuzz depending on the divisibility of the numbers 

# The input is a number, an integer to be specific. The output will either be an integer or the words above

# The format would either be int or strings
# # Match
# A similar problem would be repeating processes on numbers and determining divisibility

# Plan 

# def fizzbuzz(n):
#   go through range including the input n
#     determine whether n is divisible by both 3 and 5
#       print fizzbuzz
#     determine whether n is divisible by 3 
#       print fizz
#     determine whether n is divisible by 5
#       print n  
# Implement

def fizbuzz(n):
  for num in range(1, n+1):
    if num % 3 == 0 and num % 5 == 0:
      print("fizzbuzz")
    elif num % 3 == 0:
      print("fizz")
    elif num % 5 == 0:
      print("buzz")
    else:
      print(num)       

fizbuzz(15)      
# Review
# Evaluate