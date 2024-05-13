"""

The 'adding_up_to' function recursively calculates the sum of all the 
numbers in the list up to the given index point. It starts by checking 
if the index is 0 (base case) and returns the first element of the list. 

If the index is greater than 0, it returns the sum of the element at the 
specified index and the result of the function called with the sublist 
from index 0 to index - 1.

"""

# Function named adding_up_to that takes a list of integers and an index as arguments
def adding_up_to(nums, index):
    """
    Recursively calculates the sum of elements in a list up to a specified index.

    Args:
        nums (list of int): List of integers.
        index (int): Index up to which the sum is calculated.

    Returns:
        int: Sum of elements in the list up to the specified index.
    """
    # Base case: if index is 0, return the first element of the list
    if index == 0:
        return nums[0]
    # Recursive case: return the sum of the current element and the result of
    # the function called with the sublist from index 0 to index - 1
    return nums[index] + adding_up_to(nums, index - 1)

# Example usage:

# nums = [1, 4, 5, 3, 12, 16], index = 4
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Output: 25
# nums = [4, 3, 1, 5], index = 1
print(adding_up_to([4, 3, 1, 5], 1))  # Output: 7