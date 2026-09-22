import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command_list = ['echo', 'exit']
    sentinel = True

    while sentinel :
        sys.stdout.write("$ ")
        # User input
        command = input()
        # Find out the firs command Index
        index = command.find(" ")
        # Fist Command
        initial_command = command[:index] if index >= 0 else command
         # Argument passed with the command
        arguments = command[index + 1:]
        # Notify  user if the command is not found in acceptable list
        if initial_command not in command_list:
            print(f"{initial_command}: command not found")
        # End run of program if user enters exit
        if command == "exit" :
            sentinel = False
            break
        if command.startswith("echo ") :
            print(f"{arguments}")


if __name__ == "__main__":
    main()
