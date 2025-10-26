def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}

    # iterate the whole list through index 'i'
    for i in range(lens(nums)):
        current_num = nums[i]

        # check value we need to complete the sum:
        check = target - current_num

        # If found, the complement's index is the stored value (j)
        # and current index is i

        if complement in num_map:
            j = num_map[complement]
            return [j, i]

        # if not found, add current number and its index to map
        # for future potential use
        num_map[current_num] = i
    return []
