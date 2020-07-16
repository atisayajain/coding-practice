class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        stack = []
        cur = head
        while(cur != None):
            data = cur.data
            prev = cur
            nex = cur.next
            while(nex != None):
                #print(nex.data)
                if (nex.data == data):
                    #print('yes')
                    if (nex.next != None):
                        prev.next = nex.next
                    else:
                        prev.next = None
                    #print(prev.data, prev.next.data)
                else:
                    prev = nex
                nex = nex.next
            cur = cur.next
        #stack.append(cur.data)
        #count = counter
        #print(stack)
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head);
