from utilz.help_func import my_func2
#from pandas import DataFrame 

print ("test code for python")
print ("now exec line 5")

print ("now exec line 9")
def myfunction(a):
    print ("now exec line 11")
    print("here we are executing some fansy function")
    for i in range(0,a,2):
        print(i)
        print(a)
    return
print ("now exec line 17")

a=15
print ("now exec line 23")
b=16
print(b)
print('now I know the variable b')
print ("now exec line 27")
print(myfunction(b))
print ("now exec line 29")
#c=DataFrame(index=[1,2,3,4,5],columns=["column1","column2"])
#print(c)

b=23


my_func2(b)



print("your request completed")
myfunction(9)


class employer:
    def __init__ (self,number,salary):
        self.number=number
        self.salary=salary
    def employerbudget(self):
        return (self.number*self.salary)

e1=employer(10,100)
print(e1.salary)
print('here is a problem in line52')