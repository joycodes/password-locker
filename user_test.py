import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    test class that defines tests for user class behaviours
    """

    def setUp(self):
        """
        setup method to run before each test case
        """
        self.new_user = User("NewUser", "qwerty123")  # create user obj

    def test_init(self):
        """
        test if object is initialized properly
        """
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "qwerty123")

    def test_save_user(self):
        """
        test if user object if saved in user_list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == "__main__":
    unittest.main()
