x = int(input("Enter number: "))
n = x
m = 0
while n>0:
    m = m*10 + (n%10)
    n = n//10
    
if x == m:
    print(x, "is palindrome")
else:
    print(x, "is not palindrome")
