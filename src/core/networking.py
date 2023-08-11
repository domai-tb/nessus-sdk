import json
from json import JSONDecodeError
from urllib.parse import urlsplit

import backoff
from requests import request
from requests.exceptions import ConnectionError, Timeout
from requests.packages import urllib3
from validators import url

from . import errors as NErrors


class Networking:
    __shared_headers: dict = {
        "Content-type": "application/json",
        "Accept": "application/json",
    }

    __shared_base_url: str = ""

    def __init__(self, base_url: str | None = None, verify_ssl: bool = False) -> None:
        self.verify_ssl = verify_ssl

        if base_url is not None:
            Networking.__shared_base_url = self.__parse_base_url(base_url)

        # Disable SSL Warning
        if not verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @property
    def base_url(self) -> str:
        """
        Get Server URL.

        Returns:
            str: The Base URL all Networking object use.
        """
        return Networking.__shared_base_url

    @base_url.setter
    def base_url(self, base_url: str) -> None:
        """
        Set Server URL.
        """
        Networking.__shared_base_url = self.__parse_base_url(base_url)

    @property
    def headers(self) -> dict:
        """
        Get headers

        Returns:
            dict: The headers all Networking objects use.
        """
        return Networking.__shared_headers

    @headers.setter
    def headers(self, header: dict) -> None:
        """
        Set headers.
        """
        Networking.__shared_headers = header

    @headers.deleter
    def headers(self) -> None:
        """
        Delete headers.
        """
        Networking.__shared_headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
        }

    def GET(
        self, path: str, params: dict = {}, headers: dict = __shared_headers
    ) -> dict | str:
        """
        Perform a GET request.

        Returns:
            dict | str: Parsed Response as JSON object or Response body as string.
        """
        return self.__request("GET", path, params, headers)

    def POST(
        self, path: str, params: dict = {}, headers: dict = __shared_headers
    ) -> dict | str:
        """
        Perform a POST request.

        Returns:
            dict | str: Parsed Response as JSON object or Response body as string.
        """
        return self.__request("POST", path, params, headers)

    def DELETE(self, path: str, headers: dict = __shared_headers) -> dict | str:
        """
        Perform a DELETE request.

        Returns:
            dict | str: Parsed Response as JSON object or Response body as string.
        """
        return self.__request("DELETE", path, headers)

    def PUT(
        self, path: str, params: dict = {}, headers: dict = __shared_headers
    ) -> dict | str:
        """
        Perform a PUT request.

        Returns:
            dict | str: Parsed Response as JSON object or Response body as string.
        """
        return self.__request("PUT", path, params, headers)

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
            raise NErrors.ValidationError(base_url, "URL")

        splitted_url = urlsplit(base_url)
        return f"{splitted_url.scheme}://{splitted_url.netloc}"

    @backoff.on_exception(backoff.expo, NErrors.NetworingError, max_tries=3)
    def __request(
        self,
        method: str,
        path: str,
        params: dict = {},
        headers: dict = __shared_headers,
    ) -> dict | str:
        """
        Perfrom a network request to given path of base URL.

        Args:
            path (str): API Path, e.g. /session
            method (str): One of GET, POST, PUT, DELETE
            params (dict, optional): Parameter / Body of POST-Request. Defaults to {}.
            headers (dict, optional): The Headers to send with the request.
                                      By Default it will use a shared object over all instances.

        Raises:
            NErrors.UnexpectedNetworingError: Indicates that the network request could not performed.
            NErrors.ResponseParsingError: Indicates the the response is malicious formated.
            NErrors.StatusCodeError: The response was not successfully.

        Returns:
            dict | str: Parsed Response as JSON object or Response body as string.
        """
        try:
            response = request(
                method=method,
                url=self.base_url + path,
                data=json.dumps(params) if params != {} else None,
                headers=headers,
                verify=self.verify_ssl,
                timeout=10,
            )
        except ConnectionError:
            raise NErrors.NetworingError(method, self.base_url + path)
        except Timeout:
            raise NErrors.NetworingError(method, self.base_url + path)
        except Exception as e:
            raise NErrors.UnexpectedNetworingError(method, self.base_url + path, e)

        if response.status_code != 200:
            raise NErrors.StatusCodeError(method, self.base_url + path, response)

        try:
            return response.json()
        except JSONDecodeError:
            return response.text
        except Exception:
            raise NErrors.ResponseParsingError("JSON or String")
