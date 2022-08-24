def linearsort(l):

    for i in range(len(l)-1):
        for j in range(i,len(l)-1):
            if(l[j]>l[j+1]):
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
    return(l)



def frequency(l):
    # creating a set of the given list  and convert thet set to a list so that we will have a list using which we will compare
    # provided list and count the frequencies of every element.
 
    newl=list(set(l))
    # print(newl)
    # create a list with same length as of the set list we will use this list to store the frequencies of 
    # corresponding elements present in the set list.
    freqlist=[]
    # initialize all positions to 0.
    for i in range(len(newl)):
        freqlist.append(0)

    # A for loop to count the frequencies of elements in the given list using the set list and storing the frequencies 
    # in the frequency list 
    x=0
    for a in newl:
        for i in range(len(l)):
            if(a == l[i]):
                freqlist[x]=freqlist[x] + 1

        x += 1
    
    # print(freqlist)
    # finding the minimum and maximum frequencies from the frequency list.
    fmin=min(freqlist)
    fmax=max(freqlist)

    # initilizing lists to store the minimum and maximum elements in the given list
    listmin=[]
    listmax=[]
    # storing the elements with corresponding minimum and maximum frequencies in the lists to return.
    for i  in range(len(freqlist)):
        if(fmin == freqlist[i]):
            listmin.append(newl[i])
        elif(fmax == freqlist[i]):
            listmax.append(newl[i])
            
    # when all elements are same
    # the function may fail when all elements are same ,i.e it will return either a minimum or a maximum list so 
    # this will make the function to return the list containing atleast one element 
    # in this case, ass all elements are same then min and max will be the same element( present at every index )

    if(len(listmax)== 0 ):
        listmax.append(newl[0])

    elif( len(listmax)==0):
        listmin.append(newl[0])

    # the lists to be returned need to be sorted in ascending order ,although they are sorted but for surity 
    # linearsort(listmin)
    # linearsort(listmax)
        

    return(linearsort(listmin),linearsort(listmax))
  

def onehop(l):
    hoplist=[]
    for a, b in l:
       for c,d in l:
        if( b == c and a !=d ):
            toappend=(a,d)
            hoplist.append(toappend)
    

    hoplist.sort()
    hoplist=list(set(hoplist))

    # we need to sort the list obtained so far
    # find the smallest element and append it in the new 
    if(len(hoplist)>1 and len(hoplist) != 0):
        nhoplist=[]
        for a,b in l:
            hopmin=min(hoplist)
            nhoplist.append(hopmin)
            hoplist.remove(hopmin)

        #if((4,3) in l):
         #   nhoplist.append(hoplist[0])

        return(nhoplist)

    return(hoplist)



print(frequency([1,1,1,1,1]))
print(frequency([4,4,4,1,1,2,2,2,3,3]))
print(frequency([1,2,3,4,5,5,4,3,2,3,4,5,5,4,5]))
print(onehop([(1,2)]))
print(onehop([(1,2),(2,1)]))
print(onehop([(1,3),(1,2),(2,3),(2,1),(3,2),(3,.1)]))


'''
Public Test Cases	Input	Expected Output	Actual Output	Status
Test Case 1	
frequency([1,2,3,4,5,5,4,3,2,3,4,5,5,4,5])
([1], [5])\n
([1], [5])\n
Passed
Test Case 2	
frequency([4,4,4,1,1,2,2,2,3,3])
([1, 3], [2, 4])\n
([1, 3], [2, 4])\n
Passed
Test Case 3	
frequency([1,1,1,1,1])
([1], [1])\n
([1], [1])\n
Passed
Test Case 4	
onehop([(1,2),(2,1)])
[]\n
[]\n
Passed
Test Case 5	
onehop([(1,2)])
[]\n
[]\n
Passed
Test Case 6	
onehop([(1,3),(1,2),(2,3),(2,1),(3,2),(3,1)])
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]\n
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]\n
'''
