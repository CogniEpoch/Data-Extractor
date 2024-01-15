# Data Extractor

This Python script automates the extraction of data from ZIP files, providing a flexible solution for various data sources.

## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/CogniEpoch/Data-Extractor.git
   
2. Update the script with your source and destination directories and configure ignore and stop files.
3. Run the script:
   ```bash
   python data_extractor.py

# Parameters
  - src_dir: Source directory where ZIP files are located.
  - dst_dir: Destination directory where files will be extracted.
  - ignore_files: List of files to ignore during extraction (optional).
  - stop_files: List of files to stop extraction at (optional).

>[!warning]
>Specify the src_dir and dst_dir to match your file locations.

# Example

Specify source and destination directories:
   ```bash
   src_dir = '/content/'
   dst_dir = '/content/unzipped'
   ```
Specify files to ignore and stop extraction (optional):
   ```bash
   ignore_files = ['this.zip', 'that.zip']
   stop_files = ['these.zip', 'those.zip']
   ```
>[!IMPORTANT]
>Ensure that you have a clear understanding of the files in your source directory before running the script.\
>The script extracts all ZIP files up to the specified stop files and will ignore extracting the provided ignore files (if provided).

>[!CAUTION]
>**Disclaimer:**\
>This script is for organizational purposes and assumes the user understands the structure of their data files.



  
