def median(L):
    mod=L.sort()
    if len(L) %2 == 0:
        mid1=len(L)/2
        mid2=mid1-1
        return (L[mid1]+L[mid2])*1.0/2
    return L[len(L)/2]
	
print  median( [ 1.0, 100.0, 2.0 ] )
print median( [ 1.0, 100.0, 2.0, 3.0 ] )
