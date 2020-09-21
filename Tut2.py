
"""lst=[]
lst3=[]

n=int(input())
k=int(input())
for i in range(0,n):
     ele=int(input())
     lst.append(ele)

if k >= n:
    lst2 = set(lst)
    if len(lst2)==len(lst):
        print("Duplicates not found!!")
    else:
        print("Duplicates found!!")
        
if k < n:
    
    lst3=lst[0:k+1]

    new_lst=set(lst3)
    if(len(lst3)==len(new_lst)):
        print("Duplicates not found!!")
    else:
        print("Duplicates found!!")
        """
"""
lst=[]
n=int(input())
for i in range(0,n-1):
    ele=int(input())
    lst.append(ele)

tot_sum=n*(n+1)//2
print("Missing number is ",tot_sum-sum(lst))
"""


"""
n=int(input())
lst1=[]
lst2=[]
for i in range(0,n):
    element=int(input())
    lst1.append(element)
max_num=0
for i1 in range(0,n):
    if lst1[i1] > max_num:
        max_num=lst1[i1]
        print(lst1[i1])
        continue

"""

"""arr = [1, 2, 3, 4, 5] 
index = [3, 2, 4, 1, 0] 
n = len(arr)  
temp = [0]*n ; 
  
for i in range(0,n): 
    temp[index[i]] = arr[i]  
for i in range(0,n): 
    arr[i] = temp[i]
print("Reordered array is:") 
for i in range(0,n): 
    print(arr[i],end = " ")
"""

"""  
n=int(input())
lst1=[]
lst2=[]
for i in range(0,n):
    element=int(input())
    lst1.append(element)
max_num=0
"""
"""for i1 in range(0,n):
    if lst1[i1] > max_num:
         max_num=lst1[i1]
         print(lst1[i1])
         """
"""for i1 in range(n-1,-1,-1):
    if lst1[i1] > max_num:
         max_num=lst1[i1]
         print(lst1[i1])
"""
"""
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if lst1[i] < lst1[j]:
            max_num=lst1[j]
            print(lst1[j])
            break
"""
"""
if lst1[0]==max(lst1):
    for item in reversed(lst1):
          if item > max_num:
              max_num=item
              print(item)
              continue
if lst1[n-1]==max(lst1):
    for item in lst1:
          if item > max_num:
              max_num=item
              print(item)
               
"""
"""
lst=[]
lst2=[]
n=int(input())
k=int(input())
for i in range(0,n):
     ele=int(input())
     lst.append(ele)

if k >= n:
    lst2 = set(lst)
    if len(lst2)==len(lst):
        print("Duplicates not found!!")
    else:
        print("Duplicates found!!")

if k<=n:
    temp=0
    for i in range(0,len(lst)):
       if i+k+1 <= len(lst):
           elecount=lst[i:i+k+1].count(lst[i])
       
       if elecount>1 :
            temp=1
            break
       
        
    if temp==1:
        print("Dublicates found!!!")
    else:
        print("No Duplicates found")
"""    
 
"""                
def differ(x,y):
    diff=x-y

    file=open('pytest.txt',"a")

    file.write(f'diff of {x} and {y} is {diff}\n')

    file.close()
differ(23,45);
"""
"""
a=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    a.append(ele)
if n%2!=0:
    
    for j in range(0,n-1) :
        if a[j] > a[j+1]:
            print(a[j])

    print(a[n-1])
if n%2==0:
    for j in range(0,n-1) :
        if a[j] > a[j+1]:
            print(a[j])

"""
        

































    
