class queue:
    def __init__(self):
        self.que=[]
    def dispaly(self):
        print(self.que)
    def is_empty(self):
        return len(self.que)==0
    def enqueue(self,data):
        self.que.append(data)
        print("enqueued item:",data)
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            ele=self.que.pop(0)
            print("popped item is :",ele)
q=queue()
q.enqueue(5)
q.enqueue(9)
q.dispaly()
q.dequeue()
q.dequeue()
q.dequeue()