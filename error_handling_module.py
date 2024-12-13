
import logging

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler
        file_handler = logging.FileHandler('error.log')
        file_handler.setLevel(logging.ERROR)

        # Create a formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(file_handler)

    def handle_file_operation_error(self, function_name, error):
        self.logger.error(f"Error in {function_name}: {error}")
        raise Exception(f"File operation failed: {error}")

    def validate_file_params(self, content_encoding, content_text):
        if not content_encoding:
            raise ValueError("'content.encoding' parameter is required.")
        if not content_text:
            raise ValueError("'content.content' parameter is required.")
