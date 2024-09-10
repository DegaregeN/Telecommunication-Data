import logging
import os

class Logger:
    """Logger class for logging messages to a file."""

    def __init__(self, file_name: str, basic_level=logging.INFO):
        """Initialize logger class with file name to be written and default log level.

        Args:
            file_name (str): Name of the log file.
            basic_level (int, optional): Log level. Defaults to logging.INFO.
        """
        # Create logs directory if it doesn't exist
        logs_dir = '../logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Gets or creates a logger
        logger = logging.getLogger(__name__)

        # Set log level
        logger.setLevel(basic_level)

        # Define file handler and set formatter
        file_handler = logging.FileHandler(f'{logs_dir}/{file_name}')
        formatter = logging.Formatter(
            '%(asctime)s : %(levelname)s : %(name)s : %(message)s', '%m-%d-%Y %H:%M:%S'
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        self.logger = logger

    def get_app_logger(self) -> logging.Logger:
        """Return the logger object.

        Returns:
            logging.Logger: Logger object.
        """
        return self.logger