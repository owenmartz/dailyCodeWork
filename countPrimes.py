# Question: Count the number of prime numbers less than a non-negative number, n

# Understand

# We shall keep count of the numbers that are found to be prime between a certain range

# a number is a prime number if its divisible by one and itself leaving no remainder

# the input is an integer and the output will also be an integer

# Match

# Process repeating itself problem, hence the need for a loop, also a prime factors kind of problem

# Plan

# Test cases:
#  2, 3, 5, 7 -> Prime numbers between 0 and 10

# we will have to loop through the numbers in the range and check whether each one is Prime

# if number is prime, we increment count by one, if not we increment the number in the range by one

# n = 6

# 1 is not prime

# we start at 2 because it is the first prime number
# go to the next number

# is 3 divisible by 2? no
# then 3 is prime
# go to the next number

# is 4 divisible by 2? yes
# 4 is not prime
# go to next number

# is 5 divisible by 2? no
# is 5 divisible by 3? no
# is 5 divisible by 4? no
# 5 is prime
# go to next number

# Meanwhile, we have to keep a count of the prime numbers 


# Implement

# We need to write a function to determine if the numbers are prime

def isPrime(n):
  for current_number in range(2,n):
    if n % current_number == 0:
      return False
  return True    

def countPrimes(n):
  count = 0
  for current_number in range(2, n):
    if isPrime(current_number):
      count += 1
  return count  

print(countPrimes(6))

# Review


# Evaluate