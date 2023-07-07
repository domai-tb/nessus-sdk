from core import Networking


class SessionAPI(Networking):
    def create(self, username: str, password: str) -> dict:
        """
        Create a new session token for the given user. Certificate based logins require no parameters.

        Args:
            username (str): The username for the person who is attempting to log in.
            password (str): 	The password for the person who is attempting to log in.

        Returns:
            dict: API-Token of given user and MD5-Sums:

                    {
                        "md5sum_wizard_templates": {string},
                        "token": {string},
                        "md5sum_tenable_links": {string}
                    }
        """
        return {}

    def destroy(self):
        pass

    def edit(self):
        pass

    def get(self):
        pass

    def password(self):
        pass

    def keys(self):
        pass
