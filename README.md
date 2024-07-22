# Multinational Retail Data Centralisation Project
Overview
This project is aimed at centralising data from different sources for a retail company. The project involves extracting data from multiple databases, cleaning, transforming the data and then uploading the cleaned data into a database for querying.

- [Installation](#installation)
- [File Structure](#file-structure)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TDAYENI/multinational-retail-data-centralisation771.git

   cd multinational-retail-data-centralisation771

2. **Install the Environment from the Text File**
    The text file can be found in the environments folder

    Navigate to the directory containing the environment.yml file
    ```bash
    cd /path/to/directory
    
3. **Specify a name for the new environment during creation**
    ````bash
    conda env create -f environment.yml -n new_env_name
4. **Activate new env**
    ````bash
    conda activate myenv

## Project Structure
The project directory contains the following key files and directories:

main.py: The main script that orchestrates the data extraction, cleaning, and uploading processes.
data_extraction.py: Contains methods for extracting data from various sources such as RDS databases, PDFs, APIs, and S3 buckets.
data_cleaning.py: Contains methods for cleaning data, including replacing null values, converting date formats, and cleaning numeric data.
database_utils.py: Contains methods for managing database connections and uploading data to databases.
cred/: Directory containing credential files for accessing databases.
SQL/: Directory containing SQL scripts for database operations.


## Installation
To run this project, you need to have Python installed along with the necessary libraries. You can install the required libraries using the requirements.txt file.


Depedencies
Yaml
conda install -c anaconda sqlalchemy
pandas
pip install psycopg2
pip install tabula-py
database_utils.py
pip3 install jpype1
pip install requests
pip install boto 3
The module is responsible for connecting to the database and performing database operations.