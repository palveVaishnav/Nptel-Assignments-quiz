'''
Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where

minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order
Here are some examples of how your function should work.

>>> frequency([13,12,11,13,14,13,7,11,13,14,12])
([7], [13])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
([7], [13, 14])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
([7, 11, 12], [13, 14])


>>> frequency([1,1,1,1,1,1,1])
([1],[1])

'''

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
    linearsort(listmin)
    linearsort(listmax)
        

    return(listmin,listmax)


    # print(listmin)
    # print(listmax)



# print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))

