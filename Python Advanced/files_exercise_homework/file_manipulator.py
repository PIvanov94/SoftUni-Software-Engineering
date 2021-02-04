import os


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


def add_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(content + "\n")


def replace_string_to_file(file_name, content, replaced):
    try:
        with open(file_name, "r+") as file:
            text = "".join(file.readlines())
            replaced_text = text.replace(content, replaced)
            file.seek(0)
            file.write(replaced_text)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


mapper = {"Create": create_file, "Add": add_to_file, "Replace": replace_string_to_file, "Delete": delete_file}


def start_program():
    data = input().split("-")
    while not data[0] == "End":
        command, command_data = data[0], data[1:]
        mapper[command](*command_data)
        data = input().split("-")


start_program()
