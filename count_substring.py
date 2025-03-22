s=input()
n=len(s)
count=0
for i in range(n):
    for j in range(i,n):
        if s[i:j+1] == s[i:j+1][::-1]:
            count+=1
print(count)


