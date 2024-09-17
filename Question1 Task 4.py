import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Load SciSpaCy models (you can use en_core_sci_sm or en_ner_bc5cdr_md)
nlp_sci = spacy.load("en_ner_bc5cdr_md")  # or "en_core_sci_sm"

# Load BioBERT tokenizer and model for entity recognition
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
ner_biobert = pipeline("ner", model=model, tokenizer=tokenizer)

# Path to the text file
input_txt_file = r'C:\Users\mahak\OneDrive\Desktop\HIT137\extracted_texts.txt'

# Read the content of the text file
with open(input_txt_file, 'r', encoding='utf-8') as file:
    text = file.read()

### 1. Extract entities using SciSpacy (diseases and drugs)
sci_entities = nlp_sci(text)
sci_diseases = [ent.text for ent in sci_entities.ents if ent.label_ == "DISEASE"]
sci_drugs = [ent.text for ent in sci_entities.ents if ent.label_ == "CHEMICAL"]

print(f"SciSpacy Disease Entities: {sci_diseases}")
print(f"SciSpacy Drug Entities: {sci_drugs}")

### 2. Extract entities using BioBERT
biobert_entities = ner_biobert(text)
biobert_diseases = [ent['word'] for ent in biobert_entities if 'B-Disease' in ent['entity']]
biobert_drugs = [ent['word'] for ent in biobert_entities if 'B-Drug' in ent['entity']]

print(f"BioBERT Disease Entities: {biobert_diseases}")
print(f"BioBERT Drug Entities: {biobert_drugs}")

### 3. Compare the results:
# Total entities detected
sci_total_entities = len(sci_diseases) + len(sci_drugs)
biobert_total_entities = len(biobert_diseases) + len(biobert_drugs)

print(f"Total Entities Detected by SciSpacy: {sci_total_entities}")
print(f"Total Entities Detected by BioBERT: {biobert_total_entities}")

# Most common entities in both models
sci_common_entities = sci_diseases + sci_drugs
biobert_common_entities = biobert_diseases + biobert_drugs

# Find overlapping entities
overlap = set(sci_common_entities) & set(biobert_common_entities)
print(f"Common Entities Detected by Both Models: {overlap}")

# Unique entities detected by each model
sci_unique = set(sci_common_entities) - set(biobert_common_entities)
biobert_unique = set(biobert_common_entities) - set(sci_common_entities)

print(f"Unique Entities Detected by SciSpacy: {sci_unique}")
print(f"Unique Entities Detected by BioBERT: {biobert_unique}")
