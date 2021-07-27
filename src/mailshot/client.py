import os

class Client:
    """
        A class used to represent the client.

        Attributes:
            email (str): An email. 
                (default is None)
            password (str): A password.
                (default is None)

        Methods:
            _get(): Returns dictionary of the client attributes.
            _set(): Sets attribute value to attribute value from environment variables.
    """
    def __init__(self, email=None, password=None) -> None:
        """
            Args:
                email (str): An email string.
                    (default is None)
                password (str): A password string.
                    (default is None)

            Raises:
                ValueError: If either email or password is not provided.
        """
        if email is None and password is None:
            self._set()
        elif email is None or password is None:
            raise ValueError
        else:
            self._email = email
            self._password = password
    

    def _get(self) -> str:
        """
            Returns dictionary of the client attributes.

            Returns:
                dict: A dictionary of the attributes.
        """
        return {
            "EMAIL": self._email,
            "PASSWORD": self._password
        }


    def _set(self) -> None:
        """
            Sets attribute value to attribute value from environment variables.

            Returns:
                dict: A dictionary of the attributes.

            Raises:
                KeyError: If environment variable not found.
        """
        try:
            self._email = os.environ['EMAIL']
            self._password = os.environ['PASSWORD']
        except KeyError:
            raise KeyError