import unittest
from credentials import Credentials
import pyperclip


class TestCredentials(unittest.TestCase):
    """
    tests cases for credentials' class behaviours
    """

    def setUp(self):
        self.new_credentials = Credentials(
            "Account", "AccountUserName", "Allow1234")  # create credentials object

    def test_init(self):
        """
        tests if credentials object is proprely initialized
        """
        self.assertEqual(self.new_credentials.account_name, "Account")
        self.assertEqual(
            self.new_credentials.account_username, "AccountUserName")
        self.assertEqual(self.new_credentials.account_password, "Allow1234")

    def test_save_credentials(self):
        """
        tests if credentials is saved in credentials' list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """
        tests if i can save multiple credentials in credentials' list
        """
        self.new_credentials.save_credentials()
        new_test_credentials = Credentials(
            "Twitter", "TestAccountName1", "TestAccountPassword1")  # new cred
        new_test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        """
        this method does clean up after each test case is run to avoid errors/failures
        """
        Credentials.credentials_list = []

    def test_delete_credentials(self):
        """
        this method checks if i can remove/delete a credential from the list
        """
        self.new_credentials.save_credentials()
        new_test_credentials = Credentials(
            "Twitter", "TestAccountName1", "TestAccountPassword1")  # new cred
        new_test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  # deletes the credential
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_locate_credentials_by_name(self):
        """
        tests to check if we can locate a credential and display info
        """
        self.new_credentials.save_credentials()
        new_test_credentials = Credentials(
            "Twitter", "TestAccountName1", "TestAccountPassword1")  # new cred
        new_test_credentials.save_credentials()

        located_credentials = Credentials.locate_by_name("Twitter")

        self.assertEqual(located_credentials.account_name,
                         new_test_credentials.account_name)

    def test_credentials_exists(self):
        """
        test to check if we can return boolean if we cannot find the credential
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Account", "TestAccountName", "TestAccountPassword")  # new cred
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exists("Account")

        self.assertTrue(credentials_exists)

    def test_display_credentials(self):
        """
        method that displays all current credentials
        """
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)

    # self.new_credentials.account_password, pyperclip.paste())


if __name__ == "__main__":
    unittest.main()
