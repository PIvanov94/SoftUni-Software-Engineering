n = int(input())

pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

line = input()

while not line == "Stop":
    data = line.split("|")
    command = data[0]
    piece = data[1]
    if command == "Add":
        composer = data[2]
        key = data[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        new_key = data[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    line = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))

for piece, value in sorted_pieces:
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")