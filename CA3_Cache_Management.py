# Nicholas Bryan - 201531951
# COMP517 - CA3 Cache Management

#-------#
# SETUP:
#-------#
# global scope lists

# list for storing page requests from user (where each 'page' is an int)
requests = []

# list for storing up to 8 cached pages
cache = []


#---------------#
# FIFO FUNCTION:
#---------------#
# function for managing cache by the "first in, first out" (FIFO) method
# adds requested pages to cache and, where necessary, evicts the page that has been in the cache the longest 

def fifo(requests, cache):
    # entry of request pages into the cache is managed by iterating over requests
    for i in requests:

        # checks for presence of request page 'i' in cache
        if i in cache:
            # pages present in cache generate a hit
            print("Hit:", i, "in cache")
        
        else:
            # pages not present in cache generate a miss
            print("Miss:", end = " ")
            
            # check if cache is full
            # if not full, the number of pages in cache is less than 8
            if len(cache) < 8:
                # use list.append() method to add new page to end of cache list
                cache.append(i)
                print("add", i)

            # else, cache is full
            # the page that has been in the cache the longest must be evicted to allow new page to enter cache
            else:
                # use list.pop() method to remove and return 0th page from cache list (as new pages are always appended to end of list, 0th page will have been in longest)
                evictedPage = cache.pop(0)
                # add new page to end of cache list
                cache.append(i)
                print("evict", evictedPage, "and add", i)

    print("Cache:", cache)
    # return to request entry
    return cache

#--------------#
# LFU FUNCTION:
#--------------#
# function for managing cache by the "least frequently used" (LFU) method
# adds requested pages to cache and, where necessary, evicts the page that has had the fewest hits

def lfu(requests, cache):

    # create empty dictionary, where keys are cached pages and values are number of page hits whilst in the cache
    cacheHitDict = {}

    # entry of request pages into the cache is managed by iterating over requests
    for i in requests:
    
        # checks for presence of request page 'i' in cache
        if i in cache:
            # pages present in cache generate a hit
            print("Hit:", i, "in cache")
            # if a hit, a dictionary entry for that page already exist
            # each hit against a page is logged by incrementing dictionary value of page by 1
            cacheHitDict[i] += 1

        else:
            # pages not present in cache generate a miss
            print("Miss:", end = " ")

            # check if cache is full
            # if not full, the number of pages in cache is less than 8
            if len(cache) < 8:
                # use list.append() method to add new page to end of cache list
                cache.append(i)
                # if a miss, add a dictionary entry for the page and assign value of 1 as entry to cache is first hit
                cacheHitDict[i] = 1
                print("add", i)

            # else, cache is full
            # the page that has had the fewest hits must be evicted to allow new page to enter cache
            # where pages in cache have equal number of hits, the smallest page number is evicted
            else:                
                # create empty list for adding all dictionary items, which allows the items to be sorted within this list 
                cacheHitList = []

                # iterate over dictionary items and add each item to list
                # each item in the cacheHitList is a tuple representing the dictionary key:value pairs as (key, value)
                for item in cacheHitDict.items():
                    cacheHitList.append(item)
                
                # first sort dictionary items in list by 0th element of each tuple (the key), which puts the list in ascending order by page number
                cacheHitList.sort(key = lambda x: x[0])
                # second sort dictionary items in list by 1st element of each tuple (the value), which then put the list in ascending order by number of hits
                cacheHitList.sort(key = lambda x: x[1])

                # in the sorted list, the 0th tuple is now the dictionary item with the smallest page number and fewest hits (LFU)
                # using list.pop() method, remove and return 0th tuple from list and assign to variable itemToEvict
                itemToEvict = cacheHitList.pop(0)

                # evict the LFU page from cache, using the 0th element of the itemToEvict tuple (page number)
                cache.remove(itemToEvict[0])
                # delete the corresponding LFU dictionary item from cacheHitDict by its key, using the 0th element of the itemToEvict tuple (page number)
                del cacheHitDict[itemToEvict[0]]

                # use list.append() method to add new page to end of cache list
                cache.append(i)
                # requested page was a miss, add a dictionary entry for the page and assign value of 1 as entry to cache is first hit
                cacheHitDict[i] = 1                
                print("evict", itemToEvict[0], "and add", i)

    print("Cache:", cache)

    # return to request entry
    return cache


#---------------#
# MENU FUNCTION:
#---------------#
# menu function for calling other functions

# function for evaluation of user's menu selection, calls relevant function if true, else returns to menu
def evalMenu(menuInput):
    
    if menuInput == "1":
        print("\nFIFO\n")
        fifo(requests, cache)
        # clears requests and cache lists following completion of management
        requests.clear()
        cache.clear()
    
    elif menuInput == "2":
        print("\nLFU\n")
        lfu(requests, cache)
        # clears requests and cache lists following completion of management
        requests.clear()
        cache.clear()
    
    elif menuInput == "Q":
        exit()
    
    else:
        print("Invalid input: please enter [1], [2] or [Q] to select option")
        return


#--------------------------------------#
# USER REQUESTS AND MANAGEMENT OPTIONS:
#--------------------------------------#
# the request for input is the beginning of the programme for the user
# a while loop is used to return to the requests following completion of the cache management function

start = 0

while start == 0:
    print("\nCACHE MANAGEMENT\nEnter request pages (as integers).\nEntering 0 ends the requests (but will not be requested itself)")
    
    # user input for page requests
    userRequests = input("Request: ")

    # while loop checks user input, if 0 is entered the loop is exited
    while userRequests != "0":
        
        # checks if user input is a number
        if userRequests.isnumeric():
            # cast user input as int
            userRequests = int(userRequests)
            # adds requested page to end of requests list
            requests.append(userRequests)
            # asks user for another input
            userRequests = input("Request: ")

        # if entry is not an integer, error message prompts user for a valid input 
        else:
            print("Please enter a valid positive integer")
            userRequests = input("Request: ")

    print("Requests:", requests)
    # after 0 has been entered to end requests, provide menu options for cache management

    # menuOptions is a tuple containing valid menu inputs
    menuOptions = ("1", "2", "Q")
    # menuInput is a variable for collecting user input at menu
    menuInput = 0
    
    # while loop checks if user input is a valid menu option
    # if menuInput is found in menuOptions, evaluates as false and loop breaks, returning to new page requests
    while menuInput not in menuOptions:   
        # prints menu options for cache management and requests input
        print("\nMenu")
        print("[1] Manage cache by FIFO")
        print("[2] Manage cache by LFU")
        print("[Q] Exit")
        menuInput = input("\nSelect option and press [Enter] key: ")
        # menuInput is used as the parameter in function evalMenu
        evalMenu(menuInput)
