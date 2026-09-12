# Упражнение 1
# a=int(input())
# b=int(input())
# print(a+b)
# print(a-b)
# print(a*b)


# Упражнение 2
# a=int(input())
# print(a%10)

# Упражнение 3
# a=list(map(int,input().split()))
# k=1
# for i in a:
#     k*=i
# print(k**(1/len(a)))

# Упражнение 4
# a=open("input.txt").readlines()
# a[0]=a[0][:-1]
# num=a[0]
# n=a[1]
# num=num.split()
# res=0
# if n=="+":
#     res=sum([int(i) for i in num])
#     with open("output.txt", "w") as f:
#         f.write(str(res))
#num1=int(num[0])
# num=num[1:]
# if n =="-":
#     for i in num:
#         i=int(i)
#         num1-=i
#
# if n == "*":
#     for i in num:
#         i=int(i)
#         num1*=i
# if res ==0:
#     with open ("output.txt","w") as f:
#         f.write(str(num1))

# Упражнение 5
# N=int(input())
# b=int(input())
# c=int(input())
# res=0
# k=0
# for i in str(N)[::-1]:
#     res+=int(i)*b**k
#     k+=1
# q=""
# while res>0:
#     q+=str(res%c)
#     res=res//c
# q=q[::-1]
# print(q)


# Упражнение 6
with open("input.txt") as f:
    a=f.readlines()
num = list(map(str, a[0].split()))
op= a[1].strip()
alp=sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
alp=sorted(alp)
alp="".join(alp)
osn= int(a[2].strip())
numk=[]
for i in num:
    k=0
    n=0
    for j in str(i)[::-1]:
        n+=int(alp.find(j))*osn**k
        k+=1
    numk.append(n)
if op =="+":
    res=sum(numk)
if op =="-":
    res=numk[0]
    for i in numk[1:]:
        res-=i
if op =="*":
    res=1
    for i in numk:
        res*=i
flag=0
if res<0:
    flag=1
    res=abs(res)
resk=""
while res>0:
    resk+=str(alp[(res%osn)])
    res=res//osn
resk=resk[::-1]
with open("output.txt","w") as f:
    if flag==0:
        f.write(resk)
    else:
        f.write("-"+resk)