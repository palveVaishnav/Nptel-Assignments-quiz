'''
Question 1
Here is an function to return the maximum value among three positive integers. There is an error in this function. 
Provide an input triple (n1,n2,n3), where n1, n2 and n3 are all positive integers, for which max3bad produces an incorrect output.
'''
def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)

#answer: when first two elements are equal.
max3bad(5,5,10)
max3bad(6,6,11)
'''
Question 2
Here is an implementation of mergesort, along with the associated merge function.
There is a small error in the implementation. Provide an input list for which this version of mergesort produces an incorrect output.
'''
def mergebad(l1,l2):

  (lmerged,i,j) = ([],0,0)

  while i+j < len(l1) + len(l2):
    if i == len(l1):
      lmerged.append(l2[j])
      j = j+1
    elif j == len(l2):
      lmerged.append(l1[i])
      i = i+1
    elif l1[i] < l2[j]:
      lmerged.append(l1[i])
      i = i+1
    elif l2[j] < l1[i]:
      lmerged.append(l2[j])
      j = j+1
    else:
      lmerged.append(l1[i])
      i = i+1
      j = j+1
    
  return(lmerged)    

def mergesortbad(l):
  if len(l) < 2:
    return(l)
  else:
    n = len(l)
    leftsorted = mergesortbad(l[:n//2])
    rightsorted = mergesortbad(l[n//2:])
    return(mergebad(leftsorted,rightsorted))

#answer: any list with dublicate elements.
mergesortbad([-1,0,6,-1,0,6,-1])
mergesortbad([5,5,4,4,3,3,2,1,1])

'''
Question 3
Here is a function to compute the largest of four input integers. You have to fill in the missing lines.
'''
def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line
  if x>=w and x>=y and x>=z:
    maximum=x
  if y>=w and y>=x and y>=z:
    maximum = y
  if z>=w and z>=x and z>=y:
    maximum = z
  return(maximum)

'''
Q.4
A list is a palindrome if it reads the same forwards and backwards. For instance [], [7], [8,11,8] and [19,3,44,44,3,19] are palindromes, 
while [3,18,4] and [23,14,3,14,3,23] are not. Here is a recursive function to check if a list is a palindrome. 
You have to fill in the missing argument for the recursive call.

def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(...)
'''
#answer

def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(
       # Complete the recursive call below this line
        	l == l[::-1]
    )







