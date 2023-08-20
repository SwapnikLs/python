def bs(arr, x):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = input("Enter the list of elements separated by spaces: ").split()
arr = [int(nums) for nums in arr]
arr.sort()
x = int(input("Enter the required element: "))
index = bs(arr, x)

if index != -1:
    print(f"Element {x} is present at index {index}.")
else:
    print(f"Element {x} is not present in the array.")
