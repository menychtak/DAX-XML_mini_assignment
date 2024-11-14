# XML Publication Analyzer

This mini-assignment demonstrates how to efficiently perform aggregation and extract tag content from a large XML file to derive meaningful insights. It utilizes a SAX abstract class for parsing the XML file, ensuring minimal memory usage while processing large datasets. After completing the aggregation, the resulting dictionary is visualized through a bar-chart using matplotlib.

## Folder Structure

The project follows this structure:
```
.
├── code
│   └── main.py               # Main script to run the XML analyzer
├── dataset
│   └── file.xml              # Place your XML files here (e.g., file.xml)
├── libs
│   ├── xml_parser.py         # XML parsing logic
│   ├── logger_config.py      # Logger setup
│   ├── file_handler.py       # File handling utilities
│   └── plotter.py            # Plotting functions
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.x
- Required packages listed in `requirements.txt`

To install the necessary packages, run:
```bash
pip install -r requirements.txt
```

### Dataset

To replicate the results, download the XML dataset from [this link](https://dblp.org/xml/release/dblp-2024-10-01.xml.gz), unzip it, and place the `.xml` file in the `dataset` folder. Rename it to `file.xml` or update the path in the code.

### Usage

1. Add your XML file to the `dataset` folder.
2. In `main.py`, set the `tag_name` variable to the tag you want to count. For example, to count occurrences of `<year>` tags, set:
   ```python
   tag_name = "year"
   ```
3. Run the main script:
   ```bash
   python code/main.py
   ```

### Output

- The script will output a dictionary with counts of each year (or specified tag) and display a bar chart of the publication counts.

### Example

An example XML file containing `<year>` tags can be found in the DBLP dataset linked above. The dictionary output will look something like:
```json
{"2020": 100, "2021": 150, "2022": 200}
```

The program will also display a bar chart with the counts per year.

---

### License

This project is licensed under the MIT License. See the LICENSE file for details.
