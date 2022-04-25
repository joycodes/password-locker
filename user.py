class User:
    """
    a class for users
    """

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    user_list = []

    def save_user(self):
        """
        method that appends users to user_list
        """
        self.user_list.append(self)

