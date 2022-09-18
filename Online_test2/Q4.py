'''Question 4
Recall that the positions in a list of length n are 0,1,…,n-1.
We want to write a function mod3pos(l) that returns the elements at all positions in l that are divisible by 3. 
In other words, the function should return the list [l[0],l[3],...]. 
For instance mod3pos([]) == [], mod3pos([7]) == [7], mod3pos([8,11,8,11]) == [8,11] and mod3pos([19,3,44,44,3,19,17,23]) == [19,44,17].
A recursive definition of mod3pos is given below. You have to fill in the missing argument for the recursive call.

def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return(...)
  '''
def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return(
       # Complete the recursive call below this line
        [l[0]] + mod3pos(l[3:])
       # Complete the recursive call above this line
    )
mod3pos([0,1,2,3,4,5,6,7,8,9])
mod3pos([19,23,14,11,12,17,6,4,23,44,55,77])
mod3pos([2])
mod3pos([0,1,2])
