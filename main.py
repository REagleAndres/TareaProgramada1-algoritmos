import gc
import numpy

class listPointer:
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
            if str(newKey) == self.orderList[i][0]:
                return 
            i += 1
        
        i -= 1
        newPair = (str(newKey), str(newValue))
        self.orderList.insert(i, newPair)
        
    def Unassign(self, delKey):
        for i in range(self.orderList.len()):
            if delKey == self.orderList[i][0]:
                self.orderList.pop(i)
        
    def Lookup(self, key): ##Retorna 0 si la lista no contiene la llave
        for i in range(self.orderList.len()):
            if key == self.orderList[i][0]:
                return self.orderList[i][0]
        return 0
    
    def Keys(self):
        allKeys = []
        for i in range(self.orderList.len()):
            allKeys.append(self.orderList[i][0])
        print(allKeys)
        return allKeys
    
    def Print(self):
        for i in range(self.orderList.len()):
            print("Llave: " + i + self.orderList[i][0] + "Valor: " + i + self.orderList[i][1])
            
class listArray: ##refactorizar a array
    def __init__(self):
        self.orderList = numpy.array(numpy.array([]), dtype= 'S')
        pass
    
    def Done(self):
        del self.orderList
        gc.collect()
        
    def Clear(self):
        del self.orderList
        gc.collect()
        self.orderList = numpy.array([], dtype= 'S')  
        
    def Assign(self, newKey, newValue):
        
        if str(newKey).len() > 20 or str(newValue) > 20:
            raise ValueError("no se permite datos mayores a 20")
        
        i = 0
        while i > self.orderList.len() and str(newKey) >= self.orderList[i[0]]:
            if str(newKey) == self.orderList[i][0]:
                return 
            i += 1
        
        i -= 1
        newPair = (str(newKey), str(newValue))
        self.orderList.insert(i, newPair)
        
    def Unassign(self, delKey):
        for i in range(self.orderList.len()):
            if delKey == self.orderList[i][0]:
                self.orderList.pop(i)
        
    def Lookup(self, key): ##Retorna 0 si la lista no contiene la llave
        for i in range(self.orderList.len()):
            if key == self.orderList[i][0]:
                return self.orderList[i][0]
        return 0
    
    def Keys(self):
        allKeys = []
        for i in range(self.orderList.len()):
            allKeys.append(self.orderList[i][0])
        print(allKeys)
        return allKeys
    
    def Print(self):
        for i in range(self.orderList.len()):
            print("Llave: " + i + self.orderList[i][0] + "Valor: " + i + self.orderList[i][1])
    
class binaryTree:
    
    
class trie:
    
    
class hashTable():
    

def main():
    print("Hello from tareaprogramada1!")


if __name__ == "__main__":
    main()
