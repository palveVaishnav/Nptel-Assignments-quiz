'''
1)Write a function contracting(l) that takes as input a list of
integer l and returns True if the absolute difference between
each adjacent pair of elements strictly decreases.

Here are some examples of how your function should work.

  >>> contracting([9,2,7,3,1])
  True

  >>> contracting([-2,3,7,2,-1]) 
  False

  >>> contracting([10,7,4,1])
  False

'''
# question one 
def contracting(l):
  if(len(l)==0):
    return True
  diff= abs( l[1]-l[0])
  for i in  range(1,len(l)-1):
    if(abs(l[i]-l[i+1]) < diff):
      diff=abs(l[i]-l[i+1])
    
    else:
      return  False
  return True




'''
def contracting(l):
  if(len(l)== 0):
    return False
  i=0
  while(i  <  len(l)-2):
    if(abs(l[i-1]-l[i] ) ==   abs( l[i+1] - l[i])):

      return False
    elif(abs(l[i-1]-l[i] ) <   abs( l[i+1] - l[i])):
      return False
    else:
      i = i+1

  return True
'''

# print(contracting([9,2,7,3,1]),contracting([-2,3,7,2,-1]), contracting([10,7,4,1]))
# print(contracting([]))
# t f f 

'''

def leftrotate(m):
    l = len(m)
    # arr = []
    arr=[ [0 for i in (0,len(m))]  for i in (0,len(m))]

    for i in range(0,len(m)-1):
        # sub_arr = []
        for j in range(0,len(m)-1):   
            arr[i][j]=m[len(m)-1-i][len(m)-1-j]
            # sub_arr.append(m[j][(l-1)-i])
        # arr.append(sub_arr)
    return arr

'''



def leftrotate(m):

  # size=len(m)-1
  i=0
  while(i<len(m)-1):
    for j in (0,len(m)-1):
      
      temp=m[i][j]
      m[i][j]=m[j][i]
      m[j][i]=temp
    i+=1

  for i in (0 ,len(m)-1):
    temp2=m[i]
    m[i]=m[len(m)-1]
    m[len(m)-1]=temp2

  return m

print(leftrotate([[1,2,3], [4,5,6], [7,8,9]]))


def counthv(l):
  hill=0
  valley=0
  for i in (1,len(l)-2):
    if(l[i] > l[i+1] and l[i] > l[i-1]):
      hill += 1
    if(l[i] < l[i+1] and l[i] < l[i-1]):        
      valley += 1
  
  return [hill,valley]

print(counthv([1,2,1,2,3,2,1]))
# [2, 1]

print(counthv([1,2,3,1]))
# [1, 0]

print(counthv([3,1,2,3]))
# [0, 1]




'''
2) In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than
its neighbours and a valley if it is strictly less than its neighbours.
Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,second] wherefirst is the number
of hills in l and second is the number of valleys in l. 

3)A square nxn matrix of integers can be written in Python as a list with n 
elements, where each element is in turn a list of n integers, representing 
a row of the matrix. For instance, the matrix
Write a function leftrotate(m) that takes a list representation m of a square
matrix as input, and returns the matrix obtained by rotating the original matrix 
counterclockwize by 90 degrees. For instance.


  1  2  3
  4  5  6
  7  8  9

=>
  3  6  9
  2  5  8    
  1  4  7


Your function should not modify the argument m provided to the function rotate().

Here are some examples of how your function should work.

 
  >>> leftrotate([[1,2],[3,4]])
  [[2, 4], [1, 3]]
  
  
  >>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
  
  leftrotate([[1,1,1],[2,2,2],[3,3,3]]) 
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

'''


