arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
arr.sort()
print(arr)

x = 0
for item in range(0, len(arr) // 2):
    arr[x], arr[x + 1] = arr[x + 1], arr[x]
    x = x + 2
print(arr)