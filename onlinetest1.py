def decreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(
       # Complete the recursive call below this line
# False if l[0]<l[1] else decreasing(l[1:])
l[0]>l[1] and decreasing(l[1:])
    	
  
       # Complete the recursive call above this line
    )

print(decreasing([83,59,44,44,23,19]))


'''
import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "decreasing":
  arg = tolist(farg)
  print(decreasing(arg))

#answer:
def decreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(
       # Complete the recursive call below this line
           l[0] > l[1] and decreasing(l[1:])
       # Complete the recursive call above this line
    )

def median3(x,y,z):
  if x <= y:
    if x >= z:
       mymedian = x
  # Your code below this line

    # for x
  if(x>=y and x <= z):
    return(x)
  #if(x<=y and x >= z):
    #return(x)
  #for y
  if(y>=x and y<=z):
    return(y)
  if(y<=x and y>=z):
    return(y)
  #for z
  if(z<=x and z>=y):
    return(z)
  if(z>=x and z<=y):
    return(z)
  # Your code above this line
  return(mymedian)
 
import ast

def totripleint(inp):
  inp = "[" + inp + "]"
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "median3":
  arglist = totripleint(farg)
  print(median3(arglist[0],arglist[1],arglist[2]))



def sum3cubes(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if( i*i*i + j*j*j + k*k*k  == n):
                    return(True)
    return(False)
#ans
# extra cube function is decleared 
def sum3cubes(n):
    for i in range(1,n-1):
        for j in range (1,n-i):
            k = n - (i+j)
            if cube(i) and cube(j) and cube(k):
                return(True)
    return(False)

# Question 6
# Write a Python function uncommon(l1,l2) that takes two lists sorted in ascending order as arguments and returns the list of all 
# elements that appear in exactly one of the two lists. The list returned should be in ascending order.
#  All such elements should be listed only once, even if they appear multiple times in l1 or l2.

# Thus, uncommon([2,2,4],[1,3,3,4,5]) should return [1,2,3,5] while uncommon([1,2,3],[1,1,2,3,3]) should return [].

def uncommon(a,b):
  a=set(a)
  b=set(b)
  r=(a^b)
  r=list(r)
  r.sort
  return(r)

def aboveaverage(l):
    p=[]
    s=[]
    for a,b in l:
        p.append(a)
        s.append(b)
    #average score:
    tavg=0
    sp=set(p)
    sp=list(sp)
    for i in range(len(s)):
        tavg=tavg+s[i]
    tavg=(tavg/len(s))


    inavg=[]
    insum=0
    n=0
    #individual average
    for i in range(len(p)):
        for j in range(len(p)):
            if(p[i]==p[j]):
                insum=insum+s[j]
                n+=1
        if(n==0):
            inavg.append(s[i])
        else:
            inavg.append(insum/n)
        insum=0
        n=0
    final=[]
    for i in range(len(p)):
        if(inavg[i]>=tavg):
            final.append(p[i])


    # print(final)
    # for i in range(len(final)):
    #     for j in range(len(final)):
    #         if(final[i]==final[j]):
    #             final.remove(final[j])
    final=set(final)
    final=list(final)

    
    return sorted(final)

# print(aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',100),('Pujara',25),('Pujara',35),('Ashwin',109)]))
# print(aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',69),('Pujara',102),('Pujara',40),('Ashwin',109)])
print(aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',69),('Pujara',102),('Pujara',40),('Ashwin',109)]))

'''
'''
def aboveaverage(l):
  aggregate = {}
  innings = {}
  totalscore = 0
  totalinnings = 0
  for (name,score) in l:
    totalscore += score
    totalinnings += 1
    try:
      aggregate[name] += score
      innings[name] += 1
    except KeyError:
      aggregate[name] = score
      innings[name] = 1

  overallaverage = totalscore/totalinnings

  aboveaverage = []
    
  for name in aggregate.keys():
    average = aggregate[name]/innings[name]
    if average >= overallaverage: 
      aboveaverage.append(name)
      
  return(sorted(aboveaverage))
    
import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "aboveaverage":
  arg = tolist(farg)
  print(aboveaverage(arg))


# Write a Python program that reads input from the keyboard (standard input).
#  The input will be terminated by a blank line. The lines are numbered 0,1,2,… 
#  Your program should print out the even numbered lines followed by the odd numbered 
#  lines. In other words, first print lines 0,2,4,… then lines 1,3,5,…

inputlines = []
inputline = input()
while(inputline):
  inputlines.append(inputline)
  inputline = input()

for i in range(0,len(inputlines),2):
  print(inputlines[i])
for i in range(1,len(inputlines),2):
  print(inputlines[i])
  '''
