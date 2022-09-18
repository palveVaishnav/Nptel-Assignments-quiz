'''
Question 1
Here is an function to return the minimum value in a list.
There is an error in this function.
Provide an input list for which minbad produces an incorrect output.
# '''
#Incorrect function
def minbad(l):
  mymin = l[-len(l)]
  for i in range(-len(l),-1):
    if l[i] < mymin:
       mymin = l[i]
  return(mymin)

#proof:
#keep minimum value at last element.
print(minbad([6,5,4,3,2,1]))
