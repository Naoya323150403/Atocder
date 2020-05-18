import math
a,b,h,m = map(int,input().split())
angle= math.pi * 2 * (h/12 + m/60/12 - m/60)
ans =a**2 + b**2 - 2*a*b*math.cos(angle)
print(ans**0.5)

