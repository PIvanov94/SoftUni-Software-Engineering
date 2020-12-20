line = input()

for index in range(len(line)):
    if line[index].startswith(":"):
        print(line[index:index+2])