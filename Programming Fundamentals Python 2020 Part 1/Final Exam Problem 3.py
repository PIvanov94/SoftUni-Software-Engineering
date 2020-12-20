messages_capacity = int(input())

line = input()
users = {}

while not line == "Statistics":
    data = line.split("=")
    command = data[0]
    if command == "Add":
        username = data[1]
        sent = int(data[2])
        received = int(data[3])
        if username not in users:
            users[username] = {"sent": sent, "received": received}
    elif command == "Message":
        sender = data[1]
        receiver = data[2]
        if sender in users and receiver in users:
            users[sender]['sent'] += 1
            users[receiver]['received'] += 1
            total_sender_messages = users[sender]['sent'] + users[sender]['received']
            total_receiver_messages = users[receiver]['received'] + users[receiver]['sent']
            if total_sender_messages >= messages_capacity:
                del users[sender]
                print(f"{sender} reached the capacity!")
            if total_receiver_messages >= messages_capacity:
                del users[receiver]
                print(f"{receiver} reached the capacity!")
    elif command == "Empty":
        username = data[1]
        if username == "All":
            users = {}
        elif username in users:
            del users[username]
    line = input()

sorted_messages = dict(sorted(users.items(), key=lambda x: (-x[1]['received'], x[0])))
sum_of_2 = {k: sum(v.values()) for k, v in sorted_messages.items()}

print(f"Users count: {len(users)}")

for name, value in sum_of_2.items():
    print(f"{name} - {value}")
