class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        return node(data)
    else:
        if data<root.data:
            root.left=insert(root.left, data)
        else:
            root.right=insert(root.right, data)
    return root

def search(root,data):
    if root is None or root.data==data:
        return root
    if data>root.data:
        return search(root.right,data)
    return search(root.left,data)

def delete(root,data):
    if root is None:
        return root
    if data<root.data:
        root.left=delete(root.left,data)
    elif data>root.data:
        root.right=delete(root.right,data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp=min_value_node(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root


def min_value_node(node):
    current=node
    while current.left is not None:
        current=current.left
    return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
root=None
root=insert(root, 30 )
root=insert(root, 40 )
root=insert(root, 50 )
root=insert(root, 60 )
inorder(root)
root=delete(root,40)
search_result=search(root,60)
if search_result:
    print("\npresent")
else:
    print("\nABSENT")



