#Write your complete code here
n=int(input())
s1=input()
s2=input()
lst1=[]
lst2=[]
for i in range(n):
    s = s1[i]
    lst1.append(s)
    t = s2[i]
    lst2.append(t)

flag=False
for j in range(n):
    if lst1[j]=="#" and lst2[j]=="m":
        flag = True
    elif lst1[j]=="m" and lst2[j]=="#":
        flag = True
    elif lst1[j]=="*" and lst2[j]=="n":
        flag = True
    elif lst1[j]=="n" and lst2[j]=="*":
        flag = True
    elif lst1[j]==lst2[j]:
        flag = True
    elif lst1[j]!=lst2[j]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
