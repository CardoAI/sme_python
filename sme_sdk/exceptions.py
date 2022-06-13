class LoginFailed(Exception):
    def __init__(self, message, status_code):
        super().__init__(message, status_code)


class BatchCreationFailed(Exception):
    def __init__(self, message, status_code):
        super().__init__(message, status_code)


class BatchResultRetrieveFailed(Exception):
    def __init__(self, message, status_code):
        super().__init__(message, status_code)
