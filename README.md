 # Python Exercises

Solutions for the Python Essentials exercises in `exercise1.py`, with the
object-oriented solutions for Tasks 13–15 in `object_oriented.py`.

## Requirements

The NumPy exercises require NumPy:

```bash
python3 -m pip install numpy
```

## Task 2: Printing

The first function uses an f-string. The second uses `sep` to control the
spacing between arguments and `end` to keep two `print()` calls on one line.

```python
def isolate(arg1, arg2, arg3, arg4, arg5):
	print(f"{arg1}     {arg2}     {arg3} {arg4} {arg5}")


def isolate2(arg1, arg2, arg3, arg4, arg5):
	print(arg1, arg2, arg3, sep="     ", end=" ")
	print(arg4, arg5)
```

## Task 3: String Slicing

Integer division finds the midpoint. The `[::-1]` slice reverses a sequence by
using a step of `-1`.

```python
def first_half(value):
	return value[:len(value) // 2]


def backward(value):
	return value[::-1]
```

## Task 4: Lists

List methods mutate the list in place: `append()` adds at the end, `insert()`
adds at an index, `pop()` removes an item, and `sort()` orders the list.

```python
def list_ops():
	animals = ["bear", "ant", "cat", "dog"]
	animals.append("eagle")
	animals.insert(2, "fox")
	animals.pop(1)
	animals.sort()
	animals.insert(animals.index("eagle"), "hawk")
	animals.append("hunter")

	for animal in animals:
		print(animal)
```

## Task 5: Strings

The `in` operator checks whether the first character is a vowel. Vowel-starting
words receive `hay`; consonant-starting words move their first character and
receive `ay`.

```python
def pig_latin(word):
	if not word:
		return word
	if word[0].lower() in "aeiou":
		return word + "hay"
	return word[1:] + word[0] + "ay"
```

## Task 6: Largest Palindrome

The nested loops test every product of two three-digit numbers. A string slice
checks whether each product reads the same forward and backward.

```python
def palindrome():
	largest = 0
	for first in range(999, 99, -1):
		for second in range(first, 99, -1):
			product = first * second
			if product > largest and str(product) == str(product)[::-1]:
				largest = product
	return largest
```

## Task 7: Alternating Harmonic Series

The list comprehension creates exactly `n` terms of the alternating harmonic
series, and `sum()` adds them.

```python
def alt_harmonic(n):
	terms = [(-1) ** (k + 1) / k for k in range(1, n + 1)]
	return sum(terms)
```

## Task 8: Lists

The built-in `min()`, `max()`, and `sum()` functions calculate the three
statistics. `len()` supplies the count for the average.

```python
def list_min_max_avg(values):
	return min(values), max(values), sum(values) / len(values)
```

## Task 8b: List Comprehension

The list comprehension selects the name whose associated value equals the
input number.

```python
def inverse_association(number):
	associations = [("Marco", 1), ("Luca", 2), ("Alex", 3)]
	matches = [name for name, value in associations if value == number]
	return matches[0]
```

## Task 9: Mutable vs Immutable Objects

Assignment creates a second name for the same object. Mutating a list or set
changes both names, while operations on immutable integers, strings, and
tuples create a new object. `id()` compares object identity.

```python
def mutable_vs_immutable():
	my_int = 10
	int_copy = my_int
	my_int += 1
	print("int:", int_copy == my_int, id(int_copy) == id(my_int))

	my_string = "hello"
	string_copy = my_string
	my_string += "!"
	print("str:", string_copy == my_string, id(string_copy) == id(my_string))

	my_list = [1, 2]
	list_copy = my_list
	my_list.append(3)
	print("list:", list_copy == my_list, id(list_copy) == id(my_list))

	my_tuple = (1, 2)
	tuple_copy = my_tuple
	my_tuple += (1,)
	print("tuple:", tuple_copy == my_tuple, id(tuple_copy) == id(my_tuple))

	my_set = {1, 2}
	set_copy = my_set
	my_set.add(3)
	print("set:", set_copy == my_set, id(set_copy) == id(my_set))
```

