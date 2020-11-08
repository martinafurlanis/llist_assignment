"""
Linked list assignment:
1) Your (individual) assignment is the development of a linked list. Using object-oriented programming, define a class Node
that will hold the data as well as a reference to the next element. The class Node also needs a method insert that
inserts a new element right after itself and before the previously next element.
"""

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList():
    def __init__(self, head=None):
        self.head = head


    # function "insert_after_node" takes value of the previous element as a string and inserts a new node after the
    # previous element

    def insert_after_node(self, prev_node, newdata):
        new_node = Node(newdata)
        cur_node = self.head
        while cur_node.value != prev_node:
            cur_node = cur_node.next
            if cur_node is None:
                print("previous node is not present in the list")
                return
        new_node.next = cur_node.next
        cur_node.next = new_node


    # to insert an element in the middle of the list, the function "insert_mid" finds the position of the middle node
    # starting from the head and inserting the new node after this element
    # when the middlenode is found, we create a new node and change next attribute until end of the linked list

    def insert_mid(self, middlenode, newvalue):

        # if the middlenode is not found, a message appears
        if middlenode is None:
            print("This node is not in the list")
            return

        newnode = Node(newvalue)
        newnode.next = middlenode.next
        middlenode.next = newnode


    # function "insert_end" inserts the element at the beginning creating a head if the linked list is empty
    # if our element is not the head tail, we traverse the list and find the tail starting from the head value

    def insert_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return node

        currentnode = self.head

        while True:
            if currentnode.next is None:
                currentnode.next = node # if there is no node at the end, we insert is at the end
                break
            currentnode = currentnode.next


    # function "printlist" starts traversing the string from the beginning (head of the list) and prints all elements
    # after that until the last node

    def printlist(self):
        currentnode = self.head

        while currentnode is not None:
            print(currentnode.value)
            currentnode = currentnode.next
        return print("none")


ll = LinkedList()
ll.insert_end("3")
ll.insert_end("7")
ll.insert_end("10")
ll.insert_end("12")

# insert new element after second position
ll.insert_mid(ll.head.next, "9")

# insert new element after nr 10
ll.insert_after_node("10", "11")

ll.printlist()


"""
2) Your second task is verifying this by creating differently sized lists and adding a new element somewhere (note that 
finding the element is not part of calculating the time complexity; hence you could always enter an element 
after the first position).
"""

"""
Inserting an element in a linked list has always a constant time complexity of O(1), as it always require same amount of
work to insert the new code. 
"""



import time
import matplotlib.pyplot as plt

llist = LinkedList()
llist.insert_end("0")

results = []
list_lenghts = [100, 200, 400, 800]

for l in list_lenghts:
    numbers = range(l)
    for i in numbers:
        llist.insert_end(i)

    first_time = time.time()
    llist.insert_after_node("0", "element_to_insert")
    last_time = time.time()
    final_time = last_time - first_time
    results.append(final_time)

print(results)
plt.plot(list_lenghts, results)
plt.ylim(0, 0.0002)
plt.show()