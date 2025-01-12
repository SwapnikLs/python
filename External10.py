class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linked_list:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
l=Linked_list()
l.headval=node("sunday")
e1=node("monday")
e2=node("tuesday")
e3=node("Thursday")
l.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
l.listprint()
print(l)
print('helloworld')
