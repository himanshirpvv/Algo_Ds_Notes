# Function for selection sort
def Selection_Sort(array):
    for i in range(0, len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

# Function to print array
def Print_Array(array):
    for i in range(0, len(array)):
        print(array[i], end = " ")

    print()

array = [2, 4, 3, 1, 6, 8, 4]

Selection_Sort(array)

Print_Array(array)


''' Output

1 2 3 4 4 6 8

'''
