def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if low < len(arr):
        return (iterations, arr[low])  
    else:
        return (iterations, None)  

arr = [0.1, 0.5, 1.2, 2.8, 3.4, 4.5, 5.9]
target = 2.0

result = binary_search(arr, target)
print(result)  

target_not_found = 6.0
result_not_found = binary_search(arr, target_not_found)
print(result_not_found)  