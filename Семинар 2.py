# Упражнение 1
# a=input().split()
# kol=int(a[0])
# card = list(map(int, a[1:]))
# su= 0
# for i in range(1, kol+1):
#     su+=i
# print(su - sum(card))


# Упражнение 2
# a=input().split()
# kol=int(a[0])
# st = a[1]
# stk= ""
#
# for i in range(len(st)//kol):
#     stk+=st[:kol:][::-1]
#     st=st[kol:]
# print(stk)


# Упражнение 4
# a="".join(str(input()).split())
# print("".join(a[i:i+2][::-1] for i in range(0, len(a),2 )))

#одно и тоже что выше
# a=input().split()
# a[0:-1:2], a[1::2]= a[1::2], a[0:-1:2]
# print(*a)


# Упражнение 5
# a = "".join(str(input()).split())
# print(a[-1]+a[:-1])


# Упражнение 6
# a=input().split()
# for i in a:
#     if a.count(i)==1:
#         print(i, end=" ")


# Упражнение 7
# a=input().split()
# ma=0
# s=""
# for i in a:
#     if a.count(i)>ma:
#         ma=a.count(i)
#         s=i
# print(s)


# Упражнение 9
# with open("input.txt") as f:
#     a=f.read()
# alp=["...", "?!", "!?", "!", "?"]
#
# for i in alp:
#     a=a.replace(i, ".")
# print(a.count("."))
from re import *

# Упражнение 9 чуть лучше
# with open("input.txt") as f:
#     a=f.read()
# alp=["...", "!", "?"]
# for i in alp:
#     a=a.replace(i,".")
# kol=0
# alp="qwertyuiopasdfghjklzxcvbnm"
# for i in range(1,len(a)):
#     if a[i]=="." and a[i-1] in alp:
#         kol+=1
# print(kol)

# with open("input.txt") as f:
#     a=f.read()
# kol=0
# flag=False
# for i in a:
#     if i in ".?!":
#         if not flag:
#             flag=True
#             kol+=1
#     else:
#         flag=False
# print(kol)

# Упражнение 10
# a=str(input())
# s=""
# gl= "уеыаояиюэ"
# sogl = "йцкнгшщзхъфвпрлдсжчмтьб"
# i=0
# a+=" "
# while i<len(a):
#     if a[i] in sogl and a[i+1] in gl:
#         s+=a[i]+a[i+1]+"c"+a[i+1]
#         i+=2
#     else:
#         s+=a[i]
#         i+=1
# if s[-1]==" ":
#     print(s[:-1])
# else:
#     print(s)



# Упражнение 8
# kol=int(input())
# num=list(map(int,input().split()))
# for i1 in num:
#     kol1=0
#     kol2=0
#     for i2 in num:
#         if i1>i2:
#             kol1+=1
#         if i1<i2: kol2+=1
#     if kol1==kol2:
#         print(i1)
#         break


#Упражнение 3
a=str(input())
flagp=0
flagm=0
alp1="AHIMOTUVWXY18"
alp2="EJSZ"
alp3="3L25"
for i in range(len(a)//2):
    if a[i]==a[-1*i-1] and a[i] in alp1:
        flagp=1
        flagm=1
    if (alp2.find(a[i])==alp3.find(a[-1*i-1]) and alp2.find(a[i])!=-1 ) or (alp3.find(a[i])==alp2.find(a[-1*i-1]) and  alp3.find(a[i])!=-1):
        flagm=1
        flagp=0
    if a[i]==a[-1*i-1] and a[i] not in alp1:
        flagm=0
        flagp=1
    if flagp+flagm==0:
        print(f"{a} is not a palindrome.")
        break

if flagm+flagp==2:
    if len(a)%2==0:
        print(f"{a} is a mirrored palindrome.")
    else:
        if a[len(a)//2] in alp1:
            print(f"{a} is a mirrored palindrome.")
        else:
            print(f"{a} is a regular palindrome.")
if flagm==0 and flagp ==1:
    print(f"{a} is a regular palindrome.")
if flagm==1 and flagp ==0:
    print(f"{a} is a mirrored string.")
