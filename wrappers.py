import numpy as np

# function to pretty print a numpy array
def pretty_print_array(array):
    np.set_printoptions(precision=3, suppress=True)
    print(array)

# make a random array of shape (100, 100) with x, y, z coordinates
@pretty_print_array
def make_random_array(x, y, z):
    return np.random.rand(x, y, z)

make_random_array(100, 100, 3)





