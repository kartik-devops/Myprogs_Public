"""
a=int(input())
b=int(input())
c=int(input())
if a > b and a>b:
    print("a is greater")
elif b>a and b>c :
    print("b is greater")
else :
    print("c is greater")

"""
"""
a=int(input())
b=int(input())
c=int(input())
d=max(a,b)
e=max(d,c)
print(e)
"""
"""
sum_num=0
n=int(input())
for i in range(0,n+1):
    if i%2==0 :
        sum_num+=i
print(sum_num)
"""

"""
def prime_num(n):
    tmp=1
    if n > 1:
        for i in range(2,n//2+1):
            if n%i==0:
                 print("not a prime num")
                 break
        else:
               print("prime num")
    else :
        print("Not a prime number")
    

prime_num(29)

"""
"""
def sums(n):
    sum_var=0
    for i in range(0,n+1):
        sum_var+=i
    return sum_var

n=int(input())
sumTot=sums(n)
print(sumTot)
"""
"""
def sums(n):
    sum_var=0
    for i in range(0,n+1):
        if i%2==0:
            
           sum_var+=i
    return sum_var

n=int(input())
sumodd=sums(n)
print(sumodd)

"""
"""
n=int(input())
if n > 1:
        for i in range(2,n//2+1):
            if n%i==0:
                 print("not a prime num")
                 break
        else:
               print("prime num")
else :
  print("Not a prime number")
"""

#n1=int(input("Till whrere you want :"))

def sum_prime(n1):
    sum_num=0
    for num in range(2,n1+1):
        i=2
        for i in range(2,num):
            if int(num%i) == 0:
                i=num
                break;
        if i!=num:
            sum_num+=num

    print(sum_num+2)
    
n1=int(input("Till whrere you want :"))
print("Sum is :")
sum_prime(n1);
