import random
from user import User
from credentials import Credentials

# functions that add credentials


def create_new_credentials(account_name, account_username, account_password):
    """
    function to create new acc with its credentials
    """
    new_credentials = Credentials(
        account_name, account_username, account_password)
    return new_credentials


def save_new_credentials(credentials):
    """
    function to save the new credentials
    """
    credentials.save_credentials()


def locate_credentials(account_name):
    """
    function to locate credentials based on account_name
    """
    return Credentials.locate_by_name(account_name)


def credentials_existance(name):
    """
    function that checks if a a particular account and its credentials exist based on searched account_name
    """
    return Credentials.credentials_exists(name)


def delete_credentials(credentials):
    """
    function that deletes credentials
    """
    return Credentials.delete_credentials(credentials)


def display_credentials():
    """
    fuction that returns all saved credentials
    """
    return Credentials.display_credentials()


def main():
    while True:
        print("*"*29 + "\n")
        print("\t"+"PASSWORD LOCKER"+ "\n"+"*"*29)
        print('\n')
        print("Use these short codes to select an option: To create New User - reg, To login your account - log, To exit - ex")
        short_code = input().lower()
        print('\n')

        if short_code == 'reg':
            print("Create a UserName")
            created_user_name = input()

            print("Select a Password")
            created_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_password:
                print("Sorry, your password did not match!")
                print("Enter a password")
                created_password = input()
                print("Confirm your Password")
                confirm_password = input()
            else:
                print(
                    f"Congratulations {created_user_name}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

                while entered_userName != created_user_name or entered_password != created_password:
                    print("You entered a wrong username or password")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()
                else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                    print('\n')

                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credentials")
                    print("3: Delete credentials")
                    print("4: Search credentials")
                    print("5: Log Out")
                    option = input()

                    if option == '1':
                        while True:
                            print("Below is a list of all your credentials")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(
                                        f"ACCOUNT NAME:{credential.account_name}")
                                    print(
                                        f"ACCOUNT USERNAME:{credential.account_username}")
                                    print(
                                        f"PASSWORD:{credential.account_password}")

                            else:
                                print('\n')
                                print("You don't seem to have any contacts yet")
                                print('\n')

                            print("Back to Menu? y/n")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == '2':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter your Account Name")
                                account_name = input()
                                print("Enter your account username")
                                account_username = input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'gp' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gp':
                                    account_password = random.randint(
                                        111111, 1111111)
                                    print(f"Account: {account_name}")
                                    print(f"Username: {account_username}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif keyword == 'n':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Username: {account_username}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_new_credentials(create_new_credentials(
                                    account_name, account_username, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")

                    elif option == '3':
                        while True:
                            print("Search for credential to delete")

                            search_name = input()

                            if credentials_existance(search_name):
                                search_credential = locate_credentials(
                                    search_name)
                                print(
                                    f"ACCOUNT NAME: {search_credential.account_name} \n USERNAME: {search_credential.account_username} \n PASSWORD: {search_credential.account_password}")
                                print("Delete? y/n")
                                sure = input().lower()
                                if sure == 'y':
                                    delete_credentials(search_credential)
                                    print("Account SUCCESSFULLY deleted!")
                                    break
                                elif sure == 'n':
                                    continue

                            else:
                                print("That Credential Does not exist")
                                break

                    elif option == '5':
                        print(
                            "WARNING! You will loose all your credentials if you log out. Are you sure? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out")
                            break
                        elif logout == 'n':
                            continue

                    elif option == '4':
                        while True:
                            print("Continue? y/n")
                            option2 = input().lower()
                            if option2 == 'y':
                                print("Enter an account name to find credentials")

                                search_name = input()

                                if credentials_existance(search_name):
                                    search_credential = locate_credentials(
                                        search_name)
                                    print(
                                        f"ACCOUNT NAME: {search_credential.account_name} \n USERNAME: {search_credential.account_username} \n PASSWORD: {search_credential.account_password}")
                                else:
                                    print("That Credential Does not exist")
                            elif option2 == 'n':
                                break
                            else:
                                print("Please enter a valid code")

                    else:
                        print("Please enter a valid code")
                        continue

        elif short_code == 'log':
            print("WELCOME")
            print("Enter UserName")
            default_user_name = input()

            print("Enter Your password")
            default_password = input()
            print('\n')

            while default_user_name != 'user1' or default_password != '123':
                print(
                    "Wrong userName or password. Username 'user' and password '123'")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_password = input()

                print('\n')

            if default_user_name == 'user' and default_password == '123':
                print("YOU HAVE SUCCESSFULLY LOGGED IN!")
                print('\n')
                print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1: View Your saved credentials")
                print("2: Add new credentials")
                print("3: Delete credentials")
                print("4: Search credentials")
                print("5: Log Out")
                option = input()

                if option == '1':
                    while True:
                        print("Below is a list of all your credentials")
                        if display_credentials():

                            for credential in display_credentials():
                                print(
                                    f"ACCOUNT NAME:{credential.account_name}")
                                print(
                                    f"ACCOUNT USERNAME:{credential.account_username}")
                                print(
                                    f"PASSWORD:{credential.account_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any contacts yet")
                            print('\n')

                        print("Back to Menu? y/n")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("Please Enter a valid code")

                elif option == '2':
                    while True:
                        print("Continue to add? y/n")

                        choice = input().lower()
                        if choice == 'y':
                            print("Enter your Account Name")
                            account_name = input()
                            print("Enter your account username")
                            account_username = input()
                            print("Enter a password")
                            print(
                                "To generate random password enter keyword 'gp' or 'n' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                account_password = random.randint(
                                    111111, 1111111)
                                print(f"Account: {account_name}")
                                print(f"Username: {account_username}")
                                print(f"Password: {account_password}")
                                print('\n')
                            elif keyword == 'n':
                                print("Create your password")
                                account_password = input()
                                print(f"Account: {account_name}")
                                print(f"Username: {account_username}")
                                print(f"Password: {account_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_new_credentials(create_new_credentials(
                                account_name, account_username, account_password))
                        elif choice == 'n':
                            break
                        else:
                            print("Please use 'y' for yes or 'n' for no!")

                elif option == '3':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if credentials_existance(search_name):
                            search_credential = locate_credentials(
                                search_name)
                            print(
                                f"ACCOUNT NAME: {search_credential.account_name} \n USERNAME: {search_credential.account_username} \n PASSWORD: {search_credential.account_password}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                delete_credentials(search_credential)
                                print("Account SUCCESSFULLY deleted!")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That Contact Does not exist")
                            break

                elif option == '5':
                    print(
                        "WARNING! You will loose all your credentials if you log out. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                    elif option == '4':
                        while True:
                            print("Continue? y/n")
                            option2 = input().lower()
                            if option2 == 'y':
                                print("Enter an account name to find credentials")

                                search_name = input()

                                if credentials_existance(search_name):
                                    search_credential = locate_credentials(
                                        search_name)
                                    print(
                                        f"ACCOUNT NAME: {search_credential.account_name} \n USERNAME: {search_credential.account_username} \n PASSWORD: {search_credential.account_password}")
                                else:
                                    print("That Credential Does not exist")
                            elif option2 == 'n':
                                break
                            else:
                                print("Please enter a valid code")

                    else:
                        print("Please enter a valid code")

        elif short_code == 'ex':
            break
        else:
            print("Please Enter a valid code to continue")


if __name__ == '__main__':
    main()
