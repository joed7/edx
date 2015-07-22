def swapBits( S ):
    if len(S) == 0:
        return ''
    ch=''
    if S[0] == '0':
        ch='1'
    else:
        ch='0'
    return ch+swapBits(S[1:])
        
print swapBits('101011')

def numDivisors( N ):
    l=[]
    for i in range(N):
        num=i+1
        if N % num == 0:
            l.append(num)
    return len(l)

print numDivisors(42)

def cycle( S, n ):
    shift = S[-n:]
    newIndex = len(S)-n
    modstring = S[:newIndex]
    return shift+modstring
print cycle('1110110000', 2)   
