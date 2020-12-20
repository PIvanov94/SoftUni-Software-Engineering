positive_list = input().split(", ")


def palindrome_integers(numbers):
    for number in positive_list:
        if number[::] == number[::-1]:
            print("True")
        else:
            print("False")
    return palindrome_integers


palindrome_integers(positive_list)
