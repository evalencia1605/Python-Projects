user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.split()))

user_alg = input("Enter \"i\" for Insertion Sort or \"m\" for Merge Sort or \"s\" for Selection Sort or \"b\" for Bubble Sort or \"h\" for Heap Sort: ")


def Insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

def Merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #Recursion
        Merge_sort(left_arr)
        Merge_sort(right_arr)

        #merge
        i = 0 #left array index
        j = 0 #right array index
        k = 0 #merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
            k = k + 1

    #Adding remaining elements  
        while i < len(left_arr): 
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1

def Selection_Sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
              arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = len(arr)
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
          largest = l
  
    if r < n and arr[largest] < arr[r]:
          largest = r
  
    if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)

def Heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
                
if user_alg == "i":
    Insertion_sort(arr)
    print(arr)

elif user_alg == "m":
    Merge_sort(arr)
    print(arr)

elif user_alg == "s":
    Selection_Sort(arr)
    print(arr)

elif user_alg == "b":
    BubbleSort(arr)
    print(arr)

elif user_alg == "h":
    Heap_sort(arr)
    print(arr)

else:
    print("Not a valid algorithm!!")