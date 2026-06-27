n = input("Enter:")

l = [int(i) for i in list(n.split(','))]
l.sort()

for i in range(len(l)):
    if l[len(l)-i-1] < l[len(l)-1]:
        x = l[len(l)-i-1]
        break

print(x)
