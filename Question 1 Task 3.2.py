# pip install trasnformers 
from transformers import AutoTokenizer
from collections import Counter
import csv

# Function to tokenize the text and count unique tokens
def count_unique_tokens(file_path, top_n=30):
    # Load the AutoTokenizer from the 'bert-base-uncased' model (you can replace it with another model if needed)
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    
    # Count occurrences of each token
    token_counts = Counter(tokens)
    
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

