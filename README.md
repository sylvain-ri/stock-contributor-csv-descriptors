# Parser for descriptors CSV files for Stock Websites
Output a CSV file for each selected stock website (such as Adobe Stock, Shutterstock, ...), for photo or video descriptions.

Most websites accept a CSV files instead of manually enter each field for each uploaded file.
Nevertheless their format differs slightly, and this script tries to output one csv file for each supported website.


# Installation
Usual `pip install stock_contributor_csv_descriptors`
Create a venv before if desired.

# Run
To get the initial CSV for your files:
`generate-master-csv <folder_with_media> <output_csv>`

`stock_contributor_csv_descriptors <descriptor_file.csv> <output_folder/basename_without.csv> -d <folder_with_media>` <br />
The optional argument `-d` also checks that the filenames correspond to the one in the CSV file.

# Notes
- Contributions are welcome.
- Project barely started, expect bugs
- You can define a new output by changing the `OutputFormat-StockContribution.csv`. 
Duplicate the template, and adapt it to the new website format.

# Author
Started by Sylvain Riondet in December 2022.

