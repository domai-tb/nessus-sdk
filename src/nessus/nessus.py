from api import NessusAPI
from core import NErrors


class Nessus:
    def __init__(self, server_url: str) -> None:
        self.url = server_url

        # Ensure API initilization
        NessusAPI(self.url)

    @property
    def api(self) -> NessusAPI:
        """
        Get Nessus API handler.
        """
        return NessusAPI()

    def authenticate(
        self,
        bypass_api_limitations: bool = True,
        user_pass: tuple[str, str] | None = None,
        api_keys: tuple[str, str] | None = None,
    ) -> bool:
        """
        Authenticate Nessus.

        Args:
            user_pass (tuple[str, str] | None, optional): Authentication with Username and Password. Defaults to None.
            api_keys (tuple[str, str] | None, optional):  Authentication with Access- and Secret-Key. Defaults to None.

        Returns:
            bool: True on success. False otherwise.
        """
        try:
            if user_pass is not None:
                token = self.api.session.create(user_pass[0], user_pass[1])["token"]
                self.api.session.headers.update({"X-Cookie": f"token={token}"})
                keys = self.api.session.keys()
                access_key, secret_key = keys["accessKey"], keys["secretKey"]
                self.api.session.headers.update(
                    {"X-ApiKeys": f"accessKey={access_key}; secretKey={secret_key}"}
                )
            elif api_keys is not None:
                self.api.session.headers.update(
                    {"X-ApiKeys": f"accessKey={api_keys[0]}; secretKey={api_keys[1]}"}
                )
            else:
                raise NErrors.AuthenticationError
        except:
            return False

        if bypass_api_limitations:
            try:
                magic_api_key = self.api.get_magic_api_token()
                self.api.session.headers.update({"X-Api-Token": magic_api_key})
            except:
                pass

        # check authentication
        try:
            self.api.session.get()
        except:
            return False

        return True
