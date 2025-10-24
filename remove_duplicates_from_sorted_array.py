def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    
    i = 0;
    # loop through the whole list
    for j in range (1, len(nums)):
        # check if current element [j] is different from last unique element (i)
        if nums[j] != nums[i]:
           # found a new unique element
            # advance write pointer
            i = i + 1
            # overwrite duplicate/old pointer value at new unique pos
            nums[i] = nums[j]
    k = i + 1
    return k

nums_example = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums_example) 

print(f"The number of unique elements (k) is : {k}")
# The list 'nums_example' is modified in-place:
print(f"The modified list is: {nums_example}")
print(f"The first k elements are: {nums_example[:k]}")