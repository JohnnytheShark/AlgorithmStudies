def findSmallest(arr):
    smallest = arr[0] # Stores the smallest value
    smallest_index = 0 #Stores the index of the smallest value
    for i in range(i,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,2,4,5,10]))

#Quick sort
def quicksort(array):
    if len(array) < 2:
        return array

    
