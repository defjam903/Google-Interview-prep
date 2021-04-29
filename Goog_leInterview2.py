# Chris Jones
# Google Coaching Call Questions

from random import *

class Node:
    def __init__(self, Item):
        self.data = Item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,Item):
        self.data = Item

    def setNext(self, Item):
        self.next = Item


class GoogleUnorderedList:
    def __init__(self):
        self.head = None

    # checks to see if the list is empty
    def isEmpty(self):
        return self.head == None

    # adds a value to the list
    # Param 1 Item to add to list
    def add(self, Item):
        temp = Node(Item)
        temp.setNext(self.head)
        self.head = temp

    # gets the size of the list
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count +1
            current = current.getNext()
        return count

    # Searches for an item n the list
    # Param 1 Item to search in the list
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    # removes an item from teh list
    # Param 1 Item to remove an item in the list
    def remove(self,Item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == Item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # prints the list
    def PrintList(self):
        current = self.head
        while current is not None:
            print(current.getData(),end=" ")
            current = current.getNext()

    # gets a random item from the list based on teh list size
    def getRandom(self):
        x = randint(1,self.size())
        current = self.head
        count = 0
        while current is not None:
            count = count +1
            if x == count:
                return current.getData()
            else:
                current = current.getNext()




# -----------INIT------------#
# create an instance of the linked list
googleList = GoogleUnorderedList()
#----------------------------#


#-----------Add------------#
# add values to the list
googleList.add(31)
googleList.add(543)
googleList.add(54)
googleList.add(565)
googleList.add(4)
googleList.add(44)
#-----------------------------#


#-----------Search------------#
# Search for a value in the list
val = 4
print('Value search for',val,'is',googleList.search(val))
#------------------------------#


#---------Remove--------------#
# Removes an item form the  list
print('Array Before = ', end= " ")
googleList.PrintList()
googleList.remove(44)
# test Remove
print('\nArray After = ',end= "")
googleList.PrintList()
#------------------------------#

#----------getRandom------------#
# Get a random item form teh list
print('\nRandom Value form list ',googleList.getRandom(), end = "")
#------------------------------#

