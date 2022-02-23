class Node:
    # Constructor to initialize the node object
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    # Set data to the node instance
    def setData(self, data):
        self.data = data

    # Get data from the node instance
    def getData(self):
        return self.data

    # Set the reference to the next node
    def setNext(self, next):
        self.next = next

    # Get the reference of the next node
    def getNext(self):
        return self.next

    # Check whether the node has a next node
    def hasNext(self):
        return self.next is not None

    # Set the reference to the previous node
    def setPrev(self, prev):
        self.prev = prev

    # Get the reference of the previous node
    def getPrev(self):
        return self.prev

    # Check whether the node has a previous node
    def hasPrev(self):
        return self.prev is not None
