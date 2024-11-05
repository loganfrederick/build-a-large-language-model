import re

class SimpleTokenizerV2:
    def __init__(self, vocab):
        # Store vocab as a class attribute for access in the encode and decode methods
        self.str_to_int = vocab

        # Create an inverse vocab taht maps token IDs to original text tokens
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\"]|--|\s)',text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        # New from V1
        # Replaces unknown words by unk tokens
        preprocessed = [item if item in self.str_to_int
                        else "<|unk|>" for item in preprocessed]

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

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer,token in enumerate(all_tokens)}

for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text3 = " <|endoftext|> ".join((text1,text2))
print(text3)

tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.encode(text3))

# This allows us to see that the Edith Wharton book "The Verdict"
# does not contain the words Hello and Palace when they are compared using
# the encoder and decoder.

print(tokenizer.decode(tokenizer.encode(text3)))

# Other Common Special Tokens
# <BOS>
# <EOS>
# <PAD>

# GPT does not use an "unk" token
# Instead a byte pair encoding taught later