#non-recursive way to write the binary search algorithm, iterative solution

def binary_search(list, target):
  #list.sort()
  #we need two variables to indicate the beginning and end of the list
  first = 0   #constant time operation
  last = len(list) - 1  #constant time operation

  while first <= last:
    midpoint = (first + last)//2  #simple arithmetic operation, the runtime is constant

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1   # this is a log n operation because we ask the loop to constantly split the list and redefine the value of first
    else:
      last = midpoint - 1  # this is a log n operation because we ask the loop to constantly split the list and redefine the value of last
    
  return None

# It is worth noting that the list must be sorted before any operation is carried out
def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")

#numbers = [1,2,3,4,5,6,7,8,9,10]

#result = binary_search(numbers, 9)
#verify(result)

#Recursive way to write the binary search algorithm, will not return an index of the item, will return a True if it exists and a False otherwise

def binarysearch(list, target):
  if len(list) == 0:
    return False
  else:
    midpoint = len(list)//2
    if list[midpoint] == target:
      return True
    else:
       if list[midpoint] < target:
         return binarysearch(list[midpoint+1:], target)
       else:
         return binarysearch(list[:midpoint], target)
      
      
def verifying(result):
  print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binarysearch(numbers, 2)
verifying(result)
  
 