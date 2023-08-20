class stack:
    def __init__(self):
        self.stk=[]
    def display(self):
        print(self.stk)
    def is_empty(self):
        return len(self.stk)==0
    def push(self,data):
        self.stk.append(data)
        print("the pushed item is: ",data)
    def pop(self):
        if self.is_empty():
            print("the stack is empty!")
        else:
            ele=self.stk.pop()
            print("the poped item is: ",ele)
    def peek(self):
        top=self.stk[-1]
        print("the top item is :",top)
stack=stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.peek()
stack.pop()
stack.pop()
stack.display()
            
        
        