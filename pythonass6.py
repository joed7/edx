def mult( n, m ):
    if m < 0:
        m=m*-1
        n=n*-1
    if m == 0:
        return 0
    else:
        return n + mult(n,m-1)



def dot(L,K):
    if len(L) != len(K):
        return 0.0
    if len(L) == 0:
        return 0.0
    return (L[0]*K[0])+(dot(L[1:],K[1:]))



#Write ind(e, L), which takes in a sequence L and an element e. L might be a string or, more generally, a list. Your function ind should return the index at which e is first found in L. Counting begins at 0, as is usual with lists. If e is NOT an element of L, then ind(e, L) should return the integer equal to len(L). Here are a few examples:

def ind(e,L):
    if len(L) == 0:
        return 0
    if(e == L[0]):
        return 0
    return 1 + ind(e,L[1:])
        

def letterScore( let ):
    if let in 'qz':
        return 10
    
    if let in 'aeilnorstu':
        return 1
    if let in 'dg':
        return 2
    if let in 'bcmp':
        return 3
    if let in 'fhvwy':
        return 4
    if let in 'jx':
        return 8
    if let == 'k':
        return 5
    return 0

def scrabbleScore(s):
    if len(s) == 0:
        return 0
    return letterScore(s[0])+scrabbleScore(s[1:])

def one_dna_to_rna( c ):
    """ converts a single-character c from DNA
        nucleotide to complementary RNA nucleotide """
    if c == 'A': return 'U'
    if c == 'C': return 'G'
    if c == 'G': return 'C'
    if c == 'T': return 'A'
    return ''
    # you'll need more here...

def transcribe(s):

    if len(s) == 0:
        return ''
    return one_dna_to_rna(s[0])+transcribe(s[1:])
        
#
# Tests
#
print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)

print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] ) 
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] ) 
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] ) 
print "dot( [], [6] )           0.0 ==", dot( [], [6] ) 
print "dot( [], [] )            0.0 ==", dot( [], [6] ) 

print "ind( 42, [ 55, 77, 42, 12, 42, 100 ])  2 ==", ind( 42, [ 55, 77, 42, 12, 42, 100 ])
print "ind(42, range(0,100))                  42 ==", ind(42, range(0,100))
print "ind('hi', [ 'hello', 42, True ])       3 ==", ind('hi', [ 'hello', 42, True ])
print "ind('hi', [ 'well', 'hi', 'there' ])   1 ==", ind('hi', [ 'well', 'hi', 'there' ])
print "ind('i', 'team')                       4 ==", ind('i', 'team')
print "ind(' ', 'outer exploration')          5 ==", ind(' ', 'outer exploration')

print "scrabbleScore('quetzal'):  25 ==", scrabbleScore('quetzal')
print "scrabbleScore('jonquil'):  23 ==", scrabbleScore('jonquil')
print "scrabbleScore('syzygy'):   25 ==", scrabbleScore('syzygy')
print "scrabbleScore('abcdefghijklmnopqrstuvwxyz'):  87 ==", scrabbleScore('abcdefghijklmnopqrstuvwxyz')
print "scrabbleScore('?!@#$%^&*()'):  0 ==", scrabbleScore('?!@#$%^&*()')
print "scrabbleScore(''):          0 ==", scrabbleScore('')

print "transcribe('ACGT TGCA'):  'UGCAACGU' ==", transcribe('ACGT TGCA')
print "transcribe('GATTACA'):     'CUAAUGU' ==", transcribe('GATTACA')
print "transcribe('cs5') :               '' ==", transcribe('cs5')
print "transcribe('') :                  '' ==", transcribe('')

