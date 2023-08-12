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
        self.response_text = response.text
        self.status_code = response.status_code
        super().__init__(
            f"Network request returned {response.status_code}\n"
            f"{method} {uri}: {response.text}"
        )


class AuthenticationError(NessusError):
    def __init__(self, msg: str = "") -> None:
        super().__init__(
            f"Could not authenticate against the given server with given credentials.\n{msg}"
        )


class MagicAPIKeyNotFound(NessusError):
    def __init__(self) -> None:
        super().__init__("The Magic Nessus API key could not extracted... :(")


class NotFoundError(NessusError):
    def __init__(self, object: str) -> None:
        super().__init__(f"'{object}' could not be found / {object} invalid")


class InsufficientPermissionsError(NessusError):
    def __init__(self) -> None:
        super().__init__("Insufficient Permissions.")


class InternalServerError(NessusError):
    def __init__(self) -> None:
        super().__init__("Internal Nessus Server Error.")