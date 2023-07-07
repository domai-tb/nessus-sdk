class NessusError(Exception):
    pass


class UnexpectedError(NessusError):
    def __init__(self, exception: Exception):
        super().__init__(f"An unexpected Exception occured: {exception}")


class ValidationError(NessusError):
    def __init__(self, validation_on: str, validate_as: str):
        super().__init__(f"Cannot validate {validation_on} as {validate_as}!")


class NetworingError(NessusError):
    def __init__(self, method: str, uri: str, exception: Exception):
        super().__init__(
            f"An Exception occured while performing a network request:"
            f"\t{method} {uri}\n{exception}"
        )
