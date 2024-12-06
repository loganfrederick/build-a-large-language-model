# Last step in preparing the input text for LLM training
# Convert the token IDs into embedding vectors

import torch

# Preliminary step: Random vector initialization

input_ids = torch.tensor([2,3,5,1])

vocab_size = 6
output_dim = 3

# Using these variables, we can create an embedding layer
torch.manual_seed(123) # TODO: How does torch.manual_seed work internally?
embedding_layer = torch.nn.Embedding(vocab_size, output_dim) # TODO: How does Embedding class work?
print(embedding_layer.weight)

