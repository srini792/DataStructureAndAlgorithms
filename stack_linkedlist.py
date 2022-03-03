# problem here is list as a stack


class stackList():
    def __init__(self):
        self.stack = []

    def push(self,n,data):
        if len(self.stack) == n:
            print("stack is full!..")
        else:
            self.stack.append(data)
            print(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty....!")
        else:
            self.stack.pop()
            print(self.stack)


stackLimit = int(input("Enter the limit of stack:"))
stack_obj = stackList()
while True:
    choice = input("1.push,2.pop,3.exit: ")
    if choice is "1":
        data = int(input("enter data to push:"))
        stack_obj.push(stackLimit,data)
    elif choice is "2":
        stack_obj.pop()
    else:
        break