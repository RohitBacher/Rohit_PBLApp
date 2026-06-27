inp = { 
    'Krishna' : [67,68,69],
    'Arjun' :[70,98,63],
    'Malika' : [52,56,60] 
}

name = input("Enter the name: ")

if name in inp:
    t = 0
    for m in inp[name]:
        t += m
    print("Average marks is:", t/3)
else:
    print("Name not present in the input")
