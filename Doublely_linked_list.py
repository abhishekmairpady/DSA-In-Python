from itertools import count


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class doubely_ll:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
            if self.head == None:
                node = Node(data, self.head, None)
                self.head = node
            else:
                node = Node(data, self.head, None)
                self.head.prev = node
                self.head = node
    
    def insert_at_end(self,data):
        if self.head==None:
            self.insert_at_begining(data)
            return
        
        itr=self.head
        while(itr.next):
            itr=itr.next

        itr.next=Node(data,None,itr)


    def print_forward(self):
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

    def print_backward(self):
        if self.head==None:
            print("Empty")
            return

        itr=self.head
        llstr=''
        while(itr.next):
            itr=itr.next
        
        while(itr):
            if(itr.prev==None):
                llstr=llstr+str(itr.data)
                break
            else:
                llstr=llstr+str(itr.data)+"-->"
                itr=itr.prev
        print(llstr)

    def get_length(self):
        count=0
        itr=self.head
        while(itr):
            itr=itr.next
            count+=1
        return count

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
            
        if index==0:
            self.head=self.head.next
            self.head.prev=None
        else:
            itr=self.head
            count=0
            while(itr):
                if count==index-1:
                    itr.next=itr.next.next
                    itr.next.next.prev=itr
                count+=1
                itr=itr.next


if __name__ == '__main__':
    ll = doubely_ll()
    ll.insert_at_begining(100)
    ll.insert_at_begining(101)
    ll.insert_at_begining(103)
    ll.insert_at_begining(104)
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end(60)
    ll.insert_at_end(800)
    ll.print_forward()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print_forward()
        


