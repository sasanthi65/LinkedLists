from Node import Node

class LinkedList:
    # Constructor to initialize head and length of linked list
    def __init__(self):
        self.head = None    # head is the reference of first node
        self.length = 0

    def ListLength(self):
        current = self.head
        count = 0
        # Traverse the linked list
        while current is not None:  # Loop executes until last node
            count = count + 1
            print(current.getData(),"--->", end=" ")
            current = current.getNext() # get the reference of the next node and assign it to current in each execution
        return count

    def addNodeBegining(self,data):
        # Creating the new Node
        newNode = Node()
        newNode.setData(data)

        # Add to the beginning
        if self.head is None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length +=1

    def addNodeEnd(self,data):
        #creating the new Node
        newNode = Node()
        newNode.setData(data)

        #Add to the end
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() is not None:
                # Loop breaks when it reaches last element
                current = current.getNext()
            current.setNext(newNode)
            newNode.setNext(None)
        self.length += 1

    def addNodeInPos(self, pos, data):

        if pos > self.length - 1 or pos < 0:
            return None

        elif pos == self.length - 1:
            self.addNodeEnd(data)
        elif pos == 0:
            self.addNodeBegining(data)
        else:
            #Creating new node
            newNode = Node()
            newNode.setData(data)
            count = 0
            current = self.head

            while count == pos -1:
                count +=1
                current = current.getNext()

            newNode.setNext(current.getNext())
            current.setNext(newNode)
        self.length +=1

    def deleteFirstNode(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.getNext()
        self.length -=1

    def deleteEndNode(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            previous = None
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            self.length -= 1


    def DeleteNodeInPos(self, pos):
        if self.head is None:
            print("List is Empty")
            return None
        if self.length > pos > -1:
            if pos == 0:
                self.deleteFirstNode()
            elif pos == self.length -1:
                self.deleteEndNode()
            else:
                count = 0
                current = self.head
                while count != pos -1:
                    count +=1
                    current = current.getNext() #get next node
                deleteNode = current.getNext()
                current.setNext(deleteNode.getNext())
                self.length -= 1
        else:
            print("Invalid Position")