## Task 10: Implementing Modules

`calculator.py` exposes addition, multiplication, and `sqrt`. The hypotenuse
function uses only those module functions to calculate $\sqrt{a^2+b^2}$.

```python
# calculator.py
from math import sqrt


def add(first, second):
	return first + second


def multiply(first, second):
	return first * second
```

```python
# exercise1.py
import calculator


def hypotenuse(first_side, second_side):
	first_square = calculator.multiply(first_side, first_side)
	second_square = calculator.multiply(second_side, second_side)
	sum_of_squares = calculator.add(first_square, second_square)
	return calculator.sqrt(sum_of_squares)
```

## Task 11: Modules

The source contains the topic heading `itertools`, `sys`, `random`, and `time`,
but no separate Task 11 implementation.

## Task 12: Module Itertools

`itertools.combinations()` creates subsets of each possible size. `chain` joins
those groups into one iterator. Each tuple becomes a set; ordinary mutable sets
cannot be placed inside another set because they are unhashable.

```python
from itertools import chain, combinations


def power_set(iterable):
	elements = list(iterable)
	subsets = chain.from_iterable(
		combinations(elements, size) for size in range(len(elements) + 1)
	)
	return [set(subset) for subset in subsets]
```

## Task 13: Classes

The `Backpack` class is defined in `object_oriented.py`. It stores ownership,
color, capacity, and contents, and prevents items from exceeding capacity. 
For full implementation see `object_oriented.py`. 

```python
class Backpack:
	def __init__(self, name, color, max_size=5):
		self.name = name
		self.color = color
		self.max_size = max_size
		self.contents = []

	def put(self, item):
		if len(self.contents) >= self.max_size:
			print("No Room!")
		else:
			self.contents.append(item)

	def dump(self):
		self.contents = []

	def take(self, item):
		self.contents.remove(item)

	def __eq__(self, other):
		if not isinstance(other, Backpack):
			return NotImplemented
		return (self.name == other.name
				and self.color == other.color
				and len(self.contents) == len(other.contents))

	def __str__(self):
		return (f"Owner:\t\t{self.name}\n"
				f"Color:\t\t{self.color}\n"
				f"Size:\t\t{len(self.contents)}\n"
				f"Max Size:\t{self.max_size}\n"
				f"Contents:\t{self.contents}")
```

## Task 14: Inheritance

`Jetpack` inherits the Backpack behavior and adds a fuel supply, controlled
burning through `fly()`, and a `dump()` method that clears both contents and
fuel.

```python
class Jetpack(Backpack):
	def __init__(self, name, color, max_size=2, fuel=10):
		super().__init__(name, color, max_size)
		self.fuel = fuel

	def fly(self, fuel_burned):
		if fuel_burned > self.fuel:
			print("Not enough fuel!")
		else:
			self.fuel -= fuel_burned

	def dump(self):
		super().dump()
		self.fuel = 0
```

## Task 15: Magic Methods

The `Backpack` methods `__eq__()` and `__str__()` implement equality and a
readable display format.

## Task 16: Handling Exceptions

The `try` block performs the walk, and `KeyboardInterrupt` lets the function
return the current position if the user stops it with Ctrl+C.

```python
from random import choice


def random_walk(max_iters=1e12):
	try:
		walk = 0
		directions = [1, -1]
		for _ in range(int(max_iters)):
			walk += choice(directions)
		return walk
	except KeyboardInterrupt:
		print("Walk interrupted by user.")
		return walk
```

## Task 17: File Input/ Output

`with open()` closes the file automatically. The constructor catches invalid
filename errors and keeps prompting until it can read a file.

```python
class ContentFilter:
	def __init__(self, filename):
		while True:
			try:
				with open(filename, "r") as input_file:
					self.contents = input_file.read()
				self.filename = filename
				break
			except (FileNotFoundError, TypeError, OSError):
				filename = input("Please enter a valid file name: ")
```

