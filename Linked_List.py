from msilib.schema import Class
from os import remove


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head==None:
            print("Empty")
            return
        
        itr=self.head
        llstr=''
        while(itr):
            if(itr.next):
                llstr=llstr+str(itr.data)+"-->"
                itr=itr.next
            else:
                llstr=llstr+str(itr.data)
                break
        print(llstr)


    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if (self.head==None):
            self.head=Node(data,None)
            return

        itr=self.head
        while(itr.next):
            itr=itr.next

        itr.next=Node(data,None)

    def get_length(self):
        count=0
        itr=self.head
        while(itr):
            count+=1
            itr=itr.next
        return count

    def remove_at(self,index):

        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count=0
        itr=self.head
        while(itr):
            if count==index-1:
                itr.next=itr.next.next
                break

            count+=1
            itr=itr.next()

    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return
        
        count=0
        itr=self.head
        while(itr):
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count+=1
            itr=itr.next

    def remove_by_value(self,data):
        itr=self.head
        if itr.data==data:
            self.head=self.head.next
            return
        while(itr):
            if itr.next.data==data:
                itr.next=itr.next.next
                return
            itr=itr.next

    def insert_after_value(self, data_after, data_to_insert):
        itr=self.head
        if itr.data==data_after:
            node=Node(data_to_insert,itr.next)
            itr.next=node
            node.next=itr.next.next
            return
        while(itr):
            if(itr.next.data==data_after):
                itr=itr.next
                node=Node(data_to_insert,itr.next)
                itr.next=node
                node.next=itr.next.next
                return
            itr=itr.next
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(67)
    ll.insert_at_begining(7)
    ll.insert_at_begining(656)
    ll.insert_at_end(54)
    ll.print()
    print(ll.get_length())
    ll.remove_at(1)
    ll.print()
    ll.insert_at(1,100)
    ll.print()
    ll.remove_by_value(656)
    ll.print()
    ll.insert_after_value(100,112)
    ll.print()
    ll.insert_after_value(67,200)
    ll.print()
