history = []

while True:
    command = input("Enter a command: ")
    
    if command == "history":
        number = 1
        for item in history:
            print(number, item)
            number += 1

    elif command == "exit":
        break

    else:
        history.append(command)
        print("Command logged.")