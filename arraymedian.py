nums1 = [1, 2]
nums2 = [3, 4]

def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    mid = n // 2
    if n % 2 == 0:
        median = (merged[mid - 1] + merged[mid]) / 2
    else:
        median = merged[mid]
    return median
print(findMedianSortedArrays(nums1, nums2))