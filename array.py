#1. Reverse an Array

arr = [1,2,3,4,5]

start = 0
end =len(arr)-1

while start < end:
    arr[start] ,arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(arr)

#2. Find the Maximum & Minimum Element

arr = [34,46,38,54]

max_ele = arr[0]
min_ele = arr[0]

for i in arr:
    if i < min_ele:
        min_ele = i
    if i > max_ele:
        max_ele = i

print('Maximum number:',max_ele)
print('Minimum number:',min_ele)

#3. Find the Sum of Elements

arr = [1,5,7,8]

total = 0

for num in arr:
    total += num

print('Sum:', total)

#4. Find the Second Largest Element

arr = [2,5,8,6,9]
max_ele = arr[0]
second_max_ele = arr[0]

for num in arr:
    if num > max_ele:
        second_max_ele = max_ele
        max_ele = num
    elif num > second_max_ele and num != max_ele:
        second_max_ele = num

print("Second Largest:", second_max_ele)   

#5. Count Frequency of Elements

arr = [1,2,3,5,6,1,5,6]

freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq) 

#6. Check if Array is Sorted

arr = [5,8,9,2]

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print(False)
        break
else:
    print(True)

#8.Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
nums = [5,7,8,9]
target = 12

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+ nums[j] == target:
            print((nums[i],nums[j]))

#9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
def remove_duplicate(arr):
    temp = []
    for num in arr:
        if num not in temp:
            temp.append(num)

    return temp

#example
arr = [1, 2, 2, 3, 4, 3, 5]
print(remove_duplicate(arr))

#10. Merge Two Sorted Arrays
def merge_sorted(arr1, arr2):
    i = 0
    j = 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

        
    return result

# Example
print(merge_sorted([1,3,5], [2,4,6]))

#11. Remove given Element from Array
def remove_element(arr, target):
    result = []
    for num in arr:
        if num != target:
            result.append(num)
    return result
# Example
arr = [1,2,3,4,5,2]
target = 2
print(remove_element(arr, target))

#12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum
# Example
arr = [1, 2, 4, 5]
print(find_missing_number(arr))

#13. Find Duplicates in an Array
def find_duplicates(arr):
    freq = {}
    duplicates = []
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    for num, count in freq.items():
        if count > 1:
            duplicates.append(num)
    
    return duplicates
# Example
arr = [1, 2, 3, 4, 2, 5, 3]
print(find_duplicates(arr))

#14. Find Intersection of Two Arrays: Find the common elements between two arrays.
def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))
# Example
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
print(intersection(arr1, arr2))

#15. Find Union of Two Arrays
def union(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.union(set2))
# Example
print(union(arr1, arr2))

 #16. Check if Two Arrays Are Equal: if two arrays contain the same elements
def are_arrays_equal(arr1, arr2):
    return sorted(arr1) == sorted(arr2)
# Example
arr1 = [1, 2, 3]
arr2 = [3, 2, 1]
print(are_arrays_equal(arr1, arr2))

#17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right
def find_leaders(arr):
    leaders = []
    max_so_far = float('-inf')

    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_so_far:
            leaders.append(arr[i])
            max_so_far = arr[i]

    return leaders[::-1]
#18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
def move_zeroes(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1

    while j < len(arr):
        arr[j] = 0
        j += 1

    return arr
#19. Find Subarray with Given Sum.
def subarray_sum(arr, target):
    start = 0
    curr_sum = 0

    for end in range(len(arr)):
        curr_sum += arr[end]

        while curr_sum > target:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == target:
            return (start, end)

    return -1
#20. Rotate Array to the Left by k Positions
def rotate_left(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]
#21. Find the Kth Smallest Element
def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]
#22. Find All Subarrays
def all_subarrays(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result.append(arr[i:j+1])
    return result
#23. Maximum Sum Subarray (Kadane's Algorithm)
def max_subarray(arr):
    max_sum = curr = arr[0]

    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        max_sum = max(max_sum, curr)

    return max_sum
#24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.
def rearrange(arr):
    arr.sort()
    result = []
    i, j = 0, len(arr)-1

    while i <= j:
        if i != j:
            result.append(arr[j])
            result.append(arr[i])
        else:
            result.append(arr[i])
        i += 1
        j -= 1

    return result
#25. Find Majority Element: Find the element that appears more than n/2 times.
def majority_element(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate
#26. Find Peak Element: A peak element is greater than its neighbors. Find one such element.
def find_peak(arr):
    for i in range(len(arr)):
        if (i == 0 or arr[i] >= arr[i-1]) and \
           (i == len(arr)-1 or arr[i] >= arr[i+1]):
            return i
#27. Find the First Missing Positive: Find the smallest positive integer missing in the array.
def first_missing_positive(arr):
    s = set(arr)
    i = 1
    while True:
        if i not in s:
            return i
        i += 1
#28. Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.
def sort012(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
#29. Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers.
def longest_consecutive(arr):
    s = set(arr)
    longest = 0

    for num in s:
        if num - 1 not in s:
            length = 1
            while num + length in s:
                length += 1
            longest = max(longest, length)

    return longest
"""30. Product of Array Except Self
Given an array, return a new array where each element is the product of all elements except itself.
Do not use division.

Input: [1,2,3,4]
Output: [24,12,8,6]"""
def product_except_self(arr):
    n = len(arr)
    left = [1]*n
    right = [1]*n
    result = [1]*n

    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]

    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * arr[i+1]

    for i in range(n):
        result[i] = left[i] * right[i]

    return result
#31. Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total -= arr[i]
        if left_sum == total:
            return i
        left_sum += arr[i]

    return -1
#32. Find Maximum Product Pair: Find two elements whose product is maximum.
def max_product_pair(arr):
    arr.sort()
    return max(arr[0]*arr[1], arr[-1]*arr[-2])
#33. Find Maximum Difference (j > i)
def max_difference(arr):
    min_val = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_val)
        min_val = min(min_val, arr[i])

    return max_diff