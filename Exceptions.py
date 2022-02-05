from logging import exception


class BadAuthorizationException(Exception):
    print("Authorization header was missing/invalid")


class TooManyRequestException(Exception):
    print("Too many concurent requests made")


class NotFoundException(Exception):
    print("No response found for ID")


class APIException(Exception):
    print("Error Calling the API")
