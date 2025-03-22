s = input().strip()
n = len(s)
count = 0

for center in range(n):
    left, right = center, center
    while left >= 0 and right < n and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

    left, right = center, center + 1
    while left >= 0 and right < n and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

print(count)
