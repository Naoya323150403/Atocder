n = int(input())
sum = 0
for i in range(1, n-1):
    if i % 3 and i % 5:
        sum+=1
print(sum)