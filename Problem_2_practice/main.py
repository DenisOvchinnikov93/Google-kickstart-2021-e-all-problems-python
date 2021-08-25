# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def compute_boundary(R, C, K, r1, c1, r2, c2):
    d_h=min(r1-1, R-r2)
    d_v=min(c1-1, C-c2)
    l_h=r2-r1+1
    l_v=c2-c1+1

    all_sides= min(math.ceil((d_h+l_h)/K)+math.ceil(l_h/K)+2*math.ceil(l_v/K),
               math.ceil((d_v+l_v)/K)+math.ceil(l_v/K)+2*math.ceil(l_h/K))

    if r1==1:
        all_sides=all_sides-math.ceil(l_v/K)
    if r2==R:
        all_sides=all_sides-math.ceil(l_v/K)

    if c1==1:
        all_sides=all_sides-math.ceil(l_h/K)
    if c2==C:
        all_sides=all_sides-math.ceil(l_h/K)

    return all_sides


def compute_inside(m,n,K):
    n, m=max(m,n), min(m,n)

    if m<=K:
        return n*m-1

    else:
        number_of_squares=((m-1)//K)*((n-1)//K)
        return n*m-1+number_of_squares


def compute(R, C, K, r1, c1, r2, c2):
    bound=compute_boundary(R, C, K, r1, c1, r2, c2)
    inside=compute_inside(r2 - r1 + 1, c2 - c1 + 1, K)
    return compute_boundary(R, C, K, r1, c1, r2, c2)+compute_inside(r2-r1+1,c2-c1+1,K)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    in_f=open('input.txt','r')
    #out_f=open('output.txt','w')

    T=int(in_f.readline())

    for Case in range(T):
        R, C, K=list(map(int,in_f.readline().split()))
        r1, c1, r2, c2=list(map(int,in_f.readline().split()))



        print("Case #"+str(Case+1)+': '+str(compute(R, C, K, r1, c1, r2, c2)))

        #out_f.write("Case #"+str(n+1)+': '+str(compute(R, C, K, r1, c1, r2, c2))+'\n')


    in_f.close()
    #out_f.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
