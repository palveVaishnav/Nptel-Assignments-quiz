'''
Question 3
Here is a function to compute the third largest value in a list of distinct integers.
All the integers are guaranteed to be positive. 
You have to fill in the missing lines. 
You can assume that there are at least three numbers in the list.
'''

def thirdmax(l):
  (mymax,mysecondmax,mythirdmax) = (0,0,0)
  for i in range(len(l)):
  # Your code below this line

    for j in range(0,len(l)-1):
      if(l[j]>l[j+1]):
        (l[j],l[j+1])=(l[j+1],l[j])
    
  return (l[-3])
  # Your code above this line
  return(mythirdmax)

thirdmax([3,1,2])
thirdmax([13,12,2,17,3,6,8,5,18,16,22])
thirdmax([10,1,8,2,0])
thirdmax([10,20,30,40]) 
          

