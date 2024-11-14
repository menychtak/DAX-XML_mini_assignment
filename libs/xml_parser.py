import xml.sax
from libs.logger_config import *

class YearCountHandler(xml.sax.ContentHandler):
    def __init__(self, tag_name):
        self.year_counts = {}  # Dictionary to store the count per year
        self.current_tag = ""  # Track the current tag
        self.year_content = ""  # Store the content of each year tag
        self.tag_name = tag_name  # Use a configurable tag name

    def startElement(self, tag, attrs):
        self.current_tag = tag  # Update current tag
        if self.current_tag == self.tag_name:
            self.year_content = ""  # Reset year content for each specified tag

    def endElement(self, tag):
        if tag == self.tag_name:
            year = self.year_content.strip()
            if year:  # Ensure that year content is not empty
                if year in self.year_counts:
                    self.year_counts[year] += 1  # Increment the count for the year
                else:
                    self.year_counts[year] = 1  # Initialize count for the first appearance of this year

    def characters(self, content):
        if self.current_tag == self.tag_name:
            self.year_content += content  # Accumulate content of the specified tag

@log_decorator
def parse_xml(xml_file_path, logger, tag_name):
    """
    Parses the XML file using the YearCountHandler with a configurable tag name
    and returns the year counts.
    """
    logger.info(f"Processing XML file: {xml_file_path}")
    parser = xml.sax.make_parser()
    handler = YearCountHandler(tag_name=tag_name)
    parser.setContentHandler(handler)
    
    parser.parse(xml_file_path)  # Parse the XML file
    
    return handler.year_counts
