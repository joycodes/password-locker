# Password Locker

This is a Python application that allows a user to generate and store passwords for various accounts.

# Author 

[Joyce Nguttu](https://github.com/joycodes)

### Installation

* Clone this repository using git clone https://github.com/joycodes/password-locker.git, or downloading a ZIP file of the code.
* The repository, if downloaded as a .zip file will need to be extracted to your preferred location.
* Ensure you have python3.10 installed in your computer.
* From the terminal navigate to the extracted project folder.
* Run python3.10 run.py code in the terminal to launch the app.

## How to Use The app

* Once you launch, You can either create a new user, login or exit the app  
* If you choose to login(log), use: user1 as username and 123 as passWord
* If you choose to create a new account, use reg as the code and follow the prompts.
* Once logged in, you can:

1. View Saved credentials.
2. Add Credentials.
3. Delete Credentials.
4. Search credentials.
5. Log Out.

### Running unit tests

* Run python3.10 credentials_test.py for credential class tests.
* Run python3.10 user_test.py for user class tests.

## Issues

Since there is no database to support the app, once you exit or log out of a session you loose all the credentials and created user. You have to create a new user for every session. You can still use the default login but if you exit the app, you will still loose all the credentials you created.

## Technologies used

* Python 3.10
* PyperClip

## Contact Information 

If you have any question or contributions, please contact me on LinkedIn at [https://www.linkedin.com/in/jnguttu/]

## License

licensed under the [MIT license](LICENSE).
