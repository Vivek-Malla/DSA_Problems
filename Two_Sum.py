def two_Sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]

n = int(input("Enter a count:"))

arr = []

for i in range(n):
    num = int(input(""))
    arr.append(num)

target = int(input("enter target :"))

print(two_Sum(arr,target))



