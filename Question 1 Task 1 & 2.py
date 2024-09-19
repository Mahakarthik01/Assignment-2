# python -m venv myenv
# myenv\Scripts\activate
# pip install spacy
# pip install scispacy
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.3.0/en_core_sci_sm-0.3.0.tar.gz
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.3.0/en_ner_bc5cdr_md-0.3.0.tar.gz
# pip install transformers
# pip install torch
# pip install pandas
import os
import csv

# Function to extract text from specified columns in the CSV files and save it to a .txt file
def extract_text_from_csv(csv_files, column_names, output_file):
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        # Loop through the CSV files and corresponding column names
        for file_path, column_name in zip(csv_files, column_names):
            with open(file_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                # Write the content from the specified column to the output .txt file
                for row in reader:
                    if column_name in row:
                        txt_file.write(row[column_name] + '\n')

    print(f"Text extracted and saved in '{output_file}'.")

# Paths to your CSV files
csv_files = [
    'C:/Users/mahak/OneDrive/Documents/CSV1.csv',
    'C:/Users/mahak/OneDrive/Documents/CSV2.csv',
    'C:/Users/mahak/OneDrive/Documents/CSV3.csv',
    'C:/Users/mahak/OneDrive/Documents/CSV4.csv'
]

# Corresponding column names for each CSV file
column_names = ['SHORT-TEXT', 'TEXT', 'TEXT', 'TEXT']

# Output file path
output_file = 'C:/Users/mahak/OneDrive/Desktop/HIT137/extracted_texts.txt'

# Call the function to extract text
extract_text_from_csv(csv_files, column_names, output_file)



