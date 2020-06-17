# Given a non-empty array of digits representing a non-negative integer, plus one to the integer. Return the resulting integer as an array. The digits are stored such that the most significant digit is at the head of the list and each element in the array contains a single digit. 

# You may assume the integer does not contain any leading zero, except the number itself.

# Input: [1,2,3] Output: [1,2,4] - The array represents integer 123
# Input: [4,3,2,1] Output: [4,3,2,2] - The array represents the integer 4321

# Code:

def plusOne(digits):
  new_string = [str(num) for num in digits]
  num = int("".join(new_string))
  num += 1
  new_array = [int(i) for i in str(num)]
  return new_array



print(plusOne([1,2,3]))

  
