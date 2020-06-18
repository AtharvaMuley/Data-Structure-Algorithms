"""
Author: Atharva Muley
Date: Jan 31 2020
"""
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class DoublyList(ListNode):
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
                temp.prev = self.tail
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
                    next.prev = prev
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

    def __str__(self):
        out = "Linked List: "
        temp = self.head
        while temp != None:
            out += "{} ".format(temp.val)
            temp = temp.next
        # out += '\n'
        return out


if __name__ == "__main__":
    custom_list = DoublyList()
    custom_list.insertNode([4,1,2,3,4])
    print(custom_list)
    custom_list.removeElement(3)
    print(custom_list)
    print(custom_list.getNodeCount())