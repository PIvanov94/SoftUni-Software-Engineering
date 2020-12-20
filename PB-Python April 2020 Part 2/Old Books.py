book = input()
lib_cnt = int(input())
checked_books = 0

while lib_cnt > 0:
    current_book = input()
    if current_book == book:
        print(f"You checked {checked_books} books and found it.")
        break
    else:
        checked_books += 1
    lib_cnt -= 1

if lib_cnt <= 0:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")