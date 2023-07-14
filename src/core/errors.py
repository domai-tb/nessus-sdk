from requests.adapters import Response


class NessusError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnexpectedError(NessusError):
    def __init__(self, exception: Exception):
        super().__init__(f"An unexpected Exception occured: {exception}")


class ValidationError(NessusError):
    def __init__(self, validation_on: str, validate_as: str):
        super().__init__(f"Cannot validate {validation_on} as {validate_as}!")


class NetworingError(NessusError):
    def __init__(self, method: str, uri: str):
        super().__init__(
            f"Could not connect to performing a network request: {method} {uri}"
        )


class UnexpectedNetworingError(NessusError):
    def __init__(self, method: str, uri: str, exception: Exception):
        super().__init__(
            f"An Exception occured while performing a network request: {method} {uri}\n{exception}"
        )


class StatusCodeError(NessusError):
    def __init__(self, method: str, uri: str, response: Response):
        self.status_code = response.status_code
        self.response_text = response.text
        super().__init__(
            f"Network request returned {self.status_code}:" f"\t{method} {uri}"
        )


class AuthenticationError(NessusError):
    def __init__(self, msg: str = "") -> None:
        super().__init__(
            f"Could not authenticate against the given server with given credentials.\n{msg}"
        )
