a,b,c,k = map(int,input().split())


if  k <= a:
    print(k)
elif a + b >= k:
    print(a)
else:
    print(2*a + b -k)
