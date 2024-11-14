import matplotlib.pyplot as plt
from libs.logger_config import *

@log_decorator
def plot_publications_per_year(yearly_records, logger, xlabel, ylabel, title, color = "skyblue", size = (10, 6)):
    """
    Plots a bar chart of the number of publications per year.
    """
    years = sorted(yearly_records.keys())  # Get sorted years
    counts = [yearly_records[year] for year in years]

    logger.info("Plotting publications per year...")

    plt.figure(figsize=size)
    plt.bar(years, counts, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(years[::5], rotation=45)
    plt.tight_layout()
    plt.show()
