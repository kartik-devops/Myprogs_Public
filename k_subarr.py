from math import *
cnt=0
square_list=[]
arr=[]
n=int(input("enter number of elements :"))
for i in range(0,n):
    x=int(input())
    arr.append(x)
    c=sqrt(x)
    d=int(c)
    if d==c:
        square_list.append(x)
        cnt+=1


k=int(input())
if k > cnt:
    print(0)
elif k==cnt:
    print(n)
else:
    print(2*n-cnt)
