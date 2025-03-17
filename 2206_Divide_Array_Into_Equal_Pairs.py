class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}

        for num in nums:
            d[num] = d.get(num,0) + 1

        for freq in d.values():
            if freq % 2 != 0:
                return False

        return True           
        

# ! Explanation:
# * This function checks if it is possible to divide an array into pairs such that each pair consists of two equal elements.
# * 1. Create a dictionary `d` to store the frequency of each element in the input list.
# * 2. Iterate through the input list and update the frequency of each element in the dictionary.
# * 3. Iterate through the values of the dictionary and check if the frequency of any element is odd.
# * 4. If the frequency is odd, return False as it is not possible to divide the array into pairs.
# * 5. If all frequencies are even, return True as it is possible to divide the array into pairs.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the number of elements in the input list.
# * This is because we iterate through the input list to calculate the frequency of each element.

# ? Space Complexity:
# * The space complexity is O(n) because we use a dictionary to store the frequency of each element in the input list.
# * The space complexity of this approach is O(n).      