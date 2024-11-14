import logging
from functools import wraps

def setup_logger():
    """
    Sets up and returns a logger instance.
    """
    logging.basicConfig(
        level=logging.INFO,  # Set logging level (DEBUG, INFO, WARNING, etc.)
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),  # Output to the console
            logging.FileHandler("xml_processing.log", mode='w')  # Log to a file
        ]
    )
    return logging.getLogger(__name__)

def log_decorator(func):
    """
    Decorator to log the start and end of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Running '{func.__name__}' function.")
        result = func(*args, **kwargs)
        logger.info(f"Finished '{func.__name__}' function.")
        return result
    return wrapper
