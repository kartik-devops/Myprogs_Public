"""
def print_formatted(number):
    # your code goes here
    for i in range(1,n+1):
        b=str(oct(i))
        c=str(hex(i))
        d=str(bin(i))
        print(' ',i,' ',b[2:],' ',c[2:].upper(),' ',d[2:],' ')
n=int(input())
print_formatted(n);
"""
"""
n=int(input())
m=int(input())

for i in range(n):
    pattern=".I."
    if i < (n-1)/2:
        print((pattern*(2*i+1)).center(m,"-"))
    elif i==(n-1)/2:
        print("Welcome".center(m,"-"))
    else :
        print((pattern*(2*(n-1-i)+1)).center(m,"-"))
    
"""
"""
n=int(input())
m=int(input())

for i in range(n):
    pattern=".I."
    if i < (n-1)/2:
        print((pattern*(2*i+1)).center(m,"-"))
    elif i==(n-1)/2:
        print("Welcome".center(m,"-"))
    else :
        print((pattern*(2*(n-1-i)+1)).center(m,"-"))
"""
import string
def print_rangoli(size):
    # your code goes here
    strng=string.ascii_lowercase
    for i in range(size-1 , -size , -1):
        temp='-'.join(strng[size-1:abs(i):-1]+strng[abs(i):size])
        print(temp.center(4*size-3,"-"))

n=int(input())
print_rangoli(n);
