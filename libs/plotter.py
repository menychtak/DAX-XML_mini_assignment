import matplotlib.pyplot as plt
from libs.logger_config import *

@log_decorator
def plot_publications_per_year(yearly_records, logger):
    """
    Plots a bar chart of the number of publications per year.
    """
    years = sorted(yearly_records.keys())  # Get sorted years
    counts = [yearly_records[year] for year in years]

    logger.info("Plotting publications per year...")

    plt.figure(figsize=(10, 6))
    plt.bar(years, counts, color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.title('Publications per Year')
    plt.xticks(years[::5], rotation=45)
    plt.tight_layout()
    plt.show()
