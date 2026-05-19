
# DELL

#Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.
#How it works
#Start from the second element.
#Compare it with elements before it.
#Shift larger elements one position to the right.
#Insert the current element into its correct position.
#Repeat for all elements.
#Example

#Array: [5, 3, 4, 1]

#Insert 3 before 5 → [3, 5, 4, 1]
#Insert 4 between 3 and 5 → [3, 4, 5, 1]
#Insert 1 at the beginning → [1, 3, 4, 5]




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# Example
nums = [5, 3, 4, 1]
print(insertion_sort(nums))
