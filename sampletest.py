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

'''
Question 5
A positive integer n is said to be perfect if the sum of the factors of n, other than n itself,
add up to n. For instance 6 is perfect since the factors of 6 are {1,2,3,6} and 1+2+3=6.
Likewise, 28 is perfect because the factors of 28 are {1,2,4,7,14,28} and 1+2+4+7+14=28.
'''
#answer:

def factors(n):
    f=[]
    for i in range(1,n-1):
        if(n%i==0):
            f.append(i)
    
    return(f)

def sum(f):
    x=0
    for i in range(len(f)):
        x=x+f[i]

    return(x)
#main function
def perfect(n):
  #find all factors accept the number itself
    l=factors(n)
    #find the sum of factors
    s=sum(l)
    #compare and return
    if(n==s):
        return (True)
    else:
        return(False)
#exampes:
print(perfect(6))
print(perfect(28))
print(perfect(12))

'''
Question 6
Write a Python function sublist(l1,l2) that takes two sorted lists as arguments and returns True if the the first list is a sublist of the second list,
and returns False otherwise.
A sublist of a list is a segment consisting of contiguous values, without a gap. Thus, [2,3,4] is a sublist of [2,2,3,4,5], but [2,2,4] and [2,4,5] are not.
'''
#error

def sublist(a,b):
    if(len(a)==0):
        return (True)
    c=0
    chk=0
    for i in range(len(b)):
        if(a[c]==b[i]):
            m=i
            for j in range (len(a)):
                if(a[j] != b[m]):
                    chk+=1
                m+=1
        if(chk==0):
            return(True)
        else:
            break
                
    return(False)
#examples:
sublist([2,2,4],[2,2,3,4,5])  #false
sublist([2,2,3],[2,2,3,4,5])  #true

'''
Question 7
Write a Python program that reads input from the keyboard (standard input). The input will consist of some number of lines of text. The input will be terminated by a blank line. Your program should print every third line.

For instance, if the input is the following:

"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then the output should be:

Jack challenged
1 = 0
'''









'''
Question 8
Write a Python function repeated(l) that takes a list of immutable values as argument. 
The function should return the number of values that are repeated in the input list.
For instance, repeated([1,17,22,17,23,17]) should return 1 because only 1 value, 17 is repeated. 
Likewise repeated(["the","higher","you","climb","the","further","you","fall"]) is 2 becaues 2 values, "the" and "you", are repeated.
'''





