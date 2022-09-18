'''
Question 6
Write a Python function disjointlist(l1,l2) that takes two lists as arguments and 
returns True if the two lists are disjoint, otherwise returns False.
Two lists are said to be disjoint if there is no element that common to both the lists. 
For instance, [2,2,3,4,5] and [6,8,8,1] are disjoint, while [1,2,3,4] and [2,2] are not.'''


def disjointlist(a,b):
    x=set(a)
    y=set(b)

    z= x & y
    z=list(z)
    if(len(z)>0):
        return False
    else:
        return True
'''
#Alternate
def disjointlist(l1,l2):
  s1 = set(l1)
  s2 = set(l2)
  return(s1 & s2 == set())
'''


disjointlist([2,2,3,4,5],[6,8,8,1])
# True
disjointlist([1,2,3,4],[2,2])
#  False
disjointlist([1,2,3,4],[])
#  True	
disjointlist([1,4,1,1],[2,2,3,3])
# True
