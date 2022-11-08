import torch


print(torch.empty(1))
print(torch.empty(2,3))
print(torch.ones(2,2,2,3))

'''
    - similar to ones and empty
     - ones
     - zeros
     - rand
     - give dtype similar to numpy
        - torch.float16
        - torch.float32

'''

# now lets create two tensors with 2*2 matrix and rand values

x = torch.rand(2,2)
y = torch.rand(2,2)

print(x)
print(y)
# basic operations on both tensors

print(x+y) # torch.add(x,y) will do the same functionality
'''
    y.add_(x) -> will do the inplace addition of the values and store in y
    y.mul_(x) -> will do the inplace multiplication
    y.div_(x) -> inplace division

    similar to torch.add(x,y)
        - torch.sub(x,y) = x - y
        - torch.mul(x,y) = x * y
        - torch.div(x,y) = x / y
'''

'''
    similar to numpy how we access specific group of elements we can achieve same using tensors
'''

arr = torch.rand(5,3)

# This print the whole 2D array
print(arr)

# to print a particular row of the 2D matrix
print(arr[1,:])

# to get only a particular column of matrix
print(arr[:,1])

# to access one particular element
print(arr[1,2])

# ** If we have only one element inside tensor then we can use .item() to access the value of the element **
print(arr[1,2].item())


'''
    How to reshape the given tensor
        - using view() method
'''

arr = torch.rand(6,5)

print(arr.view(3,10))
print(arr.view(-1,10))

