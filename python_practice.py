a,b,c,d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

e = a*b*c*d/8/1024/1024
print(round(e,1) )
print("MB")