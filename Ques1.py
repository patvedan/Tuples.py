# . Write a Python function to reverse a tuple.

def reverse_tuple(input_tuple):
    reversed_tuple = tuple(reversed(input_tuple))
    return reversed_tuple

original_tuple = (1,2.3,4,5)
reversed_result = reverse_tuple(original_tuple)