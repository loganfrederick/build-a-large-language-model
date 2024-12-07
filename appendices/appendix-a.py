import torch

tensor0d = torch.tensor(1)

tensor2d = torch.tensor([[1,2,3],[4,5,6]])

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

# Common PyTorch Tensor Ops
print(tensor3d.shape)

print(tensor3d.reshape(1,2,4))

print(tensor3d.view(1,2,4))

# UserWarning: The use of `x.T` on tensors of dimension other than 2 to reverse their shape
# is deprecated and it will throw an error in a future release. 
# Consider `x.mT` to transpose batches of matrices 
# or `x.permute(*torch.arange(x.ndim - 1, -1, -1))` to reverse the dimensions of a tensor.
print(tensor3d.T)

# RuntimeError: Expected size for first two dimensions of batch2 tensor to be: [2, 2] but got: [2, 4].
#print(tensor3d.matmul(tensor3d.T))
#print(tensor3d @ tensor3d.T)

print(tensor2d.matmul(tensor2d.T))
print(tensor2d @ tensor2d.T)
