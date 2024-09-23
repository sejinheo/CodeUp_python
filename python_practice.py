a = input()
a = int(a)
check = 1
sum = 0
while 1:
    sum = sum + check
    check = check + 1 
    if(sum >= a):
        break
print(sum)