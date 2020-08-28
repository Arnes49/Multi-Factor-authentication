import hashlib
import smtplib


def hashing_method(hash_pass):
    key = hashlib.md5(hash_pass.encode())
    return key.hexdigest()


def send_email(receiver, password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
    except Exception:
        print("Something went wrong")
        input("Press enter to close the window")

    # traffic encryption
    server.starttls()
    # login into system, from which we send keys.
    system_pass = "ntcncbcntv409"
    system_email = "testsystemfor409@gmail.com"
    server.login(system_email, system_pass)

    key = hashing_method(password)
    msg = \
        f"""
    Authentication code is: {key}

    Sincerely, 
    Your support.
    """
    server.sendmail(system_email, receiver, msg)
    server.quit()
    return key


def user_reg():
    while True:
        login = input("Login: ")
        try:
            open(login + ".txt", "r")
            print("This login is already used!")
        except Exception:
            password = input("Password: ")
            password1 = input("Password confirm: ")
            if password == password1:
                # create a file login:system
                file = open(login + ".txt", "w")
                file.write(login + ":" + password)
                file.close()
                break
            else:
                print("Passwords don't match!")
                print("Try again.")


def user_login():
    attempts = 0
    while True:
        if attempts > 2:
            input("Press enter to close the window")
            break

        login = input("Login: ")
        password = input("Password: ")
        try:
            user = open(login + ".txt", "r")
        except FileNotFoundError:
            print("Incorrect login or password!")
            attempts += 1
            if attempts < 3:
                print("Try again.")
            continue
        # read login:password from user file.
        data = user.readline()
        user.close()

        if data == login + ":" + password:
            email = input("Enter your e-mail address: ")
            check = send_email(email, password)
            auth_key = input("Enter your Authentication code: ")

            if check == auth_key:
                print("You logged in successfully.")
                input("Press enter to close the window")
                break
            else:
                print("Invalid code.")
                input("Press enter to close the window")
                break
        else:
            print("Incorrect login or password!")
            attempts += 1
            if attempts < 3:
                print("Try again.")


def request():
    print("Enter 'q' for exit.")
    while True:
        check = input("Do you have an account? y/n: ")
        if check == "n":
            user_reg()
            break
        elif check == "y":
            user_login()
            break
        elif check == "q":
            break
        else:
            print("I don't know this command.")


request()