## Task 18: Matrix Multiplication in Numpy

NumPy arrays store the matrices, and `@` performs matrix multiplication.

```python
import numpy as np


def matrix_product():
	matrix_a = np.array([[3, -1, 4], [1, 5, -9]])
	matrix_b = np.array([
		[2, 6, -5, 3],
		[5, -8, 9, 7],
		[9, -3, -2, -3],
	])
	return matrix_a @ matrix_b
```

## Task 19: Matrix Multiplication

The `@` operator calculates matrix powers through multiplication, rather than
the element-by-element power operation.

```python
import numpy as np


def matrix_polynomial():
	matrix_a = np.array([
		[3, 1, 4],
		[1, 5, 9],
		[-5, 3, 1],
	])
	matrix_a_squared = matrix_a @ matrix_a
	matrix_a_cubed = matrix_a_squared @ matrix_a
	return -matrix_a_cubed + 9 * matrix_a_squared - 15 * matrix_a
```

## Task 20: Array Creation

NumPy’s `ones()` creates the base array. `triu()` selects the upper triangle and
`tril()` selects the lower triangle; `k=1` starts one diagonal above the main
diagonal. The product is converted to `np.int64`.

```python
import numpy as np


def structured_matrix_product():
	ones = np.ones((7, 7), dtype=np.int64)
	matrix_a = np.triu(ones)
	matrix_b = np.tril(-ones) + np.triu(5 * ones, k=1)
	return (matrix_a @ matrix_b).astype(np.int64)
```

## Task 21: Arrays

`np.copy()` protects the input. The Boolean expression `result < 0` selects all
negative entries at once, and fancy indexing replaces those entries with zero.

```python
import numpy as np


def replace_negatives(array):
	result = np.copy(array)
	result[result < 0] = 0
	return result
```

## Task 22: Arrays

`np.hstack()` joins blocks horizontally and `np.vstack()` joins complete block
rows vertically. The zero arrays have shapes chosen to match neighboring blocks.

```python
import numpy as np


def block_matrix():
	matrix_a = np.array([[0, 2, 4], [1, 3, 5]])
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
```

## Task 23: Arrays

`sum(axis=1)` computes one sum per row. `keepdims=True` keeps the result shaped
as a column, so broadcasting divides every row by its own sum.

```python
import numpy as np


def row_stochastic(matrix):
	matrix = np.asarray(matrix)
	row_sums = matrix.sum(axis=1, keepdims=True)
	return matrix / row_sums
```

## Task 24: Polynomials

`numpy.polynomial.Polynomial` represents a polynomial by its coefficient array.
The coefficients below are the Taylor-series coefficients for `arcsin(x)`.
Evaluating at $x=1/2$ and multiplying by 6 approximates pi.

```python
import math
import numpy as np
from numpy.polynomial import Polynomial


n_terms = 30
max_degree = 2 * (n_terms - 1) + 1
coeffs = np.zeros(max_degree + 1)

for n in range(n_terms):
	degree = 2 * n + 1
	coefficient = (math.factorial(2 * n)
				   / ((2 * n + 1) * math.factorial(n) ** 2 * 4 ** n))
	coeffs[degree] = coefficient

arcsin_poly = Polynomial(coeffs)
pi_approx = 6 * arcsin_poly(0.5)
is_close = np.allclose(pi_approx, np.pi)

print(f"Approximated Pi : {pi_approx}")
print(f"Actual Pi       : {np.pi}")
print(f"np.allclose     : {is_close}")
```

## Files

- `exercise1.py`: function, NumPy, file I/O, and array exercises.
- `object_oriented.py`: `Backpack`, `Knapsack`, `Jetpack`, and Task 15 magic methods.
- `calculator.py`: arithmetic helpers and `sqrt` for Task 10.
