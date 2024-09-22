a = int(input())
check = 0
sum = 0
while 1:
    if sum >= a:
        break
    check = check + 1
    sum = sum+check
        
print(check)