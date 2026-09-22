import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command_list = ['echo', 'exit']
    sentinel = True

    while sentinel :
        sys.stdout.write("$ ")
        command = input()
        if command not in command_list:
            print(f"{command}: command not found")
        if command == "exit" :
            sentinel = False
            break
        if command.startswith("echo ") :
            index = command.find(" ") + 1
            output = command[index:]
            print(f"{command}: {output}")


if __name__ == "__main__":
    main()
