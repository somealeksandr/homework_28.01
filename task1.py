
arr = [34, 56, 67, 46, 4, 67, 23, 9, 23, 1, 6, 3]
name = input("Enter your name: ")
min_value = min(arr)
max_value = max(arr)
min_index = arr.index(min_value)
max_index = arr.index(max_value)
print("min_value", min_value)
print("max_value", max_value)
print("min_index", min_index)
print("max_index", max_index)
temp = arr[min_index]
arr[min_index] = arr[max_index]
arr[max_index] = temp
print("New ARR =>", arr, name)



