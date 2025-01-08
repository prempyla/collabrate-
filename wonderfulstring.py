s=str(input())
flg_lower=False
flg_upper=False
all_unique=True
for i in range(len(s)):
    if flg_lower== False:
        if s[i].islower():
            flg_lower=True
    if flg_upper==False:
        if s[i].isupper():
            flg_upper=True
    if all_unique==True:
        if s.count(s[i])>1:
            all_unique=False
if all_unique and flg_upper and flg_lower:
    print("Yes")
else:
    print("No")
