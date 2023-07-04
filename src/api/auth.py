import re


class AuthenticationAPI:
    def __init__(self, nessusAPI):
        self.api = nessusAPI

    def login(self) -> bool:
        """
        Login to Nessus server.

        Returns:
            bool: True if successful login, False otherwise.
        """
        self.add_apitoken_by_nessus6js_to_header()

        params = {"username": self.api.username, "password": self.api.password}
        response = self.api.base.post("/session", params)
        if not response:
            return False
        else:
            sessiontoken = response["token"]
            self.api.header["X-Cookie"] = f"token={sessiontoken}"
            response = self.api.base.request("PUT", "/session/keys")
            if not response:
                return False
            else:
                accessKey, secretKey = response["accessKey"], response["secretKey"]
                self.api.header[
                    "X-ApiKeys"
                ] = f"accessKey={accessKey};secretKey={secretKey};"
                return True

    def add_apitoken_by_nessus6js_to_header(self) -> bool:
        """
        Read API-Token from JavaScript file named "nessus6.js".
        The API-Key is needed to bypass Nessus Professional limitation.

        Returns:
            bool: True if an valid API key could parsed. Otherwise False.
        """
        response = self.api.base.get(self.api.server_url + "/nessus6.js")
        if not response:
            return False
        else:
            apiKey = re.findall(
                r"[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}",
                response.text,
            )[0]
            if apiKey is None:
                return False
            self.api.header["X-Api-Token"] = apiKey
            return True
