def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_idx]):
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = arr[mid_idx]
        
        if(mid_el == target):
            return mid_idx
        
        elif(mid_el < target):
            left = mid_idx + 1
        
        else:
            right = mid_idx - 1
    return -1


print("Enter list elements, separated by single space\n")
nums = [int(x) for x in input().split()]
print(f"Unsorted list\n{nums}")
selection_sort(nums)
print(f"Sorted list\n{nums}")

print("Enter a target number")
target = int(input())

result = binary_search(nums, target)

if result != -1:
    print(f"Element is present at index {str(result)} value is {nums[result]}")
else:
    print("Element is not present in array")