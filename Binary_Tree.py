class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left= BinarySearchTreeNode(data)

        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()
        
        return elements

    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)

        if self.left:
            elements+=self.left.pre_order_traversal()
        
        if self.right:
            elements+=self.right.pre_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.pre_order_traversal()
        
        if self.right:
            elements+=self.right.pre_order_traversal()
        elements.append(self.data)

        return elements
    
    def search(self,data):
        if self.data==data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        if self.left:
            return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        if self.right:
            return self.right.find_max()
        
    def sum_of_tree(self):
        sum=self.data
        if self.left:
            sum+= self.left.sum_of_tree()
        if self.right:
            sum+= self.right.sum_of_tree()
        return sum

    def delete(self, val):
        if val < self.data:
            self.left=self.left.delete(val)
        elif val> self.data:
            self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val= self.right.find_min()
            self.data=min_val
            self.right.delete(min_val)
        return self

    def delete1(self,val):
        if val<self.data:
            self.left=self.left.delete1(val)
        elif val>self.data:
            self.right=self.right.delete1(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val=self.left.find_max()
            self.data= max_val
            self.left.delete1(max_val)
        return self
        

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
    
if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.sum_of_tree())

    numbers_tree1= build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree1.delete(17)
    print("After deleting 17 ",numbers_tree1.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]

    numbers_tree1= build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree1.delete1(23)
    print("After deleting 23 ",numbers_tree1.in_order_traversal())  