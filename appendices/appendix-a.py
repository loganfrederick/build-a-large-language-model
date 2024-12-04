import torch

tensor0d = torch.tensor(1)

tensor3d = torch.tensor([[
    [1,2], [3,4],
    [5,6], [7,8]
]])

# Tensor Data Types
# Default 64 bit integer data type from Python
print(tensor3d.dtype)

floatvec = torch.tensor([1.0, 2.0, 3.0])
print(floatvec.dtype)

floatvec = tensor3d.to(torch.float16)
print(floatvec.dtype)

