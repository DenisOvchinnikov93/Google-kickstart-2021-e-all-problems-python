# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

if __name__ == '__main__':
    T=int(input())
    lam =0.5772156649

    for Case in range(T):

        N=int(input())
        if N < 100:
            ans=0
            for i in range(N):
                ans+=1/(i+1)
        elif N<5000:
            ans = lam +math.log(N)+1 / (2 * N)-1 / (12 * N * N)
        elif N<10**7:
            ans = lam +math.log(N)+1 / (2 * N)
        else:
            ans = lam +math.log(N)
        print("Case #"+str(Case+1)+": "+str(ans))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
