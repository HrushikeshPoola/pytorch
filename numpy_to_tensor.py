import torch
import numpy as np

 # lets create a tensor and then try to convert it into numpy array

a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

'''
    - There is a catch here at hardware level
        - if the tensor is created at CPU level then both numpy and tensor will share the same memory
        and changing one value will change the value of the other array too  
'''

# numpy to torch

a = np.ones(5)
print(a)

b = torch.from_numpy(a)
print(b)
