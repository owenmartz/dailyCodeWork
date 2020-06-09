# this problem is from project Euler
# https://projecteuler.net/problem=25

# The Fibonacci sequence is defined by the recurrence relation:

#   Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

### PROBLEM STATEMENT ###

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


## Understand:
## this would require us to first go through a list of fibonacci numbers and return the index of the first number we encounter that has four figures

##key actions would involve creating a list, then appending the sum of the previous two items to the list. We would then have to check the length of the item that we just added to the list each time we do the appending to compare it to the length we are looking for


## Match:

##number operations whereby we repeat a process multiple times on a number, finding the length of a string


## Plan:

## to get the fib sequence
## start with 0 and 1
## add the last two terms to get the third term
## test how many digits the current term has - if over 1000, return the index of that term
## repeat

## Then, translate to code!

def fibonacci_1000(n):
  new_list = [0, 1]
  while len(str(new_list[-1])) < n:
    new_term = new_list[-1] + new_list[-2]
    new_list.append(new_term)


  indexOfLastTerm = len(new_list) - 1
  print(indexOfLastTerm)  

fibonacci_1000(1000)  


      

