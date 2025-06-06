n=int(input())
arr=list(map(int, input().split()))
arr.sort()
median = arr[n//2]
total = sum(abs(x-median) for x in arr)

print(total)
