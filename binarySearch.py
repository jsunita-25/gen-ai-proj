def binary_search(arr, target):  
    left = 0  
    right = len(arr) - 1  
  
    while left <= right:  
        mid = (left + right) // 2  
  
        # Check if target is at mid  
        if arr[mid] == target:  
            return mid  # return index  
  
        # If target is greater, ignore left half  
        elif arr[mid] < target:  
            left = mid + 1  
  
        # If target is smaller, ignore right half  
        else:  
            right = mid - 1  
  
    return -1  # not found  
  
# Example usage  
arr = [1, 3, 5, 7, 9, 11, 13]  
target = 7  
  
result = binary_search(arr, target)  
if result != -1:  
    print(f"Element found at index {result}")  
else:  
    print("Element not found")  
