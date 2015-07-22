def indexNearest42( L ):
    modL = [x-42 for x in L]
    absL = [abs(y) for y in modL]
    minV = min(absL)
    return absL.index(minV)

print indexNearest42([43,44,40])

def longestDNA( s1 ):
    s=0
    e=0
    index = 0
    exisiting = False
    longest =-1
    (fs,fe)=(-1,-1)
    for i in s1:
        if i in 'ACGT':
            if exisiting == False:
                s=index
                e=index
                exisiting =True    
            else:
                e=index
                
        else:
            if exisiting == True:
                exisiting=False
                    
                l=e-s
                if l > longest:
                    (fs,fe)=(s,e)   
                    longest=l         
        index = index+1    

    if exisiting == True:
        l=e-s
        if l >longest:
            (fs,fe)=(s,e)        
                	
    return s1[fs:fe+1]

print longestDNA( 'A' )
