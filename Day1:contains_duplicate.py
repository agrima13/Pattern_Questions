class ContainsDuplicate():
    def is_duplicate(self, nums):
        set_of_unique_nums = set()
        for i in range(len(nums)):
            if nums[i] in set_of_unique_nums:
                return True
            else:
                set_of_unique_nums.add(nums[i])
        return False

if __name__ == '__main__':
    nums = [1, 2, 3, 4,1]
    print(ContainsDuplicate().is_duplicate(nums))

"""
Important Notes

Using Hash Set

We can use the set data structure to check for duplicates in an array.

Since a set can only hold unique elements, we can check if the elements in the given array are present more than once by adding them to a set. This way, we can determine if there are any duplicates in the array.

This approach works as follows:

A set named unique_set is created to store unique elements.

The algorithm then iterates through the input array nums.

For each element "x" in the array, the algorithm checks if "x" is already in the unique_set.

If "x" is in the unique_set, then the algorithm returns True, indicating that a duplicate has been found.

If "x" is not in the unique_set, then the algorithm adds "x" to the unique_set.

The iteration continues until all elements in the array have been processed.

If no duplicates are found, the algorithm returns False.
"""