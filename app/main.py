import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command_list = ["echo", "exit", "type"]
    sentinel = True

    while sentinel :
        sys.stdout.write("$ ")
        # User input
        command = input()
        # segment the user's input to command + args
        command_split = command.split(" ")
        # Fist Command
        initial_command = command_split[0]
        # Argument passed with the command
        comm_len = len(command_split)
        # Make sure to not remove space for join
        arguments = " ".join(command_split[1:]) if len(command_split) > 1 else ""


        if initial_command in command_list:
            # End run of program if user enters exit
            if command == "exit" or command.startswith("exit") :
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
            print(f"{initial_command}: command not found")


if __name__ == "__main__":
    main()
