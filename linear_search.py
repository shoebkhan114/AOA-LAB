def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [12, 25, 8, 45, 19, 30, 55, 10]

x = int(input("Enter element to search: "))

result = linearSearch(arr, x)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)