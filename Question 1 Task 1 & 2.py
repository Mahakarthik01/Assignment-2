# python -m venv myenv
# myenv\Scripts\activate
# pip install spacy
# pip install scispacy
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.3.0/en_core_sci_sm-0.3.0.tar.gz
# pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.3.0/en_ner_bc5cdr_md-0.3.0.tar.gz
# pip install transformers
# pip install torch
# pip install pandas
import pandas as pd

# Paths to CSV files and their corresponding text columns
csv_files = {
    "C:\\Users\\shuva\\OneDrive\\Documents\\CSV1.csv": "SHORT-TEXT",
    "C:\\Users\\shuva\\OneDrive\\Documents\\CSV2.csv": "TEXT",
    "C:\\Users\\shuva\\OneDrive\\Documents\\CSV3.csv": "TEXT",
    "C:\\Users\\shuva\\OneDrive\\Documents\\CSV4.csv": "TEXT"
}

# Path for the output text file
output_txt_file = 'extracted_texts.txt'

# Open the output file in write mode
with open(output_txt_file, 'w', encoding='utf-8') as outfile:
    # Loop through each CSV file and its text column
    for csv_file, text_column in csv_files.items():
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Check if the text column exists
        if text_column in df.columns:
            # Write each text to the output file
            for text in df[text_column]:
                outfile.write(str(text) + '\n')
        else:
            # Print an error if the column is missing
            print(f"'{text_column}' column not found in {csv_file}")


