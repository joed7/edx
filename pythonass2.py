# python 2
#
# Homework 8, Problem 1
# Loops!
#
# Name:
#
import random
def fac(n):
    """ loop-based factorial function 
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

def power(b,p):
    if p == 0:
        return 1
    
    i=1
    j=1
    while j<=p:
        i=i*b
        j=j+1
    return i

def summedOdds(L):
    i=0
    j=len(L)
    sum1=0
    while i<j:
        if (L[i] %2 != 0):
        	sum1= sum1+L[i]
        i=i+1		
    return sum1

def untilARepeat( high ):
    l=[]
    cnt=0
    while uniq(l) == True:
    #	print l
        num=random.choice(range(0,high))
        l.append(num)
        cnt=cnt+1
    return cnt		
def uniq( L ):
    """ returns whether all elements in L are unique
        input: L, a list of any elements
        output: True, if all elements in L are unique,
             or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return uniq( L[1:] ) # recursion is OK, too!

print untilARepeat( 365 )
L = [ untilARepeat( 365 ) for i in range(1000) ]

