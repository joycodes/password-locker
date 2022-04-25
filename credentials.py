class Credentials:
    """
    create class for user credentials
    """

    def __init__(self, account_name, account_username, account_password):
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        """
        method that saves credentials' object in credentials' list
        """
        self.credentials_list.append(self)

    def delete_credentials(self):
        """
        method that deletes a credential
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def locate_by_name(cls, account_name):
        """
        method that takes in a name and returns a credential that matches the specific name
        Args:
            name: account_name that has a password
        Returns:
            The account_name and its corresponding password
        """
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credentials_exists(cls, name):
        """
        method that checks if credentials exists from credentials_list.
        Args:
            name: Username to search for its existance
        Returns:
            Boolean: True or false depending if the credentials exists 
        """
        for credential in cls.credentials_list:
            if credential.account_name == name:
                return True
            return False

    @classmethod
    def display_credentials(cls):
        """
        method that returns credentials' list
        """
        return cls.credentials_list

    # pyperclip.copy(credentials_located.account_password)
