
from transformers import AutoTokenizer
from collections import Counter
import csv

# Function to tokenize the text and count unique tokens in chunks to avoid memory issues
def count_unique_tokens(file_path, top_n=30, chunk_size=1024):  # Process text in 1KB chunks
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased', use_fast=True)
    token_counts = Counter()

    # Read the text file in chunks
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            # Read a chunk of text
            chunk = file.read(chunk_size)
            if not chunk:
                break
            
            # Tokenize the chunk (removed the deprecated argument)
            tokens = tokenizer.tokenize(chunk)
            
            # Update token counts
            token_counts.update(tokens)

    # Get the top 'n' most common tokens
    top_tokens = token_counts.most_common(top_n)

    # Save the top tokens and their counts into a CSV file
    output_csv = 'top30_tokens.csv'
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Token', 'Count'])
        writer.writerows(top_tokens)
    
    print(f"Top {top_n} tokens saved in '{output_csv}'.")

# Provide the path to your extracted_texts.txt file
file_path = 'C:/Users/mahak/OneDrive/Desktop/HIT137/extracted_texts.txt'

# Call the function to count tokens and store the top 30
count_unique_tokens(file_path)

