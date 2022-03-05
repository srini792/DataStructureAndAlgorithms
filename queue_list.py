# queue works in fifo
# two main operation (enqueue and dequeue)
class queue_list:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.queue:
            print("queue is empty..!")
        else:
            self.queue.pop(0)
    def print_queue(self):
        print(self.queue)

ql = queue_list()
ql.enqueue(10)
ql.enqueue(11)
ql.dequeue()
ql.dequeue()
ql.dequeue()
ql.print_queue()