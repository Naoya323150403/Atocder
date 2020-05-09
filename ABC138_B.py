from fractions import Fraction

n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += (1 / a[i])

ans = 1 / sum
print(ans)
