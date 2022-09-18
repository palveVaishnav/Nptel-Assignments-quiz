
''''
Question 7
Write a Python program that reads input from the keyboard (standard input). 
The input will consist of an even number of lines of text.
The input will be terminated by a blank line. Suppose there are 2n lines of input.
Your program should print out the last n lines of the input, i.e., the second half of the input,
followed by the first n lines, i.e., the first half of the input.'''



lines=[]
e=input()
while (e):
    lines.append(e)
    e=input()

x=len(lines)+1
s=int(x/2)
for i in range(s,len(lines)):
    print(lines[i])
for i in range(0,s):
    print(lines[i])
    
inputlines = []
inputline = input()
while(inputline):
  inputlines.append(inputline)
  inputline = input()

n = len(inputlines)//2
for i in range(n,len(inputlines)):
  print(inputlines[i])
for i in range(n):
  print(inputlines[i])
  
  
''' Test case:
Despite the negative connotations
surrounding the colloquial term
deepfakes (people don't usually
want to be associated with the
word "fake"), the technology is
increasingly being used
commercially.  More politely
called AI-generated videos, or
synthetic media, usage is growing
rapidly in sectors including
news, entertainment and
education, with the technology
becoming increasingly
sophisticated.  One of the early
commercial adopters has been
Synthesia, a London-based firm
that creates AI-powered corporate
training videos for the likes of
global advertising firm WPP and
business consultancy Accenture.

#output:
news, entertainment and\n
education, with the technology\n
becoming increasingly\n
sophisticated.  One of the early\n
commercial adopters has been\n
Synthesia, a London-based firm\n
that creates AI-powered corporate\n
training videos for the likes of\n
global advertising firm WPP and\n
business consultancy Accenture.\n
Despite the negative connotations\n
surrounding the colloquial term\n
deepfakes (people don't usually\n
want to be associated with the\n
word "fake"), the technology is\n
increasingly being used\n
commercially.  More politely\n
called AI-generated videos, or\n
synthetic media, usage is growing\n
rapidly in sectors including\n
'''





