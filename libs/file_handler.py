import os
from libs.logger_config import *

@log_decorator
def get_xml_file_path(filename: str):
    """
    Returns the relative path of the XML file from the current script's location.
    """
    return os.path.join(os.path.dirname(__file__), f'../dataset/{filename}')
