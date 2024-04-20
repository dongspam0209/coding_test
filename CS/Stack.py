class Stack():
    
    def __init__(self):
        self.stack=[]
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        
        if self.isEmpty():
            print("Error Stack is Empty")
            return None
        
        popped_object=self.stack.pop()
            
        return popped_object
    
    def isEmpty(self):
        is_empty=False
        if len(self.stack)<=0:
            is_empty=True
            
        return is_empty
    
    def top(self):
        top_object=None
        if self.isEmpty():
            print(top_object)
        else:
            top_object=self.stack[-1]
            
        return top_object
    
def main():
    test=Stack()
    test.push(3)
    print("top data of stack is ",test.top())
    print("popped data of stack is ",test.pop())
    print("popped data of stack is ",test.pop())
    

if __name__=="__main__":
    main()