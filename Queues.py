from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'
def search(name):
    search_queue = deque() # Creates a new queue
    search_queue += graph["you"] # Adds all of your neighbors to the search queue
    searched = [] # Array is how you keep track of which people you've searched before.
    while search_queue: # While the queue isn't empty
        person = search_queue.popleft() # grabs the first person off the queue
        if person_is_seller(person):# Checks whether the person is a mango seller
            print(person + "is a mango seller!") # Yes they're a mango seller
            return True
        else:
            search_queue += graph(person) #No, they aren't. Add all of this persons's friends to the search queue
            searched.append(person) # Marks the person as searched
    return False # If you reached here, no one in the queue was a mango seller.



