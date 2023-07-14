from core import NErrors, Networking


class SessionAPI(Networking):
    def create(self, username: str, password: str) -> dict:
        """
        Create a new session token for the given user. Certificate based logins require no parameters.

        Args:
            username (str): The username for the person who is attempting to log in.
            password (str): 	The password for the person who is attempting to log in.

        Raises:
            NErrors.AuthenticationError: Indicate that an error occured in the authentication process.
            NErrors.UnexpectedError: Indicate that an error occured in the destroy process.

        Returns:
            dict: API-Token of given user and MD5-Sums:

                    {
                        "md5sum_wizard_templates": {string},
                        "token": {string},
                        "md5sum_tenable_links": {string}
                    }
        """
        try:
            return dict(
                self.post(
                    "/session", params={"username": username, "password": password}
                )
            )
        except NErrors.StatusCodeError as e:
            raise NErrors.AuthenticationError(e.response_text)
        except Exception as e:
            raise NErrors.UnexpectedError(e)

    def destroy(self) -> None:
        """
        Logs the current user out and destroys the session.

        Raises:
            NErrors.AuthenticationError: No session found to destroy.
            NErrors.UnexpectedError: Indicate that an error occured in the destroy process.
        """
        try:
            self.delete("/session")
            del self.headers
        except NErrors.StatusCodeError as e:
            if e.status_code == 401:
                raise NErrors.AuthenticationError("Returned 401, no session exists.")
            else:
                raise NErrors.UnexpectedError(e)
        except NErrors.NetworingError:
            raise NErrors.AuthenticationError("Could not get an response.")
        except Exception as e:
            raise NErrors.UnexpectedError(e)

    def edit(self, name: str = None, email: str = None) -> dict:
        """
        Changes settings for the current user.

        Args:
            name (str, optional): Full name for the user. Defaults to None.
            email (str, optional): Email address for the user. Defaults to None.

        Returns:
            dict: Returns the user session data.
        """
        return dict(self.put("/session", params={"name": name, "email": email}))

    def get(self) -> dict:
        """
        Returns the user session data.

        Returns:
            dict: Returns the user session data.

                    {
                        "id": {string},
                        "username": {string},
                        "email": {string},
                        "name": {string},
                        "type": {string},
                        "permissions": {integer},
                        "lastlogin": {integer},
                        "container_id": {integer},
                        "groups": []
                    }
        """
        return dict(self.get("/session"))

    def password(self, password: str, current_password: str) -> None:
        """
        Changes password for the current user.

        Args:
            password (str): New password for the user.
            current_password (str): Current password for the user.
        """
        self.put(
            "/session/chpasswd",
            params={"password": password, "current_password": current_password},
        )

    def keys(self) -> dict:
        """
        Generates API Keys for the current user.

        Returns:
            dict: Returned if the user API Keys were generated.

                    {
                        "accessKey": {string},
                        "secretKey": {string}
                    }
        """
        return dict(self.put("/session/keys"))
