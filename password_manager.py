# Ask user for master password
master_pwd = input("What is the master password? ")


# View passwords.txt
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # Take off line break to eliminate new line print
            data = line.rstrip()
            # Assign user and passw to name and pwd
            user, passw = data.split("|")
            print("User: ", user, "Password: ", passw)



# Add account name and password to passwords.txt file
def add():
    # Ask user for account name and password to add
    name = input("Account Name: ")
    pwd = input("Password: ")

    # Open file password.txt if it exists and append new name and password to end of file, 
    # If file does not exist, create password.txt and append new name and password
    # Close file when done
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


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