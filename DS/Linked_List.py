class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class List(ListNode):
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    def insertNode(self, values):
        if type(values) != list:
            values = [values]

        for each in values:
            if self.head == None:
                self.head = self.tail = ListNode(each)
            else:
                temp = ListNode(each)
                self.tail.next = temp
                self.tail = temp
            self.node_count += 1
    
    #Removes the first occurence of the Element
    def removeElement(self, value):
        curr = self.head;prev=None;next=None
        while curr != None:
            next = curr.next
            if curr.val == value:
                if prev:
                    prev.next = next
                    del curr
                else:
                    self.head = next
                self.node_count -= 1
                return
            prev = curr
            curr = curr.next
        
        print("Element Not Present in the list")

    #Returns the number of nodes present in the list
    def getNodeCount(self):
        return self.node_count

    def printList(self):
        temp = self.head
        while temp != None:
            print("{}".format(temp.val), end=" ")
            temp = temp.next
        #Added blank print() to stop printing grabage character on Mac OS
        print()

if __name__ == "__main__":
    custom_list = List()
    custom_list.insertNode([4,1,2,3,4])
    custom_list.insertNode(6)
    custom_list.insertNode(7)
    # custom_list.removeElement(1)
    custom_list.printList()
    print(custom_list.getNodeCount())
