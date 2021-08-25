import math


def anagram(string):
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    dict_letters={}
    for let in s:
        dict_letters[let]=[]
    for i in range(len(string)):
        dict_letters[string[i]].append(i)

    for let in s:
        if len(dict_letters[let])>len(string)/2:
            return('IMPOSSIBLE')

    ordered_str=[]
    for let in s:
        for pos in dict_letters[let]:
            ordered_str.append([pos, let])

    ans_str=['']*len(string)
    move=math.ceil(len(string)/2)
    for i in range(len(string)):
        ans_str[ordered_str[i][0]]=ordered_str[(i+move)%len(string)][1]
    return(''.join(ans_str))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    in_f=open('input.txt','r')
    #out_f=open('output.txt','w')

    N=int(in_f.readline())

    for n in range(N):
        string=in_f.readline()
        if string[-1:]=='\n':
            string=string[:-1]
        print("Case #"+str(n+1)+': '+anagram(string))


    in_f.close()
    #out_f.close()