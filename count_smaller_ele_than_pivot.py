class Solution:
    def countSmallerThanPivot(self, arr, pivot):
        arr.sort()
        ans = 0
        for i in range(len(arr)):
            if arr[i] < pivot:
                ans += 1
        return ans
