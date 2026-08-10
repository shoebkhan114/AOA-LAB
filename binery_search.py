def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [5, 10, 15, 20, 25, 30, 35, 40]

x = int(input("Enter element to search: "))

result = binarySearch(arr, x)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)