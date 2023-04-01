# Ask user for master password
master_pwd = input("What is the master password? ")


# Start of program
while True:
    mode = input("Would you like to add a new password or view existing ines (view, add)? Press q to quit ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue