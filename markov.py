import random

def createDictionary( filename ):
    file1= open(filename,'r')   
    dict1={}
#    txt = file1.read().split()
    for j in range(1):
        content = file1.read().split()
        prevEnd = True 
        words = len(content)
        start=0
        prev='$'
        while start < len(content):
            if prev not in dict1:
                dict1[prev]=[ content[start] ]
            else:
                dict1[prev].append(content[start])
    
            if isLast(content[start]):
                prev='$'
            else:
                prev=content[start]
            start=start+1
    return dict1

def isLast(string):
    if string[-1] in '!.?':
        return True
    return False

def generateText( d, n ):
    prevFist = True 
    prev='$'   
    col=[]
    for i in range(n):
        val = d[prev]
        word = random.choice(val)
        col.append(word)
        prevFist =False
        prev = word
        if isLast(word):
            prevFist = True
            prev = '$'
            
    return col        
            


d=createDictionary( 't.txt' )
print d 
print generateText(d,20)        
