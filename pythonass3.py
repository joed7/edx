import random
import math
def dartThrow():
    x= random.uniform(-1.0,1.0)
    y= random.uniform(-1.0,1.0)    
    dist = x**2 + y**2
    
    if dist < 1:
        return True
    return False

def forPi( n ):
    count=0
    i=1
    while i <= n:
        if dartThrow() == True:
            count=count+1
            
        print str(count)+ ' hits out of '+ str(i)+ ' throws so that pi is '+ str(4.0*count/i)
        i=i+1
    return 4.0*count/n

def whilePi( maxerror ):

    nThrows = 0
    nHits = 0
    e=0
    p=math.pi
    diff = abs(e - p) 
   
    while  diff > maxerror:
        if dartThrow() == True:
            nHits=nHits+1
        nThrows=nThrows+1
        print str(nHits)+ ' hits out of '+ str(nThrows)+ ' throws so that pi is '+ str(4.0*nHits/nThrows)
        e=4.0*nHits/nThrows
        diff = abs(e - p) 
    return nThrows
forPi(10)
whilePi( 0.1 )
