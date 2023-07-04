import json
from json import JSONDecodeError

from requests import request


class BaseAPI:
    def __init__(self, nessusAPI):
        self.api = nessusAPI

    def get(self, path: str) -> dict | str:
        return self.request("GET", path)

    def post(self, path: str, params: dict) -> dict | str:
        return self.request("POST", path, params)

    def request(self, method: str, path: str, params: dict = dict()) -> dict | str:
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
                url=self.api.server_url + path,
                data=json.dumps(params),
                headers=self.api.header,
                verify=self.api.verify_ssl,
            )
        except Exception:
            # TODO: Raise exception
            return {}
        if response.status_code != 200:
            # TODO: Raise exception
            return {}
        try:
            return response.json()
        except JSONDecodeError:
            return response.text
        except Exception:
            # TODO: Raise exception
            return {}
