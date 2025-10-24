def rotate(nums : list[int], k: int) -> None:
    n = len(nums)
    
    # normalize K: get the effective number of steps
    k = k % n

    if k == 0 or n <= 1:
        return

    def reverse_subarray(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse_subarray(nums, 0, n - k - 1)
    reverse_subarray(nums, n - k, n - 1)
    reverse_subarray(nums, 0, n - 1)


nums1 = [1,2,3,4,5,6,7]    
k1 = 3
rotate(nums1, k1)
print(f"Example 1 output: {nums1}")



nums2 = [-1, -100, 3, 99]
k2 = 2
rotate(nums2, k2)
print(f"Example 2 output: {nums2}")
