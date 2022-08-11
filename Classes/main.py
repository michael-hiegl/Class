

class Calc:
    
    i=10
    
    def __init__(self,firstnumber,secondnumber):
        self.firstnumber=firstnumber
        self.secondnumber=secondnumber
        
    def sum(self):
        result=self.firstnumber*self.i+self.secondnumber
        return result
    
new=Calc(5,4)

print(new.sum())




