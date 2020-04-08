# These are the libraries will be used for this lab.

import numpy as np 
import matplotlib.pyplot as plt
import torch
import pandas as pd

# Convert 2D List to 2D Tensor
twoD_list = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
twoD_tensor = torch.tensor(twoD_list)
print("The New 2D Tensor: ", twoD_tensor)

# Try tensor_obj.ndimension(), tensor_obj.shape, tensor_obj.size()
print("The dimension of twoD_tensor: ", twoD_tensor.ndimension())
print("The shape of twoD_tensor: ", twoD_tensor.shape)
print("The shape of twoD_tensor: ", twoD_tensor.size())

# Convert tensor to numpy array; Convert numpy array to tensor
twoD_numpy = twoD_tensor.numpy()
print("Tensor -> Numpy Array:")
print("The numpy array after converting: ", twoD_numpy)
print("Type after converting: ", twoD_numpy.dtype)
print("================================================")

new_twoD_tensor = torch.from_numpy(twoD_numpy)
print("Numpy Array -> Tensor:")
print("The tensor after converting:", new_twoD_tensor)
print("Type after converting: ", new_twoD_tensor.dtype)

# Try to convert the Panda Dataframe to tensor
df = pd.DataFrame({'a':[11,21,31],'b':[12,22,312]})
print("Pandas Dataframe to numpy: ", df.values)
print("Type BEFORE converting: ", df.values.dtype)

print("================================================")

new_tensor = torch.from_numpy(df.values)
print("Tensor AFTER converting: ", new_tensor)
print("Type AFTER converting: ", new_tensor.dtype)


# Practice: try to convert Pandas Series to tensor
df = pd.DataFrame({'A':[11, 33, 22],'B':[3, 3, 2]})

tensor = torch.from_numpy(df.values)
print(tensor)

tensor1 = torch.tensor(df.values)
print(tensor1)

# Use tensor_obj[row, column] and tensor_obj[row][column] to access certain position
tensor_example = torch.tensor([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print("What is the value on 2nd-row 3rd-column? ", tensor_example[1, 2])
print("What is the value on 2nd-row 3rd-column? ", tensor_example[1][2])


# Use tensor_obj[begin_row_number: end_row_number, begin_column_number: end_column number] 
# and tensor_obj[row][begin_column_number: end_column number] to do the slicing
tensor_example = torch.tensor([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print("What is the value on 1st-row first two columns? ", tensor_example[0, 0:2])
print("What is the value on 1st-row first two columns? ", tensor_example[0][0:2])



'''
But we can't combine using slicing on row and pick one column by using the code 
tensor_obj[begin_row_number: end_row_number][begin_column_number: end_column number]. 
The reason is that the slicing will be applied on the tensor first. The result type will
 be a two dimension again. The second bracket will no longer represent the index of the column
  it will be the index of the row at that time. Let us see an example.
'''
# Give an idea on tensor_obj[number: number][number]
tensor_example = torch.tensor([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
sliced_tensor_example = tensor_example[1:3]
print("1. Slicing step on tensor_example: ")
print("Result after tensor_example[1:3]: ", sliced_tensor_example)
print("Dimension after tensor_example[1:3]: ", sliced_tensor_example.ndimension())
print("================================================")
print("2. Pick an index on sliced_tensor_example: ")
print("Result after sliced_tensor_example[1]: ", sliced_tensor_example[1])
print("Dimension after sliced_tensor_example[1]: ", sliced_tensor_example[1].ndimension())
print("================================================")
print("3. Combine these step together:")
print("Result: ", tensor_example[1:3][1])
print("Dimension: ", tensor_example[1:3][1].ndimension())

# Use tensor_obj[begin_row_number: end_row_number, begin_column_number: end_column number] 
tensor_example = torch.tensor([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print("What is the value on 3rd-column last two rows? ", tensor_example[1:3, 2])

# Practice: Use slice and index to change the values on the matrix tensor_ques.
tensor_ques = torch.tensor([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
tensor_ques = tensor_ques[-2:,1]
print(tensor_ques)

''' Solution
tensor_ques[1:3, 1] = 0
print("The result: ", tensor_ques)
'''

# Calculate [[1, 0], [0, 1]] + [[2, 1], [1, 2]]
X = torch.tensor([[1, 0],[0, 1]]) 
Y = torch.tensor([[2, 1],[1, 2]])
X_plus_Y = X + Y
print("The result of X + Y: ", X_plus_Y)

# Calculate 2 * [[2, 1], [1, 2]]
Y = torch.tensor([[2, 1], [1, 2]]) 
two_Y = 2 * Y
print("The result of 2Y: ", two_Y)


# Calculate [[1, 0], [0, 1]] * [[2, 1], [1, 2]]
X = torch.tensor([[1, 0], [0, 1]])
Y = torch.tensor([[2, 1], [1, 2]]) 
X_times_Y = X * Y
print("The result of X * Y: ", X_times_Y)


# Calculate [[0, 1, 1], [1, 0, 1]] * [[1, 1], [1, 1], [-1, 1]]
A = torch.tensor([[0, 1, 1], [1, 0, 1]])
B = torch.tensor([[1, 1], [1, 1], [-1, 1]])
A_times_B = torch.mm(A,B)
print("The result of A * B: ", A_times_B)




# Practice: Calculate the product of two tensors (X and Y) with different sizes 
# Type your code here
t1 = torch.tensor([[1,2,3],[4,5,6]])
t2 = torch.tensor([[1,2],[6,6],[3,1]])

mm = torch.mm(t1,t2)
print(mm)


# Solution
X = torch.tensor([[0, 1], [1, 2]])
Y = torch.tensor([[-1, -2, 0], [2, 1, 2]])
X_times_Y = torch.mm(X, Y)
print("The result of X * Y: ", X_times_Y)