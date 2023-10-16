import os


def create_file(filename):
    with open(filename, "w") as file:
        pass


def add_content(filename, content_):
    with open(filename, "a") as file:
        file.write(f"{content_}\n")


def replace_content(filename, old_str, new_str):
    try:
        with open(filename, "r") as file:
            file_content = file.read()
        new_file_content = file_content.replace(old_str, new_str)
        with open(filename, "w") as file:
            file.write(new_file_content)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("An error occurred")


commands_mapper = {
    "Create": create_file,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file,
}


command = input()

while command != "End":
    current_command, file_name, *args = command.split("-")

    if current_command in commands_mapper:
        commands_mapper[current_command](file_name, *args)

    command = input()
