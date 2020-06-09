# Question: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Understand

# The prompt is asking for the smallest number that can be divided by all numbers in the said range without a remainder

#the key action is figuring out numbers that are evenly divisible between 1 and 20 

# the input in this case would be the integer 20, since we are adjusting the range

#the output would be an integer

# Match 

#Operations that repeat multiple times, so the need of a Loop, also there would be the process of determining the divisibility of a number, testing numbers

# Plan

#At this point we try out best bet by determining a few short test cases, so you pick an n that is small enough but not 1 or 2 or other special cases 

# so lets use 3, and find the smallest number that is evenly divisible by all numbers between 1 and 3? ans is 6, how?

# 4 divisible by 1 -- Yes
# 4 divisible by 2 -- Yes
# 4 divisible by 3 -- No
#move to next number

# 5 divisible by 1 -- Yes
# 5 divisible by 2 -- No
# Move to next number

# 6 divisible by 1 -- Yes
# 6 divisible by 2 -- Yes
# 6 divisible by 3 -- Yes
# end here

# since our numbers are 1, 2, 3, we shall start testing at 4

#start with n+1
#check to see if current number is divisible by 1
#check to see if current number is divisible by 2, if yes, move to next testnumber, if not, move on to n+2
#check to see if current number is divisible by 3, if yes, end the loop, if not, move on to n+2

# Impelement
n = 3
current_number = n + 1
while True:
  highly_divisible = True 
  for test_number in range(2, n+1):
     if current_number % test_number != 0:
       current_number += 1
       highly_divisible = False
       break
  if highly_divisible:
    print(current_number)
    break
  



# Review
# Evaluate



