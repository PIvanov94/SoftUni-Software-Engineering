n_commands = int(input())
registered_users = {}

for _ in range(n_commands):
    data = input().split()
    command = data[0]
    username = data[1]
    if command == "register":
        license_id = data[2]
        if username not in registered_users:
            registered_users[username] = license_id
            print(f"{username} registered {license_id} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_id}")
    if command == "unregister":
        if username not in registered_users:
            print(f"ERROR: user {username} not found")
        else:
            registered_users.pop(username)
            print(f"{username} unregistered successfully")

for name, id_car in registered_users.items():
    print(f"{name} => {id_car}")