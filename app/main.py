import sys
import os

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
                    """
                    If the command is not a builtin, your shell must go through every directory in PATH. For each directory:
                        - Check if a file with the command name exists.
                        - Check if the file has execute permissions.
                        - If the file exists and has execute permissions, print <command> is <full_path> and stop.
                        - If the file exists but lacks execute permissions, skip it and continue to the next directory.
                    """

                    env_path = os.environ.get("PATH", '')
                    cmd_directories = env_path.split(os.pathsep)

                    for directory in cmd_directories:
                        queried_path = os.path.join(directory, second_command)

                        # Determine if query path for command file exists and has permissions
                        cmd_file_exists = os.path.exists(queried_path)
                        cmd_file_has_execute_permissions = os.access(queried_path, os.X_OK)
                        if cmd_file_exists and cmd_file_has_execute_permissions:
                            cmd_path = queried_path
                            print(f"{second_command} is {cmd_path}")
                            break
                        elif cmd_file_exists and not cmd_file_has_execute_permissions:
                            continue
                    else:
                        print(f"{second_command}: not found")


        # Notify  user if the command is not found in acceptable list
        else:
            print(f"{initial_command}: command not found")


if __name__ == "__main__":
    main()
