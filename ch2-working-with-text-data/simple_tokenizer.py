import re

class SimpleTokenizerV1:
    def __init__(self, vocab):
        # Store vocab as a class attribute for access in the encode and decode methods
        self.str_to_int = vocab

        # Create an inverse vocab taht maps token IDs to original text tokens
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\"]|--|\s)',text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])

        # Remove spaces before the punctuation marks
        text = re.sub(r'\s+([,.?!"()\'])',r'\1',text)

        return text
    
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\"]|--|\s)',raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
all_words = sorted(set(preprocessed))
vocab = {token:integer for integer,token in enumerate(all_words)}

tokenizer = SimpleTokenizerV1(vocab)
text = """
It's the last he painted, you know, Mrs. Gisburn said with pardonable pride.
"""
ids = tokenizer.encode(text)
print(ids)

# TODO: It seems like the "\" forwardslash character is supposed to be tokenized but my code is dropping, 
# per the book's examples.
print(tokenizer.decode(ids))

try:
    new_text = "Hello, do you like tea?"
    print(tokenizer.encode(new_text))
except KeyError as e:
    print(f"Error: Token not found in vocabulary: {e}")
