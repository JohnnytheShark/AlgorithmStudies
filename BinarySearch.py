def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high: # While you haven't narrowed it down to one element
        mid = (low + high)/2 # Check the middle element
        guess = list(mid)
        if guess == item: # Item has been Found
            return mid
        if guess > item: # The giess was too high
            high = mid - 1
        else: #The item doesn't exist
            low = mid + 1
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list,3)) # => 1
print(binary_search(my_list,-1)) #=> None
