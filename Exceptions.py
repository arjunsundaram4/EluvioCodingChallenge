from logging import exception


class BadAuthorizationException(Exception):
    def __init__(self, *args: object) -> None:
        print("Authorization header was missing/invalid")
        super().__init__(*args)


class TooManyRequestException(Exception):
    def __init__(self, *args: object) -> None:
        print("Too many concurent requests made")
        super().__init__(*args)


class NotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        print("No response found for ID")
        super().__init__(*args)


class APIException(Exception):
    def __init__(self, *args: object) -> None:
        print("Error Calling the API")
        super().__init__(*args)
