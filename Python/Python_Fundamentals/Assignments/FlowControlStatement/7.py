for j in range(10, 99):
    for i in range(2, j):
        if j%i == 0:
            break
    else:
        print(j)
