def is_palindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in name:
        if ch in vowels:
            count += 1

    print("No of vowels:", count)


def frequency_of_letters(name):
    d = {}

    for ch in name:
        if ch != " ":
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

    print("Frequency of letters:")
    for key, value in d.items():
        print(key, "-", value)
