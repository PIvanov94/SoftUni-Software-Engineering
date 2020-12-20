n = int(input())
asci_small_a = ord("a")

for first_char in range(asci_small_a, asci_small_a + n):
    for second_char in range(asci_small_a, asci_small_a + n):
        for third_char in range(asci_small_a, asci_small_a + n):
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}")