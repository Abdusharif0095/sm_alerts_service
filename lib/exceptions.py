class SignException(Exception):
    def __init__(self, message: str):
        self.message = message


class SystemError(Exception):
    def __init__(self, message):
        self.message = message


class DBError(Exception):
    def __init__(self, message):
        self.message = message
