data = input()

counter = 0
resources = {}
key = ""

while not data == "stop":
    if counter % 2 == 0:
        key = data
        if key not in resources:
            resources[key] = 0
    else:
        value = int(data)
        resources[key] += value
    counter += 1
    data = input()

for key, value in resources.items():
    print(f"{key} -> {value}")