class Solution:
    # I'm taking a list of nums which are integers and returning an intger value
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Im having 2 counters one to keep track of what count im on rn 
        # And a secong count to store max amounts of 1s we have seen so far
        count = 0
        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            # Each time im updating max count 
                if count > max_count:
                    max_count = count 
            # If I havent spotted a 1 set count back to 0
            else:
                count = 0
        # After the loop is done we will retun our max
        return max_count


# Time Complexity: O(n)
# Space Complexity: O(1)

