def even_numbers(lst):
    even = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)

    print(even)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers(numbers)
