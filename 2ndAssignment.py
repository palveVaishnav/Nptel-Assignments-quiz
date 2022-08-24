"""
Write a function intreverse(n) that takes as input a positive integer n and 
returns the integer obtained by reversing the digits in n.
Here are some examples of how your function should work.

>>> intreverse(783)
387
>>> intreverse(242789)
987242
>>> intreverse(3)
3


def intreverse(number):
    reverse=0
    
    while(number>0):
        reverse=(reverse*10)+(number%10)
        number=number//10
    
    return reverse
"""

# reverse the number

def  intreverse(num):
    if(num<0):
        print("ENter a +ve number")
        return
    reverse=0
    while(num>0):
        reverse=(num%10) + (reverse*10)
        num=num//10
    
    return reverse

print(intreverse(-5362))




"""
Write a function str(s) that takes as input a string s and checks if the 
brackets "(" and ")" in s are str: that is, every "(" has a matching ")" 
after it and every ")" has a matching "(" before it. 
Your function should ignore all other symbols that appear in s.
 Your function should return True if s has str brackets and False if it does not.

Here are some examples to show how your function should work.

 

>>> str("(7)(a")
False
>>> str("a)*(?")
False
>>> str("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True
"""
list1 = ["("]
list2 = [")"]
def matched(str):
	stk = []
	for i in str:
		if i in list1:
			stk.append(i)
		elif i in list2:
			pos = list2.index(i)
			if ((len(stk) > 0) and
				(list1[pos] == stk[len(stk)-1])):
				stk.pop()
			else:
				return False
	if len(stk) == 0:
		return True
	else:
		return False

"""
Write a function sumprimes(l) that takes as input a list of integers l 
and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

>>> sumprimes([3,3,1,13])
19
>>> sumprimes([2,4,6,9,11])
13
>>> sumprimes([-3,1,6])
0
"""


from math import sqrt

def primechk(numtocheck) :
 
    if numtocheck <= 1 :
        return False
 
    for i in range(2, int(sqrt(numtocheck)) + 1) :
 
        if numtocheck % i == 0 :
            return False
 
    return True

def sumprimes(l):
    sum=0
    for i in range(0,len(l)):
        if(primechk(l[i])):
            sum=sum + l[i]
    
    return sum
