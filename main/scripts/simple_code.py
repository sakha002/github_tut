a=[1,2,3]
print(a)
print(a[1])


class employee:
    def __init__(self,salary,bonous):
        self.salary=salary
        self.bonous=bonous

    def total_salary(self):
        return(self.salary+self.bonous)
    
em1=employee(100,20)      #one instant of the function employee
print(em1)                #instance at specific location
print(em1.salary)         # pply on instance em1 property salary
print(em1.total_salary()) #apply on instance em1 method total_salary
print(em1.total_salary)   #method total_salry of the instance em1 at specific location


class employee:
    def __init__(self,sa,bo):
        self.salary=sa;
        self.bonous=bo;

    def total_salary(self):
        return(self.salary+self.bonous)
    
em1=employee(100,20)      #one instant of the function employee
print(em1)                #instance at specific location
print(em1.salary)         # pply on instance em1 property salary
print(em1.total_salary()) #apply on instance em1 method total_salary
print(em1.total_salary)   #method total_salry of the instance em1 at specific location

class engineer(employee):  #class engineer inherit properties\methods from class paretn employee
    pass
em2=engineer(200,40)
print(em2)                  #engineer instance\object at specific location
print(em2.salary)

class engineer(employee):
    def __init__(self,salary,bonous,engineerbonous):
        employee.__init__(self,salary,bonous)       #add property parent to the class (inherits all the properties&function of parent)
        self.engineerbonous=engineerbonous    #add extra property engin.. to the class engineer
    def engineertotal_salary(self):               #add extra function engi.. to the class engineer
        return(self.salary+self.bonous+self.engineerbonous)

em3=engineer(200,40,20)
print(em3.salary)
print(em3.engineerbonous)
print(em3.total_salary()) 
print(em3.engineertotal_salary()) 


b=[3,4,5,6,7]
print(iter(b))


