def merge(a, b):
    merged=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            j+=1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
        

# Do not uncomment the merge_sort function below, it is already implemented.
# The function below used your merge function and then produces the output so complete your function.

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#     return merge(left_half, right_half)
