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

'''



def frequency(l):
    newl=list(set(l))
    # print(newl)
    freqlist=[]
    for i in range(len(newl)):
        freqlist.append(0)

    x=0
    for a in newl:
        for i in range(len(l)):
            if(a == l[i]):
                freqlist[x]=freqlist[x] + 1

        x += 1
    
    # print(freqlist)
    fmin=min(freqlist)
    fmax=max(freqlist)
    # print(fmin,fmax)
    listmin=[]
    listmax=[]

    for i  in range(len(freqlist)):
        if(fmin == freqlist[i]):
            listmin.append(newl[i])
        elif(fmax == freqlist[i]):
            listmax.append(newl[i])

    return(listmin,listmax)
    # print(listmin)
    # print(listmax)



print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))