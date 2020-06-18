"""
Author: Atharva Muley
Date: Jan 31 2020
Description: Uses Linked List to implement Circular Queue
"""
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class CircularLinkedList(ListNode):
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.node_count = 0
        self.size = size
        print("Initialized a Circlar Queue with size: {}".format(size))

    #Insert element at the end of the Queue
    def insert(self, values):
        if type(values) != list:
            values = [values]
        count = 0
        for each in values:
            if self.size == self.node_count:
                print("Circular Queue Full!. Could add only {} elements".format(count))
                return

            if self.front == None:
                self.front = self.rear = ListNode(each)
            
            else:
                temp = ListNode(each)
                self.rear.next = temp
                self.rear = temp
            self.node_count += 1
            count += 1
    
    #Remove element from the front of the queue
    def remove(self):
        if self.front is None:
            print("Circular Queue is Empty!")
            return
        temp = self.front
        self.front = self.front.next
        self.node_count -= 1
        del temp

    #Returns the number of nodes present in the list
    def getNodeCount(self):
        return self.node_count

    def __str__(self):
        out = "Circular Queue: ["
        if self.node_count == 0:
            return "Circular Queue is Empty!"
        temp = self.front
        while temp != self.rear:
            out += "{} ".format(temp.val)
            temp = temp.next
        if self.rear:
            out += "{}]".format(self.rear.val)
        return out

if __name__ == "__main__":
    custom_list = CircularLinkedList(5)
    custom_list.insert([4,1,3])
    # custom_list.insert(6)
    # custom_list.insert(7)
    print(custom_list)
    print(custom_list.getNodeCount())
