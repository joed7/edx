# python 2
#
# Homework 3, Problem 2
#
# Name:
#

import random  


def rs():
    """ rs chooses a random step and returns it 
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])


def rs1(start):
    """ rs chooses a random step and returns it 
        note that a call to rs1() requires parentheses
        inputs: none at all!
    """
    return random.choice([start-1,start+1])

def rwpos( start, nsteps ):
    if nsteps == 0:
        return start
    print 'start is ' + str(start)
    return rwpos(rs1(start),nsteps-1)
    
def rwposPlain( start, nsteps ):
    if nsteps == 0:
        return start
#    print 'start is ' + str(start)
    return rwposPlain(rs1(start),nsteps-1)
    
def ave_signed_displacement( numtrials ):
    LC = [ rwposPlain(0,100) for x in range(numtrials) ]
    return sum(LC)*1.0/len(LC)

def ave_squared_displacement( numtrials ):
    LC = [ rwposPlain(0,100) for x in range(numtrials) ]
    LCSquared = [l ** 2 for l in LC]
    return sum(LCSquared)*1.0/len(LCSquared)

    

def rwsteps( start, low, hi ):
    if start == low or start == hi:
        return 0
    diff1 = start-low
    diff2 = hi-start
    print '|'+' '*(diff1-1)+'S'+' '*(diff2-1)+'|'
    return 1+ rwsteps(rs1(start),low,hi)

#print rwpos( 40, 4 )
print rwsteps( 10, 5, 15 )

