
lst = list(map(int, input().split()))
q = int(input())

prefix_sum = [0] * len(lst)
prefix_sum[0] = lst[0]
for i in range(1, len(lst)):
    prefix_sum[i] = prefix_sum[i - 1] + lst[i]

for j in range(q):
    L, R = map(int, input().split())
    if L > 0:
        result = prefix_sum[R] - prefix_sum[L - 1]
    else:
        result = prefix_sum[R]
    print(result)
