n = int(input("Enter number: "))
dsum = 0
while n>0:
    dsum += n%10
    n = n//10

print(dsum)
