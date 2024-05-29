class DuplicateError(Exception):
    def __init__(self, message='Duplicate found'):
        self.message = message
        super().__init__(message)
        
class NotFoundException(Exception):
    """Custom exception class for not found errors."""
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)