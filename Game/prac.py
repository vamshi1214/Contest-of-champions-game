'''x=[1,3,4,6,5,3,5,7]
x.insert(0,4)
print(x)'''
import math
'''t=int(input())
sum=0
#for i in range(t):
k=int(input())
for i in range(t):

    x=math.floor(k/(10**(i)))
    print(i)
    sum=sum+x
print(sum)'''
###222
#the sesssion
'''t=int(input())
sum=0
for i in range(t):
    k=int(input())
    x=math.floor(k/(10**(i)))
    sum+=x
print(sum)'''
###
'''t=int(input())
h=[]
i=0
for i in range(t):
    n,k=map(int,input().split())
    for j in range(n):
        x = list(map(int, input().split()))
        h.append(x)
        print(h)'''
'''rev=h[::-1]
    h.insert(0,k)
    if h==rev:
        print("1")

    else:
        print("0")
    print(h)''' 
'''t=int(input())
h=[]
raw_=[]
i=0
for i in range(t):
    n,k=map(int,input().split())




    x = list(map(int, input().split()))
    for i in x:
        raw_.append(i)

    for i in raw_:
        h.append(i)
    while rev!=h:
        h.insert(0,k)
        rev=h[::-1]
        if h==rev:
            print("1")

        else:
            print("0")
        i+=1
        if i>=10:
            break'''
'''def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word = word[i] + "_"
    return new_word

phrase = "hello"
print(add_underscores(phrase))'''
for i in range(4,1):
    print(i)