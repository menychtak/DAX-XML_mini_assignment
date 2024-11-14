import sys
import os

# Add the parent directory to the system path so Python can find the 'libs' folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from libs.xml_parser import parse_xml
from libs.logger_config import setup_logger
from libs.file_handler import get_xml_file_path
from libs.plotter import plot_publications_per_year

import time

def main():
    # Set up logger
    logger = setup_logger()

    # Measure start time
    start_time = time.time()

    # Get the XML file path
    xml_file_path = get_xml_file_path("file.xml")
    tag_name = "year"

    # Parse the XML file and get publication counts per year
    yearly_records = parse_xml(xml_file_path, logger, tag_name)

    # Measure end time and calculate elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Time taken: {elapsed_time:.2f} seconds")

    # Log the publication counts
    logger.info(f"Yearly publication counts: {yearly_records}")

    # Plot the results
    xlabel = 'Year'
    ylabel = 'Number of Publications'
    title = 'Publications per Year'
    plot_publications_per_year(yearly_records, logger, xlabel, ylabel, title)

if __name__ == "__main__":
    main()
