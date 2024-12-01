def longestSubseqWithDiffOne(arr, n):
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if (arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1):
                dp[i] = max(dp[i], dp[j] + 1)
    result = 1
    print(dp)
    for i in range(n):
        if result < dp[i]:
            result = dp[i]
    return result
arr = [4 ,6, 5, 3 ,3 ,1]
n = len(arr)
print(longestSubseqWithDiffOne(arr, n))
