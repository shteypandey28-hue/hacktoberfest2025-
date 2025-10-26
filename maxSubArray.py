class Solution(object):
    def maxSubArray(self, A):
        curSum = maxSum = A[0]
        for i in range(1, len(A)):
            curSum = max(A[i], curSum + A[i])
            maxSum = max(maxSum, curSum)
        return maxSum
