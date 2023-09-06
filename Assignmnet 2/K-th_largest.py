def kth_largest(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
            else:
                pass
    return arr 
n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print("k")
k = int(input())
kth_largest(arr,n)
print(arr)
print(arr[k])

