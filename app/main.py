import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command_list = ['echo', 'exit']
    sentinel = True

    while sentinel :
        sys.stdout.write("$ ")
        command = input()
        index = command.find(" ") + 1
        initial_command = command[:index]
        if initial_command not in command_list:
            print(f"{initial_command}: command not found")
        if initial_command == "exit" :
            sentinel = False
            break
        if command.startswith("echo ") :
            output = command[index:]
            print(f"{command}: {output}")


if __name__ == "__main__":
    main()
