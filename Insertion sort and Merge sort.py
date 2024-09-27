#Insertion sort

user_input = input("Enter numbers separated by spaces: ")
arr = list(map(int, user_input.split()))

user_alg = input("Enter \"i\" for Insertion Sort or \"m\" for Merge Sort: ")


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


if user_alg == "i":
    Insertion_sort(arr)
    print(arr)

elif user_alg == "m":
    Merge_sort(arr)
    print(arr)

else:
    print("Not a valid algorithm!!")