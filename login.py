usernames = []
passwords = []

def signUp(name,psw):
    if name not in usernames:
        if len(name)>0 and len(psw)>0:
            usernames.append(name)
            passwords.append(psw)
        else:
            print("Please fill username & password.")
    else:
        print("This username already exist. Please try another one.")

def login(name):
    if name in usernames:
        psw = input("Enter password:")
        idx = usernames.index(name)
        count = 1
        while psw!=passwords[idx] and count<=3:
            print("Wrong password")
            psw = input("Please enter password again:")
            count+=1
        if psw == passwords[idx]:
            print("Login Successful")
        else:
            print("You entered wrong password for 3 times. Cannot proceed")
    else:
        print("No account found. Please Sign Up first!")

while True:
    option = input("Choose:\n1:Sign Up\n2:Login\n")
    if option.isdigit() and option == '1':
        username = input("Enter username:")
        password = input("Enter password:")
        signUp(username,password)
    elif option.isdigit() and option == '2':
        username = input("Enter username:")
        login(username)
    else:
        print("Invalid input")
    ch = input("Do you want to quit:(y/n)")
    if(ch.lower()=='y'):
        print("Bye Bye!")
        break