# Write a Python function to find the index of an element in a tuple.

def find_index(element,input_tuple):
    try:
        index = input_tuple.index(element)
        return index
    except ValueError:

        return f"Element '{element}' not found in the tuple"

my_tuple = (10,20,30,40,50)
element_to_find = 40

result = find_index(element_to_find, my_tuple)
print(f"The index of {element_to_find} in the tuple is: {result}")
