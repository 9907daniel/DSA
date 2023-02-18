class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        empty_array = []
        if len(arr) == 1:
            return [-1]

        for a,b in enumerate(arr):
            if b == max(arr):
                empty_array.append(arr[a])
                
                new_array = arr[a+1:-1]
                new_array.append(arr[-1])
        
        for c in range(len(new_array)):
            new_array[c] = max(new_array[c:])
            empty_array.append(new_array[c])

        empty_array.append(-1)
        print(empty_array)
        return empty_array


# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

