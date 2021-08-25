# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import warnings
import numpy as np

def fill_right(row,pos):
    #dir=0 for horizontal, 1 for vertical:
    left=0
    right=0
    j=pos
    while j+right<len(row)-1 and row[j+right+1]!='#':
        right+=1
    while j-left>0 and row[j-left-1]!='#':
        left+=1

    if row[j+right-left]=='.':
        row[j + right - left] = row[j]
        indicator=1
    elif row[j+right-left]==row[j]:
        indicator=0
    else:
        warnings.warn('Table is not possible')

    return([row,indicator, j+right-left])

def fill(matrix):
    n=len(matrix)
    m=len(matrix[0])
    interesting_positions=[]
    filled_positions=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!='.' and matrix[i][j]!='#':
                interesting_positions.append([i,j,0])
                interesting_positions.append([i,j,1])
    ind=0

    ### dir[0] left, dir[1] right, dir[2] up, dir[3] down
    dist_m=np.zeros((n,m,4), dtype=np.int8)

    for i in range(n):
        for j in range(m):
            if i==0 or matrix[i-1,j]=='#':
                dist_m[i,j,2]=0
            else:
                dist_m[i,j,2]=dist_m[i-1,j,2]+1

            if j==0 or matrix[i,j-1]=='#':
                dist_m[i,j,0]=0
            else:
                dist_m[i,j,0]=dist_m[i,j-1,0]+1

            if i==0 or matrix[n-i,j]=='#':
                dist_m[n-i-1,j,3]=0
            else:
                dist_m[n-i-1,j,3]=dist_m[n-i,j,3]+1

            if j==0 or matrix[i, m-j]=='#':
                dist_m[i,m-j-1,1]=0
            else:
                dist_m[i,m-j-1,1]=dist_m[i,m-j,1]+1



    while ind<len(interesting_positions):
        i=interesting_positions[ind][0]
        j=interesting_positions[ind][1]
        dir=interesting_positions[ind][2]  ### direction 0 for horizontal, 1 for vertical
        if dir==0:
            left = dist_m[i,j,0]
            right = dist_m[i,j,1]

            if matrix[i][j + right - left] == '.':
                matrix[i][j + right - left] = matrix[i][j]
                filled_positions+=1
                interesting_positions.append([i , j+ right - left, 1 - dir])
        else:
            up = dist_m[i,j,2]
            down = dist_m[i,j,3]

            if matrix[i + down - up][j] == '.':
                matrix[i + down - up][j] = matrix[i][j]
                filled_positions+=1
                interesting_positions.append([i+down-up,j,1-dir])
        ind+=1
    return(matrix,filled_positions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    in_f=open('input.txt','r')
    out_f=open('output.txt','w')

    T=int(in_f.readline())

    for Case in range(T):
        n,m=list(map(int,in_f.readline().split()))
        matrix=[0]*n
        for i in range(n):
            string=str(in_f.readline())
            if string[-1:]=='\n':
                string=string[:-1]
            matrix[i]=list(string)

        x=fill(np.array(matrix))
        ans_matrix=x[0]
        filled_positions=x[1]

        print("Case #"+str(Case+1)+': '+str(filled_positions))
        for i in range(len(ans_matrix)):
            row=''.join(ans_matrix[i])
            print(row)
        #out_f.write("Case #"+str(n+1)+': '+anagram(string)+'\n')


    in_f.close()
    out_f.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
