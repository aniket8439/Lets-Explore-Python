class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        previous_end = 0

        for start, end in meetings:
            start = max(start, previous_end + 1)
            length = end - start + 1
            days -= max(length, 0)
            previous_end = max(previous_end, end)

        return days           
    
    
# ! Explanation:
# * This function calculates the number of days without any meetings given the total number of days and a list of meetings.
# * 1. Sort the meetings based on the start time.
# * 2. Initialize the previous_end variable to 0.
# * 3. Iterate through the meetings:
#     * Calculate the start time as the maximum of the current start time and the previous end time plus one.
#     * Calculate the length of the meeting.
#     * Subtract the maximum of the length and 0 from the total days.
#     * Update the previous end time as the maximum of the previous end time and the end time of the meeting.
# * 4. Return the remaining days without any meetings.

# ? Time Complexity:
# * The time complexity of this approach is O(n log n), where n is the number of meetings.
# * This is because we sort the meetings based on the start time.

# ? Space Complexity:
# * The space complexity of this approach is O(1).
# * This is because we use a constant amount of extra space to store variables and temporary values.    