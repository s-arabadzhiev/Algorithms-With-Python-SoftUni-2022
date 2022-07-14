# Implement an algorithm that finds the index of an element in a sorted array of integers 
# in logarithmic time.

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


def binary_search(arr, low, high, target):
    
    if high >= low:
        mid_idx = (high + low) // 2
    
    if (arr[mid_idx] == target):
        return mid_idx
    
    elif (arr[mid_idx] > target):
        return binary_search(arr, low, mid_idx - 1, target)
    
    else:
        return binary_search(arr, mid_idx + 1, high, target)


print("Enter list elements, separated by single space\n")
nums = [int(x) for x in input().split()]

print(f"Unsorted list\n{nums}")
selection_sort(nums)
print(f"Sorted list\n{nums}")

print("Enter a target number\n")
target = int(input())

result = binary_search(nums, 0, len(nums)-1, target)

if result != -1:
    print(f"Element is present at index {str(result)} value is {nums[result]}")
else:
    print("Element is not present in array")
