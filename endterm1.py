import math

def isPrime(n):
    count=0
    i=1
    cutoff = int(math.sqrt(n))
    while i <= cutoff:     
  #  for i in range(int(math.sqrt(n))):
        if n % (i) == 0:
            count=count+1
        i=i+1
    if count ==1:
        return True
	
    return False
#for i in range(15):
#    print str(i) +" "+ str(isPrime(i))


def addPrimes(L):
    if len(L) == 0:
        return 0
    val = L[0]
    sum1=0
    if isPrime(val) == True:
        sum1=sum1+val
    return sum1+addPrimes(L[1:])    

print addPrimes(range(7)[2:])

a={}
def uniquify(L):
    if len(L) == 0:
        a.clear()
        return []
    t=[]    
    if L[0] not in a:
        a[L[0]]=1
        t.append(L[0])
    t=t+uniquify(L[1:])
    return t

print uniquify([ 42, 'spam', 42, 5, 42, 5, 'spam', 42, 5, 5, 5 ])
print uniquify( range(4) + range(3))
print uniquify([2])
print uniquify([4,4])
