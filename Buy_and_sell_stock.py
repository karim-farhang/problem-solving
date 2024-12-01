testCase = [7, 1, 5, 3, 6, 4]


def bretForce(A):
    maxprof = 0
    for i in range(len(A)):  # Buy
        for j in range(i + 1, len(A)):  # sell
            if A[j] > A[i]:
                maxprof = max(maxprof, A[j] - A[i])
    return maxprof


def optimal(A):
    n = len(A)
    mxprofit = 0
    minprice = float('inf')
    for i in range(n):
        minprice = min(minprice, A[i])
        mxprofit = max(mxprofit, A[i] - minprice)
    return mxprofit


print(bretForce(testCase))
print(optimal(testCase))
