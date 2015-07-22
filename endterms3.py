def symmetric(S):
    row = len(S)
    col = len(S[0])
    
    for i in range(row):
        for j in range(col):
            if i < j:
                val1=S[i][j]
                val2=S[j][i]
                if val1 != val2:
                    return False
    return True

print symmetric( [ [1] ] )
print symmetric( [ [1, 42],
                 [42, 5] ] )
print symmetric( [ [1, 42],
                 [1,  1] ] )
print symmetric( [ [1, 2, 3],
                 [2, 4, 5],
                 [3, 5, 6] ] )
