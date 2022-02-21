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