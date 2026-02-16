import numpy as np

def global_alignment(sequence1,sequence2):
    n=len(sequence1)
    m=len(sequence2)
    j=2
    k=2
    s1=-2
    s2=-2
    matrix=np.zeros((m+2,n+2))
    for i in range(n):
        #matrix[0][j]=sequence1[i]
        matrix[1][j]=s1
        j+=1
        s1-=2

    for i in range(m):
        #matrix[k][0]=sequence2[i]
        matrix[k][1]=s2
        k+=1
        s2-=2
        path=[()]
    for i in range(2,m+2):
        for j in range(2,n+2):
            if sequence2[i-2]==sequence1[j-2]:
                a=matrix[i-1][j-1]+1
                b=matrix[i][j-1]-2
                c=matrix[i-1][j]-2
                matrix[i][j]=max(a,b,c)
                path.append((i,j))
            else:
                a=matrix[i-1][j-1]-1
                b=matrix[i][j-1]-2
                c=matrix[i-1][j]-2
                matrix[i][j]=max(a,b,c)
                path.append()
            

    print(matrix)
    print(path)

global_alignment("ATGCT","AGCT")

