#Khai bao toan cuc
import llist
from llist import dllist

#lst = llist.dllist(['first', 'second', 'third'])
#for value in lst:
#    print(value)








#Khoi tao, nhap gia tri
i=0

class node:
    def __init__(self, k=0, p=None, n=None):
        self.key = k
        self.prev = p
        self.next = n

head = None
first = None
temp = None
tail = None


#Doc phan tu
def traverse():
    
    ptr = head

    while ptr != None:
        print(ptr.key, end=" ")
        ptr = ptr.next

    print()








#Them phan tu
def addnode(k:int):
    global i,head,first,tail
    
    ptr = node(k)

    if head == None:
        head = ptr
        first = head
        tail = head

    else:
        temp = ptr
        first.next = temp
        temp.prev = first
        first = temp
        tail = temp
    
    i+=1

def insertatbegin(k:int):
    global head, first, tail, i

    ptr = node(k)

    if head == None:
        first = ptr
        first = head
        tail = head

    else:
        temp = ptr
        temp.next = head
        head.prev = temp
        head = temp

    i+=1

def insertatend(k:int):
    global head, first, tail, i

    ptr = node(k)

    if head == None:
        first = ptr
        first = head
        tail = head

    else:
        temp = ptr
        temp.prev = tail
        tail.next = temp
        tail = temp

    i+=1


def insertatpos(k:int, pos:int):
    global i

    if pos < 1 or pos > i + 1:
        print("Please enter a" " valid position")

    elif pos == 1:
        insertatbegin(k)
            

    elif pos == i + 1:
        insertatend(k)

    else:
        src = head

        while pos:
            pos-=1
            src = src.next

        ptr = node(k)

        ptr.next = src
        ptr.prev = src.prev
        src.prev.next = ptr
        src.prev = ptr
        i+=1

#Xoa phan tu
def delatbegin():
    global head,i
    head = head.next
    i-=1

def delatend():
    global tail, i
    tail = tail.prev    
    tail.next = None
    i-=1


def delatpos(pos: int):
    global i
    if pos < 1 or pos > i + 1:
        print("Please enter a" " valid position")

    elif pos == 1:
        delatbegin()
    elif pos == i:
        delatend()
    else:
        src = head
        pos-=1
        
        while pos:
            pos-=1
            src = src.next

        src.prev.next = src.next
        src.next.prev = src.prev

        i-=1


#Viet chuong trinh mau
if __name__ == "__main__":
    addnode(2)
    addnode(4)
    addnode(9)
    addnode(1)
    addnode(21)
    addnode(22)

    print("Doubly Linked List: ")
    traverse()

    print("\n")

    insertatbegin(1)
    print("Doubly Linked List after inserting 1 at beginning: ")
    traverse()

    insertatend(0)
    print("Doubly Linked List after inserting 0 at end: ")
    traverse()

    insertatpos(44, 3)
    print("Doubly Linked List after inserting 44 at 3rd Node: ")
    traverse()


    print("\n")


    delatbegin()
    print("Doubly Linked List after deleting node at beginning: ")
    traverse()

    delatend()
    print("Doubly Linked List after deleting node at end: ")
    traverse()

    print("Doubly Linked List after deleting node at position 5: ")
    delatpos(5)
    traverse()

    print("Is 9 in the list:", search(9))

    print("Reverse traverse:")
    reverse_traverse()

    sort()
    print("Doubly Linked List after sorting:")
    traverse()


#Tim kiem thong tin
def search(key):
    ptr = head
    while ptr is not None:
        if ptr.key == key:
            return True
        ptr = ptr.next
    return False








#Duyet va sap xep cac phan tu
def reverse_traverse():
    ptr = tail
    while ptr is not None:
        print(ptr.key, end=" ")
        ptr = ptr.prev
    print()

def sort():
    if head is None:
        return
    current = head
    while current.next is not None:
        temp = current.next
        while temp is not None:
            if current.key > temp.key:
                current.key, temp.key = temp.key, current.key
            temp = temp.next
        current = current.next








#Viet chuong trinh quan ly du lieu sach bang Python








