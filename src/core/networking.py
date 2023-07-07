import json
from json import JSONDecodeError
from urllib.parse import urlsplit

from requests import request
from requests.packages import urllib3
from validators import url

from . import errors as NessusErrors


class Networking:
    def __init__(
        self, base_url: str, verify_ssl: bool = False, headers: dict = {}
    ) -> None:
        self.base_url = self.__parse_base_url(base_url)
        self.verify_ssl = verify_ssl
        self.headers = headers

        # Disable SSL Warning
        if not verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def get(self, path: str) -> dict | str:
        """Perform a GET request."""
        return self.__request("GET", path)

    def post(self, path: str, params: dict) -> dict | str:
        """Perform a POST request."""
        return self.__request("POST", path, params)

    def delete(self, path: str) -> dict | str:
        """Perform a DELETE request."""
        return self.__request("DELETE", path)

    def put(self, path: str) -> dict | str:
        """Perform a PUT request."""
        return self.__request("PUT", path)

    def __parse_base_url(self, base_url: str) -> str:
        """
        Parse and check base URL to be in the expected format.
        E.g. https://example.com

        Args:
            base_url (str): The URL to check and parse.

        Returns:
            str: The parsed base URL.
        """
        if not url(base_url):
            raise NessusErrors.ValidationError(base_url, "URL")

        splitted_url = urlsplit(base_url)
        return f"{splitted_url.scheme}://{splitted_url.netloc}"

    def __request(self, method: str, path: str, params: dict = {}) -> dict | str:
        """
        Perfrom a Request to Nessus API.

        Args:
            path (str): API Path, e.g. /session
            method (str): One of GET, POST, PUT, DELETE
            params (dict, optional): Parameter / Body of POST-Request. Defaults to None.

        Returns:
            dict|str: Parsed Response as JSON object or Response body as string.
        """
        try:
            response = request(
                method=method,
                url=self.base_url + path,
                data=json.dumps(params),
                headers=self.headers,
                verify=self.verify_ssl,
            )
        except Exception as e:
            raise NessusErrors.NetworingError(method, self.base_url + path, e)

        try:
            return response.json()
        except JSONDecodeError:
            return response.text
        except Exception as e:
            raise NessusErrors.NetworingError(method, self.base_url + path, e)
