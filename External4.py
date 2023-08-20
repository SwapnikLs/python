def bobsort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
arr=input("enter the list of elements separated by spaces: ").split()
arr=[int(nums) for nums in arr]
bobsort(arr)
print(arr)