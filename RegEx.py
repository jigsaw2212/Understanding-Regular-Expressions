import re

#A pattern can be matched using regEx as follows
#re.search(pattern, string)

name = 'I am Divyansh Agarwal'

match = re.search(r'Div\w\w',name) #a .  wouldve also worked here
print match.group()
#re.search returns a match object
#The r at the start of the pattern string denotes a python "raw" string. Make it a habit
#object.group() is used to return the matched string


#Basic patterns
'''
--> . - matches any single character except for \n

--> \w - matched a word character, meaning a letter (a-z or A_Z), letter (0-9) or undescore (_)

--> \W - refers to any non word character

--> \s - matches a single whitespace character- space, new line, return, tab, form.

--> \S -  matches a single non-whitespace character

--> \t,\n,\f - tab, newline, form

--> ^= - matches the start of a string

--> $= - matches the end of the string

--> \ - inhibit specialness of the character; If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character.

--> \d - matches a decimal digit

'''

#Search for pattern iii in string piiig.
#On success, match.group() is the matched text.

match = re.search(r'iii','piiig')
print match.group()

match = re.search(r'..g','piiig')
print match.group()

##\d - digit character, \w - word character
match = re.search(r'\d\d\d','p123ig')
print match.group()

match = re.search(r'\w\w\w.','@@abcd!!')
print match.group()


#REPETITIONS:-
'''
+ - one or more occureneces to the left
* - zero or more occurences to the left
? - zero or one occurrence to the left

'''

##i+ = one or more i's, as many as possible

match = re.search(r'pi+','piiig')
print match.group()
#means p and then any number of i's (one or more)

#p followed by zero or more number of i's
match = re.search(r'pi*','pndkdg')
print match.group() 

#It first finds the leftmost solution for the pattern and within it drives the +  as far as possible

match = re.search(r'i+','piigiiii')
print match.group()
#Note that it doesn't get to the second set of i's

#\s* = zero or more white spaces
#Look at the 3 next examples. Of 3 digits with zero or more white spaces between them at two places
match = re.search(r'\d\s*\d\s*\d','xx1 2    3xx')
print match.group()

match = re.search(r'\d\s*\d\s*\d','xx12   3xx')
print match.group()

match = re.search(r'\d\s*\d\s*\d','xx123xxx')
print match.group()

##^ matches the start of the string
match = re.search(r'b\w+','foobarndcndsk') 
print match.group()
#Means b and then any number of characters



str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print match.group() 

str = 'purple al.i--c.e-b@google.c.o-m monkey dishwasher'
match =  re.search(r'[\w.-]+@[\w.-]+', str)
print match.group() 

#[] square brackets mean 'or'
#[abc] means a or b or c
#[^ab] means any character except a or b
#[a-z] specifies a range. This means all lower case characters from a to z



#Paranthesis () are used to introduce logical groups into pattern matching and help us to pick out parts of the matching text

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.]+)', str)
print match.group(1)
print match.group(2)
print match.group()
#group(1) prints the first part
#group(2) prints the second part
#group() still prints the whole part 

#NOTE: Sometimes there may be parenthesis in the string, which we wish to preserve and hence we will write parenthesis like (?:), with a '?:' at the start. The left parenthesis then will not count as a group result
#Adding '?:' at the end will make the search non-greedy.
#Eg. r'(<.?:>)' will stop at the first right side tag it encounters and won't go to check further



#Other options you can give re function to modify the behaviour of pattern match. The optional flag is given as an extra argument to seach() or findall() function.
#1. re.se.arch(pat, string, re.IGNORECASE) #so that 'a' matches 'A'
#2. re.search(pat, string, re.DOTALL) #allows (.) to match newline as well 
#3. #Within a string made of multiple lines, this allows ^ and $ to match the start and end of each line



















