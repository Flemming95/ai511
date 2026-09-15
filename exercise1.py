from itertools import chain, combinations

# Task 2 - Printing 
#Using formatted print 
def isolate(arg1, arg2, arg3, arg4, arg5):
    print(f"{arg1}     {arg2}     {arg3} {arg4} {arg5}")

isolate(1, 2, 3, 4, 5)

# Using sep and end parameters
def isolate2(arg1, arg2, arg3, arg4, arg5):
    print(arg1, arg2, arg3, sep="     ", end=" ")
    print(arg4, arg5)

isolate2(6, 7, 8, 9, 10)

# Task 3* - Slicing Strings
def first_half(value):
    return value[:len(value) // 2]

print(first_half("Hello World!"))  

# Remember: String slicing such as sequence[start:stop:step]
def backward(value):
    return value[::-1]

print(backward("Hello World!"))

# Task 4* - Lists
def list_ops():
    animals = ["bear", "ant", "cat", "dog"]
    animals.append("eagle")
    print(f"Added eagle to the list: {animals}")
    animals.insert(2, "fox")
    print(f"Added fox to the list at index 2: {animals}")
    animals.pop(1)
    print(f"Removed item at index 1: {animals}")
    animals.sort(reverse=False) #default value is False, so this is optional
    print(f"Sorted the list in ascending order: {animals}")
    animals.insert(animals.index("eagle"), "hawk")
    print(f"Replace hawk with eagle: {animals}")
    animals.append("hunter")
    print(f"Added hunter to the list: {animals}")

list_ops()

# Task 5 - Strings
def pig_latin(word):
    if not word:
        return word
    if word[0].lower() in "aeiou":
        return word + "hay"
    return word[1:] + word[0] + "ay"


# Task 6*
def palindrome():
    largest = 0
    for first in range(999, 99, -1):
        for second in range(first, 99, -1):
            product = first * second
            if product > largest and str(product) == str(product)[::-1]:
                largest = product
    return largest


# Task 7^
def alt_harmonic(n):
    terms = [(-1) ** (k + 1) / k for k in range(1, n + 1)]
    return sum(terms)

# Task 8^ - Lists
def list_min_max_avg(lst):
    return min(lst), max(lst), sum(lst) / len(lst)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value, avg_value = list_min_max_avg(numbers)
print(f"Minimum: {min_value}, Maximum: {max_value}, Average: {avg_value}")


# Task 8b^ - List comprehension
def inverse_association(number):
    associations = [("Marco", 1), ("Luca", 2), ("Alex", 3)]
    matches = [name for name, value in associations if value == number]
    return matches[0]

print(inverse_association(2))  


# Task 9^ - Mutable vs Immuatable Objects
def mutable_vs_immutable():
    my_int = 10
    int_copy = my_int
    my_int += 1
    print("int:", int_copy == my_int, id(int_copy) == id(my_int)) # id checks if the two variables point to the same object in memory
    print(f"See: int_copy: {int_copy}", f"my_int: {my_int}")

    my_string = "hello"
    string_copy = my_string
    my_string += "!"
    print("str:", string_copy == my_string, id(string_copy) == id(my_string))

    my_list = [1, 2]
    list_copy = my_list
    my_list.append(3)
    print("list:", list_copy == my_list, id(list_copy) == id(my_list))
    print(f"See: list_copy: {list_copy}", f"my_list: {my_list}")

    my_tuple = (1, 2)
    tuple_copy = my_tuple
    my_tuple += (1,)
    print("tuple:", tuple_copy == my_tuple, id(tuple_copy) == id(my_tuple))

    my_set = {1, 2}
    set_copy = my_set
    my_set.add(3)
    print("set:", set_copy == my_set, id(set_copy) == id(my_set))
    print(f"See: set_copy: {set_copy}", f"my_set: {my_set}")


mutable_vs_immutable()


# Task 10 - Implementing Modules
import calculator
def hypotenuse(first_side, second_side):
    first_square = calculator.multiply(first_side, first_side)
    second_square = calculator.multiply(second_side, second_side)
    sum_of_squares = calculator.add(first_square, second_square)
    return calculator.sqrt(sum_of_squares)

# Task 11: Explore itertools, sys, random, time.


# Task 12^ - Module Itertools
# A power set contains every possible subset of the original collection.  For
# n elements, a subset can contain 0, 1, 2, ..., or n elements, so the loop
# asks combinations() for every possible subset size.  combinations() returns
# tuples, and chain.from_iterable() joins all of those groups into one iterator.
# Each tuple is converted to a set so the result is a list of sets.  This also
# includes the empty set because combinations(elements, 0) returns one empty
# tuple, and it includes the complete set because the loop reaches size n.
# There are 2 ** n subsets because each element independently has two choices:
# it is either included or excluded.  The result cannot be a set of ordinary
# sets because set objects are mutable and therefore unhashable.  A set can
# contain immutable values such as frozenset objects instead.
def power_set(iterable):
    elements = list(iterable)
    subsets = chain.from_iterable(
        combinations(elements, size) for size in range(len(elements) + 1)
    )
    return [set(subset) for subset in subsets]

print(power_set({1, 2, 3}))

# Task 13^ - Classes & 14 - Inheritance & 15 - Magic Methods
# See object_oriented.py for the Backpack and Jetpack classes. 


# Task 16^ - Exception Handling 
def random_walk(max_iters=1e12):
    try:
        walk = 0
        directions = [1, -1]
        for i in range(int(max_iters)):
            walk += choice(directions)
        return walk
    except KeyboardInterrupt:
        print("Walk interrupted by user.")
        return walk

# Task 17 - File Input/Output
class ContentFilter:
    """Read and store the contents of a valid text file.

    Attributes:
        filename (str): the name of the file that was successfully opened.
        contents (str): the complete contents of the file as one string.
    """

    def __init__(self, filename):
        """Open a valid file and store its name and complete contents.

        If the initial filename is invalid, repeatedly prompt for another
        filename until a file can be successfully opened and read.

        Parameters:
            filename (str): the initial file name to try.
        """
        while True:
            try:
                with open(filename, "r") as input_file:
                    self.contents = input_file.read()
                self.filename = filename
                break
            except (FileNotFoundError, TypeError, OSError):
                filename = input("Please enter a valid file name: ")

# Task 18^ - Matrix Multiplication
import numpy as np
def matrix_product():
    """Return the product of the Task 18 matrices, A @ B."""
    matrix_a = np.array([
        [3, -1, 4],
        [1, 5, -9],
    ])
    matrix_b = np.array([
        [2, 6, -5, 3],
        [5, -8, 9, 7],
        [9, -3, -2, -3],
    ])
    return matrix_a @ matrix_b

# Task 19^ - Matrix Multiplication
import numpy as np
def matrix_polynomial():
    """Return -A^3 + 9A^2 - 15A for the Task 19 matrix A."""
    matrix_a = np.array([
        [3, 1, 4],
        [1, 5, 9],
        [-5, 3, 1],
    ])
    matrix_a_squared = matrix_a @ matrix_a
    matrix_a_cubed = matrix_a_squared @ matrix_a
    return -matrix_a_cubed + 9 * matrix_a_squared - 15 * matrix_a

# Task 20^ - Array Creation
import numpy as np
def structured_matrix_product():
    """Return the int64 product of the structured matrices A and B."""
    ones = np.ones((7, 7), dtype=np.int64)
    matrix_a = np.triu(ones)
    matrix_b = np.tril(-ones) + np.triu(5 * ones, k=1) # k=1 : 1 above the main diagonal
    print("Matrix A:\n", matrix_a)
    print("Matrix B:\n", matrix_b)

    return (matrix_a @ matrix_b).astype(np.int64)

structured_matrix_product()

# Task 21^ - Arrays 
import numpy as np
def replace_negatives(array):
    """Return a copy of array with all negative entries replaced by zero."""
    result = np.copy(array)
    # Fancy indexing = seleciting or changing elemnts using another array of indexes 
    result[result < 0] = 0
    return result

print(replace_negatives(np.array([-1, 2, -3, 4, -5])))


# Task 22 - Arrays 
import numpy as np
def block_matrix():
    """Return the Task 22 block matrix using NumPy stacking functions."""
    matrix_a = np.array([
        [0, 2, 4],
        [1, 3, 5],
    ])
    matrix_b = np.array([
        [3, 0, 0],
        [3, 3, 0],
        [3, 3, 3],
    ])
    matrix_c = -2 * np.eye(3, dtype=int)
    identity = np.eye(3, dtype=int)

    top_row = np.hstack((np.zeros((3, 3), dtype=int), matrix_a.T, identity))
    middle_row = np.hstack((matrix_a, np.zeros((2, 2), dtype=int),
                            np.zeros((2, 3), dtype=int)))
    bottom_row = np.hstack((matrix_b, np.zeros((3, 2), dtype=int), matrix_c))
    return np.vstack((top_row, middle_row, bottom_row))

print(block_matrix())


# Task 23^ - Arrays 
import numpy as np
def row_stochastic(matrix):
    """Return a copy of matrix with each row normalized to sum to 1."""
    matrix = np.asarray(matrix)
    row_sums = matrix.sum(axis=1, keepdims=True)
    return matrix / row_sums

row_stochastic(np.array([[1, 2], [3, 4]]))

# Task 24 - Polynomials 
import math
import numpy as np
from numpy.polynomial import Polynomial

# 1. Define the number of terms and initialize coefficient array
n_terms = 30
max_degree = 2 * (n_terms - 1) + 1
coeffs = np.zeros(max_degree + 1)

# 2. Compute coefficients for the arcsin(x) Taylor series expansion
for n in range(n_terms):
    deg = 2 * n + 1
    # Coefficient: (2n)! / ((2n + 1) * (n!)^2 * 4^n)
    c = math.factorial(2 * n) / ((2 * n + 1) * (math.factorial(n) ** 2) * (4**n))
    coeffs[deg] = c

# 3. Construct the NumPy Polynomial object
arcsin_poly = Polynomial(coeffs)

# 4. Approximate pi using arcsin(1/2) = pi / 6  =>  pi = 6 * arcsin(1/2)
x_val = 0.5
pi_approx = 6 * arcsin_poly(x_val)

# 5. Verify accuracy with np.allclose
is_close = np.allclose(pi_approx, np.pi)

print(f"Approximated Pi : {pi_approx}")
print(f"Actual Pi       : {np.pi}")
print(f"np.allclose     : {is_close}")