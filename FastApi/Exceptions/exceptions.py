class ValidationException(Exception):

    def __init__(self, error_code=None, description=None, message=None):
        self.error_code = error_code or "0002"
        self.message = message or "Validation Exception"
        self.decription = description
        
    def __str__(self):
        return "Error: error_code=%s message=%s" % (
            self.error_code,
            self.message
        )