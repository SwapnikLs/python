def linear_search(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1
arr=input("enter a list of elemnets seperated by spaces: ").split()
arr=[int(j) for j in arr]
x=int(input("enter the required element: "))
index=linear_search(arr,x)
if index!=-1:
    print(f"the element {x} is present at index {index} ")
else:
    print(f"the element {x} is not present in the array")
print("HOlys h")


    