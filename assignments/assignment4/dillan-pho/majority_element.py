def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_hashmap = {}

        for x in nums:
            if x not in new_hashmap:
                new_hashmap[x] = 1
            else:
                new_hashmap[x] += 1
        return max(new_hashmap, key=new_hashmap.get)

# Test case
num = [2,2,1,1,1,2,2]
target = 2
result = majorityElement(num)
print(f"The majority of the list should be {target} and the answer was: {result}")