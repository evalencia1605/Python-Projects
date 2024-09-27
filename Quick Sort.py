#Quick Sort
arr = [5,4,3,6,9]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1


def QuickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        QuickSort(arr, low, pivot - 1)
        QuickSort(arr, pivot + 1, high)

def print_arr(arr):
    for i in arr:
        print(i, end=" ")
    print()

QuickSort(arr, 0, len(arr) - 1)
print(arr)