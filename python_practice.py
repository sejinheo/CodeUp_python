a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

min1 = a if(a<b) else b
min2 = min1 if(min1 < c) else c

print(min2)