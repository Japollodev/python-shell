import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command_list = ['echo', 'exit']
    sentinel = True

    while sentinel :
        sys.stdout.write("$ ")
        command = input()
        index = command.find(" ")
        initial_command = command[:index]
        arguments = command[index + 1:]
        if initial_command not in command_list:
            print(f"{initial_command}: command not found")
        if initial_command == "exit" :
            sentinel = False
            break
        if command.startswith("echo ") :
            print(f"{arguments}")


if __name__ == "__main__":
    main()
