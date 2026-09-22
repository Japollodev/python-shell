import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command_list = ["echo", "exit", "type"]
    sentinel = True

    while sentinel :
        sys.stdout.write("$ ")
        # User input
        command = input()
        # Find out the firs command Index
        index = command.find(" ")

        has_args = index >= 0
        # Fist Command
        initial_command = command[:index] if has_args else command
         # Argument passed with the command
        arguments = command[index + 1:] if has_args else ''

        if initial_command in command_list:
            print(f"{initial_command}: command not found")
            # End run of program if user enters exit
            if command == "exit" :
                sentinel = False
                break
            if command.startswith("echo ") :
                print(f"{arguments}")
            if command.startswith("type ") :
                second_command = command.split(" ", 1)[1]
                if second_command in command_list:
                    print(f"{second_command} is a shell builtin")
                else:
                    print(f"{second_command}: not found")


        # Notify  user if the command is not found in acceptable list
        else:
            if initial_command == "echo":
                sentinel = False


if __name__ == "__main__":
    main()
