def isPrime(n):
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if isPrime(i):
            print(i)
    if t > 1:
        print()
    t -= 1
