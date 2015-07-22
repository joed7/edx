# python 2
# 
# Name:
#
# Homework 2, Problem 1
# slicing and indexing challenges
#

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]     
print answer0

# Problem 1:
# Creating the list [7,1] from pi and e
answer1 =e[1:]    
print answer1

#Use pi and/or e to create the list [9,1,1]. Store this list in the variable answer2.
answer2=[e[0]+e[1]]+[e[2]]+[e[2]]

print answer2

#Use pi and/or e to create the list [1,4,1,5,9]. Store this list in the variable answer3.
answer3=pi[1:]
print answer3

#Use pi and/or e to create the list [1,2,3,4,5]. Store this list in the variable answer4
answer4= [e[2]]+[e[0]]+[pi[0]]+[pi[2]]+[pi[4]]
print answer4

# starting strings for Homework 1

h = 'harvey'
m = 'mudd'
c = 'college'

answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5

#Create 'collude' and store this string in the variable answer6. (our best: 5 ops.)

answer6=c[:4]+m[1:3]+c[-1]
print answer6

#Create 'arveyudd' and store this string in the variable answer7. (our best: 3 ops.)
answer7=h[1:]+m[1:]
print answer7

#Create 'hardeharharhar' and store this string in the variable answer8. (our best: 8 ops.)
answer8=h[:3]+m[-1]+c[-1]+h[:3]+h[:3]+h[:3]
print answer8

#Create 'legomyego' and store this string in the variable answer9. (our best: 8 ops.)
ego=c[4:6]+c[1]
answer9=c[2]+ego+m[0]+h[-1]+ego
print answer9

#Create 'clearcall' and store this string in the variable answer10. (our best: 8 ops.)
answer10=c[0]+c[3:5]+h[1:3]+c[0]+h[1]+c[2:4]
print answer10
