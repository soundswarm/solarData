
import random
import math
import string
# print ('hi')
# if False:
#   print ('yo')
# else:
#   print ('bye')


letter = 'abcdefg'
# print ( letter[2:4] )


num = float('3')

arr = [[1, 'a'],2,3,4]

# for (e, i) in arr:
#   print(e,i)

list=[1,2,3,4]
# it = iter(list) # this builds an iterator object
# print (next(it)) #prints next available element in iterator
# print (next(it)) 
r = math.sin(3.14)
a = 'absdf'
arr.append('dd')
arr.pop()


# Function definition is here
# def changeme( mylist ):
#    "This changes a passed list into this function"
#    print ("Values inside the function before change: ", mylist)
#    mylist[2]=50
#    print ("Values inside the function after change: ", mylist)
#    return

# # Now you can call changeme function
# mylist = [10,20,30]
# changeme( mylist )
# print ("Values outside the function: ", mylist)
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

e = Employee('sea', 1)
e.displayEmployee()
