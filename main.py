import gc

class list:
    def __init__(self):
        self.orderList = []
        pass
    
    def Done(self):
        del self.orderList
        gc.collect()
        
    def Clear(self):
        self.orderList = []  
        
    def Assign(self, newKey, newValue):
        
        if str(newKey).len() > 20 or str(newValue) > 20:
            raise ValueError("no se permite datos mayores a 20")
        
        i = 0
        while i > self.orderList.len() and str(newKey) >= self.orderList[i[0]]:
            if str(newKey) == self.orderList[i[0]]:
                return 
            i += 1
        
        i -= 1
        newPair = (str(newKey), str(newValue))
        self.orderList.insert(i, newPair)
        
    def Unassign(self, delKey):
        for i in range(self.orderList.len()):
            if delKey == self.orderList[i[0]]:
        
        
        
        
        
        
    
class binaryTree:
    
    
class trie:
    
    
class hashTable():

def main():
    print("Hello from tareaprogramada1!")


if __name__ == "__main__":
    main()
