"""
The largest_number function recursively finds the largest number in a 
list of integers. It starts by checking if the list has only one element 
(base case) and returns that element. 

If the list has more than one element, it compares the first element 
with the largest number in the rest of the list (obtained by recursively 
calling the function with the sublist starting from index 1) and returns 
the larger of the two.

"""

# Define a function named largest_number that takes a list of integers as an argument
def largest_number(nums):
    """
    Find the largest number in a list of integers recursively.

    Args:
        nums (list of int): List of integers.

    Returns:
        int: The largest integer in the list.
    """
    # Base case: if the list has only one element, return that element
    if len(nums) == 1:
        return nums[0]
    # Recursive case: compare the first element with the largest number 
    # in the rest of the list and return the larger of the two
    return max(nums[0], largest_number(nums[1:]))

# Example usage:
print(largest_number([1, 4, 5, 3, 9, 6, 7]))  # Output: 9
