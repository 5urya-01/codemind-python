import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
sa=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"{sa:.2f}")