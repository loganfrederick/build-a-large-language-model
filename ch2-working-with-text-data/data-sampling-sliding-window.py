#from importlib.metadata import version
import tiktoken

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# NOTE: get_encoding needs an internet connection, failed at coffee shop
tokenizer = tiktoken.get_encoding("gpt2")

enc_text = tokenizer.encode(raw_text)
print(len(enc_text))


enc_sample = enc_text[:50] # Done for demo purposes to get more interesting results
context_size = 4
x = enc_sample[:context_size]
y = enc_sample[1:context_size]
print(f"x: {x}")
print(f"x:     {y}")

for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]
    print(context, "---->", desired)

# Same as above but now with the tokens decoded to words
for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]
    print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))

# We've now created input-target pairs we could use for LLM training
