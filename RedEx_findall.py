#findall() function for regular expressions finds all the matches of the desrired pattern in a string, and returns them as a list of strings
#findall automatically does the iteration
import re

#Suppose we have a list with many email addresses

str = 'purple alice-b@google.com, blah monkey bob@abc.com blah dishwasher'

emails=[]

emails = re.findall(r'[\w.-]+@[\w.-]+', str)
print emails

#How about :-
 
emails = re.findall(r'([\w.-]+)@([\w.-]+)',str) 
#Will return tuples
for name in emails:
    print name[0] #to access the part one of each tuple
    print name[1] #t0 access part 2 of each tuple
#Will give an output like:- 
#('alice-b', 'google.com')
#('bob', 'abc.com')

#----------------------------------------------------------------

#Just something I discovered while fooling around in Python, probably the easiest way of pattern searching. Yet to explore this fully.
if 'c' in 'abcdecf':
    print 'hello'
#WORKS! Python, you are magic! *_*

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
