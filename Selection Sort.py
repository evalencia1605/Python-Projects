arr = [7, 8, 9, 4, 6]

def SelectionSort(arr):
    for i in range(len(arr) - 1):
        minindex = i
        for j in range(i + 1, len(arr)):
            if arr[minindex] > arr[j]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]

SelectionSort(arr)
print(arr)





