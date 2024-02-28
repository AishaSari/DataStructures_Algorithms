import kivy
import array
import math as mt

arr = [2, 5, 3, 4, 1, 7, 6, 9, 10, 8]
print("Array =", arr)

# User chooses which feature for Array
options_arr = ['Append', 'Insert', 'Pop', 'Remove', 'Linear Search', 'Binary Search', 'Ternary Search', 'Bubble Sort']
user_input = ''
input_message = "Choose an option:\n"

for index, item in enumerate(options_arr):
    input_message += f'{index+1}) {item}\n'

input_message += 'Enter number of option: '

while user_input not in map(str, range(1, len(options_arr) + 1)):
    user_input = input(input_message)

print('You picked: ' + options_arr[int(user_input) - 1])

## add to array ##
# append at end
if user_input == '1':
    target_append = int(input("Enter value of element: "))
    arr.append(target_append)
    print(arr)
# insert at any position
elif user_input == '2':
    target_insertX = int(input("Enter value of element:"))
    target_insertY = int(input("Enter desired index of element: "))
    arr.insert(target_insertY, target_insertX) # inserts y at index x
    print(arr)

## delete from array ##
# delete by index
elif user_input == '3':
    target_pop = int(input("Enter desired index of element: "))
    arr.pop(target_pop)
    print(arr)
# delete by value
elif user_input == '4':
    target_remove = int(input("Enter value of element: "))
    arr.remove(target_remove)
    print(arr)

## search in array ##
# linear search
if user_input == '5':
    # traversing array
    def linear_search(arr, target_linear):
        for i in range(len(arr)):
            if arr[i] == target_linear:
                return i
        return -1

    target_linear = int(input("Enter value of element: "))
    index_linear = linear_search(arr, target_linear)
    if index_linear == -1:
        print("Element not found.")
    else:
        print("Element is present at index", index_linear)

# binary search
if user_input == '6':
    def binary_search(arr, min, max, key):
        if max >= min:
            mid = (max + min) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return binary_search(arr, min, mid - 1, key)
            else:
                return binary_search(arr, mid + 1, max, key)
        else:
            return -1

    # sort array
    arr.sort()
    print("Sorted Array =", arr)

    target_binary = int(input("Enter value of element: "))
    index_binary = binary_search(arr, 0, len(arr)-1, target_binary)

    if index_binary == -1:
        print("Element not found.")
    else:
        print("Element is present at index", index_binary)

# ternary search
if user_input == '7':
    def ternary_search(min, max, key, arr):
        if max >= min:
            mid1 = min + (max - min) // 3
            mid2 = max - (max - min) // 3

            if arr[mid1] == key:
                return mid1

            if arr[mid2] == key:
                return mid2

            if key < arr[mid1]:
                return ternary_search(min, mid1 - 1, key, arr)
            elif key > arr[mid2]:
                return ternary_search(mid2 + 1, max, key, arr)
            else:
                return ternary_search(mid1 + 1, mid2 -1, key, arr)

            return -1

    # sort array
    arr.sort()
    print("Sorted Array =", arr)

    target_ternary = int(input("Enter value of element: "))
    index_ternary = ternary_search(0, len(arr)-1, target_ternary, arr)

    if index_ternary == -1:
        print("Element not found.")
    else:
        print("Element is present at index", index_ternary)

# bubble sort
if user_input == '8':
