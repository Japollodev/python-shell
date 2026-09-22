import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    command_list = {}
    sentinel = True

    while sentinel :
        sys.stdout.write("$ ")
        command = input()
        if command == "exit" :
            sentinel = False
            break
        if command not in command_list:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
