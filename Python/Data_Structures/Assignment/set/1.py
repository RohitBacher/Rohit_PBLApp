s = {10, 20, 30, 40, 50}

item = int(input("Enter the item to remove: "))

if item in s:
    s.remove(item)
    print(s)
else:
    print("Item not found")
