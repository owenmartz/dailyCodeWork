# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

#Solution 1

def over_nine_thousand(lst):
  if len(lst) < 1:
    return 0
  i = 0
  sum = 0
  while sum <= 9000:
      sum += lst[i]
      i += 1
  return sum 


#Solution 2

#def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))




#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))