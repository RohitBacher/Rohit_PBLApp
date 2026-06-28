def sortcolor(strings):
    li = strings.split("-")
    li.sort()
    return "-".join(li)

inp = input("Enter colors: ")
print(sortcolor(strings))
