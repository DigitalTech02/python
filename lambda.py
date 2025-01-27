# Lambda Function to calculate the square of a number
square = lambda x: x ** 2

# Example usage
print(square(5))  # Output: 25
```

```python
# Lambda Function to filter even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))

# Example usage
print(even_numbers)  # Output: [0, 2, 4, 6, 8]
```

```python
# Lambda Function to sort a list of tuples by the second element
tuples_list = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])

# Example usage
print(sorted_tuples)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
