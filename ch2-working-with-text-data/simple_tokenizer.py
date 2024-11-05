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
    
