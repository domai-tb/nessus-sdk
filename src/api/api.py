from .auth import AuthenticationAPI
from .base import BaseAPI


class NessusAPI:
    """
    The Nessus object is the primary interaction point for users to interface with Nessus Server.
    All of the API endpoint classes that have been written will be grafted onto this class.
    """

    def __init__(
        self,
        username: str = "",
        password: str = "",
        server_url: str = "https://127.0.0.1:8834",
        verify_ssl: bool = False,
    ):
        self.username = username
        self.password = password
        self.server_url = server_url
        self.verify_ssl = verify_ssl

    @property
    def base(self):
        """
        The interface object for basic API functionality.
        """
        return BaseAPI(self)

    @property
    def auth(self):
        """
        The interface object for the Nessus Authentication.
        """
        return AuthenticationAPI(self)
