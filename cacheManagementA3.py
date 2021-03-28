# Name: Orion Assefaw , COMP517 Assignment 3(CA3)

# Declaring the cache and requests list with a global scope
cache = []
requests = []

# mainMenu()- First asks user to input page requests
# Takes user input(int) by prompting user to repeatedly type in their page requests until 0 is typed
def mainMenu():
    print("Welcome to the Cache Management System!!")
    print("Please input your all your requests and input 0 when all the requested pages are inputed ")
    page = None
    while page != "0":        
        page = (input())
        requests.append(int(page))
    requests.remove(0)
        
    print("Thank you for the input!!")

    # Displaying requested pages to user
    print("You have requested the following page/es", requests)

    # Providing the user with 3 options; FIFO, LFU or Quit options
    option = input(
        "Please select one of the following options :\n 1- For FIFO \n 2- For LFU \n Q- To Quit program \n")

    # "FIFO" Cache Management System, calls fifo() function and then clears stored data and returns user back to menu
    if (option == "1"):
        fifo()        
        cache.clear()
        requests.clear()
        mainMenu()

    # "LFU" Cache Management System, calls lfu() function and then clears stored data and returns user back to menu
    elif(option == "2"):
        lfu()
        cache.clear()
        requests.clear()
        mainMenu()

    # Option for quiting the program all together
    elif((option == "q") or (option == "Q")):
        raise SystemExit

    # Invalid Input checker. Takes user back to main menu again if invalid input is given
    else:
        print("Oops!! Invalid Input! Please try again to enter a valid input \n")
        mainMenu()


 # fifo() - Searches the cache for the requested page and if page is present prints "HIT" and if not prints "MISS".
 #        - The FIFO system places any “MISS” into the cache up until the cache is full.
 #        - When the cache is full, the first page that was requested gets evicted (removed) from the cache.
 # Returns: A list of the final cache
def fifo():
    for i in range(len(requests)):
        if (requests[i] not in cache):
            print("MISS")
            print("Requested Page",requests[i], "was not present in the already existsing cache ")

            if(len(cache) < 8):
                cache.append(requests[i])
                print("Cache now is:", cache, "\n")
            else:
                cache.reverse()
                cache.pop()
                cache.reverse()
                cache.append(requests[i])
                print("Cache now is:", cache, "\n")

        else:
            print("HIT")
            print("Requested Page", requests[i], "is already in cache \n")

    print("The final Cache is:", cache, "\n")
    return cache


 # lfu() - Searches the cache for the requested page and if page is present prints "HIT" and if not prints "MISS".
 #        - The LFU system places any “miss” into the cache up until the cache is full.
 #        - When the cache is full, the page that has the fewest “hits” is evicted (removed) from the cache.
 # Returns: A list of the final cache
def lfu():
    freqRequests = []
    for i in range(len(requests)):

        if(requests[i] in cache):
            print("HIT")
            print("Requested Page", requests[i], "is already in cache \n")
            freqRequests.append(requests[i])
        else:
            print("MISS")
            print("Requested Page",
                  requests[i], "was not present in the already existsing cache ")

            if(len(cache) < 8):
                freqRequests.append(requests[i])
                cache.append(requests[i])

            else:
                # Calling the lfuHelper function on the freRequests lists so as to remove least frequent page
                cache.remove(lfuHelper(freqRequests))
                removedElem = lfuHelper(freqRequests)
                while removedElem in freqRequests:
                    freqRequests.remove(removedElem)
                cache.append(requests[i])
                freqRequests.append(requests[i])

            print("Cache now is:", cache, "\n")
    print("The final Cache is:", cache, "\n")
    return cache


# lfuHelper(aList)  – A function that helps the lfu function in removing the least frequent page
# Parameters:       – aList: takes any list of ints as parameter (In the lfu() case, takes the frequency requests list)
# returns           – int : the least frequent element in the list.
#                   - In case of two ints having the same frequency, the lowest numbered int is returned.
def lfuHelper(aList):
    myset = set(aList)
    minElem = aList[0]
    min = requests.count(minElem)
    for nos in myset:
        newElem = nos
        newCount = aList.count(newElem)
        if(newCount < min):
            minElem = newElem
            min = newCount
        elif(newCount == min):
            continue
        else:
            pass
    return minElem


# Program Initiator
mainMenu()