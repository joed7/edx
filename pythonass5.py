import math

def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

#Write sq(x), which takes in a number named x as input. Then, sq should output the square of its input.

def sq(x):
    """ 
        squareroot
    """
    return x ** 2

#interp(low,hi,fraction) takes in three numbers, low, hi, and fraction, and should return the floating-point value that is fraction of the way between low and hi.

def interp(low,hi,fraction):
    return low + (hi-low)*fraction*1.0

#Write a function checkends(s), which takes in a string s and returns True if the first character in s is the same as the last character in s. It returns False otherwise. The checkends function does not have to work on the empty string (the string '').

def checkends(s):
    if len(s)==0:
        return True
    return s[0] == s[-1]

#Write a function flipside(s), which takes in a string s and returns a string whose first half is s's second half and whose second half is s's first half. If len(s) (the length of s) is odd, the first half of the input string should have one fewer character than the second half. (Accordingly, the second half of the output string will be one shorter than the first half in these cases.) There's also a hint after the examples below.


def flipside(s):
    l = len(s)
    if l <= 1:
        return s
    mid = l/2
    #abcde(5,2)
    #if l %2 == 0:
    return s[mid:]+s[:mid]
 #   else:
  #      return s[mid+1:]+s[:mid+1]
     
#Write convertFromSeconds(s), which takes in a nonnegative integer number of seconds s and returns a list (we'll call it L) of four nonnegative integers that represents that number of seconds in more conventional units of time, such that:

def convertFromSeconds(s):
    day = 24*3600
    hour = 3600
    min1 = 60
    L=[]
    L.append(s/day)
    s=s%day
    L.append(s/hour)
    s=s%hour
    L.append(s/min1)
    L.append(s%min1)
    return L
    
    
def front3(str):
    if len(str) < 3:
        return str*3
    cpy=str[:3]
    return cpy*3    
        

  



    
print interp(1.0, 9.0, 0.25) 
print interp(1.0, 3.0, 0.25)
print interp(2, 12, 0.22) 
print interp(24, 42, 0)  
print interp(102, 117, -4.0)     
print  checkends('no match')
print checkends('hah! a match')
print  checkends('q')

print checkends(' ')
print flipside('homework')
print flipside('carpets')
print  convertFromSeconds(610)
print convertFromSeconds(100000)
