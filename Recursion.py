#While Loop Pseduo Code
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")

#Recursion Pseduo Code
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) #recursion
        elif item.is_a_key():
            print("Found a Key!")

# Factorial Function Recursion: 
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
# Total an Array
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1,2,3,4]))

def quicksort(array):
    if len(array) < 2:
        return array # Base Case: arrays with 0 or 1 element are already sorted
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] # sub array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] # Sub array of all the elements that are greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))