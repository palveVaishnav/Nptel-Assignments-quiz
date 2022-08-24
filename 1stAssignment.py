
# question one
# what is the value of h(27993)  ???
def h(x):
    (d,n) = (1,0)
    while d <= x:
        (d,n) = (d*3,n+1)
    return(n)

y=h(27993)
print(y)


# QUETION TWO: what is g(60)-g(48)
def g(n): 
    s=0
    for i in range(2,n):
        if n%i == 0:
           s = s+1
    return(s)

ans=g(60)-g(48)
print(ans)

# QUESTION THREE : the ans should be true for ???

def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)

v=f(4)
print(v)
print("true only when the input is a perfect square")

def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))

k=foo(5)
print(k)
print("It returns n*(n+1)/2 if the input is non-negative")


# Week 1 Quiz
# Due date: 2022-08-10, 23:59 IST.
# Your last recorded submission was on 2022-07-29, 15:12 IST
# All questions carry equal weightage. 
# All Python code is assumed to be executed using Python3.
#  You may submit as many times as you like within the deadline
# . Your final submission will be graded.
# Note:

# If the question asks about a value of type string,
#  remember to enclose your answer in single or double quotes.
# If the question asks about a value of type list,
#  remember to enclose your answer in square brackets and use commas to separate list items.
# What does h(27993) return for the following function definition?

# def h(x):
#     (d,n) = (1,0)
#     while d <= x:
#         (d,n) = (d*3,n+1)
#     return(n)
# 10
# 2.5 points
# What is g(60) - g(48), given the definition of g below?

# def g(n): 
#     s=0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+1
#     return(s)
# 2
# 2.5 points
# 2.5 points
# Consider the following function f.

# def f(n): 
#     s=0
#     for i in range(1,n+1):
#         if n//i == i and n%i == 0:
#            s = 1
#     return(s%2 == 1)
# The function f(n) given above returns True for a positive number n if and only if:

#  n is an odd number.
#  n is a prime number.
#  n is a perfect square.
#  n is a composite number.
# 2.5 points
# Consider the following function foo.

# def foo(m):
#     if m == 0:
#       return(0)
#     else:
#       return(m+foo(m-1))
# Which of the following is correct?

#  The function always terminates with foo(n) = factorial of n
#  The function always terminates with foo(n) = n(n+1)/2
#  The function terminates for non­negative n with foo(n) = factorial of n
#  The function terminates for non­negative n with foo(n) = n(n+1)/2
#  You may submit any number of times before the due date.
#  The final submission will be considered for grading.