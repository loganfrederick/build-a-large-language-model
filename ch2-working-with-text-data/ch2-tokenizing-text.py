with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("Total number of character:", len(raw_text))
print(raw_text[:99])

# Different tokenizations
import re
text = "Hello, world. This, is a test."
result = re.split(r'([,.]|\s)', text)
print(result)

result = [item for item in result if item.strip()]
print(result)

text = "Hello, world. Is this-- a test?"
result = re.split(r'([,.:;?_!"()\"]|--|\s)',text)
print(result)

# Apply tokenization to Edith Wharton The Verdict"

preprocessed = re.split(r'([,.:;?_!"()\"]|--|\s)',raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
# NOTE: The book says the bleow should output 4690 but I got 4519
print(len(preprocessed))
print(preprocessed[:30])

# List all unique tokens and sort htem alphabetically to determine vocab size
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i>=50:
        break
