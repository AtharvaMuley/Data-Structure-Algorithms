class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
    
class List(ListNode):
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    def addNode(self, value):
        if self.head == None:
            self.head = self.tail = ListNode(value)
        else:
            temp = ListNode(value)
            self.tail.next = temp
            self.tail = temp
        self.node_count += 1
    
    def printList(self):
        temp = self.head
        while temp != None:
            print("{}".format(temp.val), end=" ")
            temp = temp.next
        #Added blank print() to stop printing grabage character on Mac OS
        print()

if __name__ == "__main__":
    custom_list = List()
    custom_list.addNode(4)
    custom_list.addNode(1)
    custom_list.addNode(2)
    custom_list.printList()
