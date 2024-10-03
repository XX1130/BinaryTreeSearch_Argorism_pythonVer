class BinaryClass:
    own = 1
    
    def __init__(self,root,d = 0):
        self.own = root
        self.leftB = None
        self.rightB = None
        self.depth = d
    
    def insert (self,newValue):
        if newValue < self.own :
            if self.leftB == None :
                self.leftB = BinaryClass(newValue, self.depth+1)
            else:
                self.leftB.insert(newValue)
        
        elif newValue > self.own :
            if self.rightB == None :
                self.rightB = BinaryClass(newValue, self.depth+1)
            else:
                self.rightB.insert(newValue)
        
    def search (self,target):
        if (self.own == target):
            return "found: "+ str(self.own) +"\ndepth: "+str(self.depth)
        elif(self.own<target):
            if(self.rightB != None):
                return self.rightB.search(target)
            else:
                return "Not Found"
        else:
            if(self.leftB != None):
                return self.leftB.search(target)
            else:
                return "Not Found"
        

        

                
    
    