                #object oriantation programmes (oops)
                       #AGENDA
#introduction to oops
#real-world opps example
#oops - classes and objects
#inheritance in python
#encapsulation in python
#polymotphism in python
#python modules
#standard library
#installing packages
#exception handling

# 1) ->introduction (class [form in object]
#   ex :parrot is a class -> it have two >>*ATTRIBUTE:age,color (data about the object)
#                                    *behaviour:singing .danceing
#       basic principle of oops:
#              1.class ;2.object; 3.encapsulation; 4.inheritance; 5.polymorphism

#2) ->real-world opps example:
#        human being is a class -> *ATTRIBUTE:they have body parts(nose.eye ect..)
#                                  *behaviour: they can walk, see ,small ect....
#         "name" and "age are object of class male
#     inheritance in python:
#        male and female are "inherited" from class human being
#           specifice thinks is different can be over it known
#     encapsulated
#         you don't known the detail of how u walk . listen or see
#     polymorphism
#          she'can be a woman,mother,teacher at the same time
#          she can being able to perform so many task
#
#3) ->opps-class & object
#       class are the blue print of house
#       objest is the real house & creat the blueprint
#
#     creat a class in python
class classname:
    variable = "i am a class attribute" # attribute
    def function(self):                 # behaviours
        print("i am inside of the class")
 #     creat a object in python
#     a = classname()
#     a
#         how to access the class member
#obj1 = classname()
#obj2 = classname()
#obj2.variable = "i was just created"
#print(obj1.variable)
#print (ibj2. variable)
#print (classname.variable)
#obj1.function()
#           __init__()in python
class dog: #class
    def __init__(self , name):
       self.name = name

    def talk(self):
       print("wooop!")

    def sayname(self):
       print("my name is : {}".format(self.name))
charly = dog("charly") #objects
charly.talk()
charly.sayname ()

jonsy = dog("jonsy")  #objects
jonsy.talk()
jonsy.sayname()
#        some cars example
class cars:
    def __init__(self, name , color, price):
        self.name  = name
        self.color = color
        self.price = price
    def description(self):
        print("my name is : {}".format(self.name))
        print("my color is: {}".format(self.color))
        print("my price is: {}".format(self.price))

    def description2(self):
         print("my name is : {}".format(self.name))
         print("my color is: {}".format(self.color))
         print("my price is: {}".format(self.price))
car1 = cars("ferrari","red","$17,00,000")
car1.description()

car2 = cars("jeep","blue","$18,00,000")
car2.description2()

#inheritance in python
#       u would have inheritance few qualities of from in parent class
#  types of inheritance:
#                    1.single inheritance
#                    2.multiple inheritance
#                    3.multilevel inheritance
#                    4.hierarchical inheritance
#                    5.hybrid  inheritance
#
#     1.single inheritance
class person:                         #  class fruit:
    def __init__(self, name):         #      def __init__(self):
      self.name = name                #          print(i'am a frulit)
    def sayname (self):               #  class citrus(fruit):
       print(self.name)               #     def__int__(self):
class engineer(person):               #         super()__ihit__()
    def __init__(self, name):         #         print(i'm citrus)
      super().__init__(name)
      self.porfession = "engineer"    #  lemon = citrus()
    def sayporfession(self):
       print(self.porfession)
a =engineer('jay')
a.sayporfession()                      # a.sayname
#       2.multiple inheritance
class A:                                  #class A:
   def printA(self):                      #    pass
       print("from A")                    #class B(A):
class B:                                  #    pass
  def printB(self):                       #class C(A ,B)
     print("from B")
class c(A,B):
  def printC(self ):
     print("from C")
obj = c()
obj.printA()
obj.printB()
obj.printC()
#        3.multilevel inheritance
#class A:
#   X= 1
#classB(A):
#   pass
#classC(B):
#    pass
#obj = c()
#0bj,x
#
#       4.hierarchical inheritance
class person:
    def __init__(self, name):
        self.name = name
    def sayname(self):
        print(self.name)
class engineer(person):                   #class A:
    def __init__(self, name):             #    pass
        super().__init__(name)            #class B(A):
        self.porfession = "engineer"      #    pass
    def sayporfession(self):              #class C(A):
        print(self.porfession)            #    pass
class doctor(person):                     #
    def __init__(self, name):             #
        super().__init__(name)
        self.porfession = "doctor"
    def sayporfession(self):
        print(self.porfession)
a = engineer('jay')
a.sayporfession()
a.sayname()
b = doctor ('jene')
b.sayname()
b.sayporfession()

#       5.hybrid  inheritance
#class A:
#    x = 1
#class B(A):
#    pass
#    pass
#class D (C,B)
#    pass
#obj = d()
# obj.x
                # supper function
class vehicel:
    def start(self):
        print("start engine")
    def stop(self):
        print('stop engine')
class twowheeler(vehicel):
    def say(self):
        super().start()
        print("i have two wheels")
        super().stop()
harley = twowheeler()
harley.say()
                #  overwritting
class base:                   #class base :
    def add(self,a , b):      #   def ad(self , a ,c )
        return (a + b)        #       return (a+ b)
class derived:                #class derived:
    def sub(self, a , b):     #    def su(self , a,c)
        return (a + b + 1)    #        return (a+b+c)
obj = base()                  #obj = base()
obj1 = derived()              #obj1 = derived()
print(obj.add(2 ,3))          #print(obj.ad(2,3))
print(obj1.sub(2,3))          #print (obj.su(2,3)) it is called overwritting

              # overloading
def add(*arg):
    if (len(arg) == 2): return arg[0] + arg[1]
    result = 0
    for x in arg:
         result +=x

    return result
print (add(1,3))
print(add (1,8,3,4,5))
#4) -> encapsulation in python
# it is contain in abstraction + data hinding
# ex : email , gmail
#
#  how to access a private method
#      private method  = use in __function
# to chang the vlaue: use in   def setmaxspeed(self.speed)
#                                    self__maxspeed = speed
#                               redcar = car()
#                               rsdcar.drive()
#                               redcar.setmaxspeed(340)
#                                redcar.ddive()
#          private function
class someclass:
    def public(self):
       print("public function")
    def __private(self):
       print("private function")
obj = someclass ()

obj.public()
obj._someclass__private() #not use in "obj.private"
#           build with private variable ->bankes
class account:
    def __init__(self):
       self.setbalance(48)
    def setbalance(self,balance):
       self.__balance = balance   # can'n return the private
    def getbalance(self):
      print(self.__balance)
bank  = account()
print(bank.getbalance())
bank.setbalance(88)
print(bank.getbalance())

 #5)-> polymotphism in python
#           function with same name but face in different ways
#           it also called as overewriting
#           different person in different behaves
#           single person behave different at different time
# example ->
#def in_the_pacific(fish):
#fish.swim()
#sammy = shark()
#casey = clownfish()
#in_the_pacific(sammy)
#in_the_pacific(casey)

class worker:
    def work(self):
        print("working")
    def perform_task(self):
        print("perform_task : ",end=" ")
        self.work()
class deliveryman(worker):
    def work(self):
        print("delivering goods")
class lumberjack(worker):
    def work(self):
        print(" cutting wood")
deliveryman = deliveryman()
lumberjack = lumberjack()
deliveryman.perform_task()
lumberjack.perform_task()

#7) ->python modules
#            module is a file containg python code
#            module can define funtion , classes , variable and can also inculded
#running code; there are pre-define modulles in python standard library
# their are use to two keys
#       from key;
#               to specoty the thing that u want to import from a module
#       import key:
#               import the complete module
#def add(X ,Y):          |
#   return X + Y         |
#                        | -> use in other file (data scince tester)
#def add(X ,Y):          |
#   X + Y          |

from worldfirst import add,sub

print(add(3,5))
print( sub(8,9))
#          or

import worldfirst
print(worldfirst.add(3,5))
print(worldfirst. sub(8,9))

#7)  ->standard library
#        it is vary extensive & offer a wide rang of facilities
#        it contain bulit-in modules,
#        privide access funtionalities such as I/O
#        all data types ,funtion , mopdules we leaaned sofar are avaliable
#                               becomes of S.L

import os
print(os.listdir('./scripts'))
#       or
from os import listdir
print(listdir('./scripts'))

#9) -> installing packages
#from colorama import init
#from termcolor import colored
#init()
#print(colored("best scientist","white"))

#10)-> exception handin))->>>
#              it is runtime error caused by things that are outside the develope
# control control , ex:file is not foundexception ect...
#              this process of writing code which can expect thing to go wrong
# and rause exceptions and handle them accordingly
#
# they are 4 type :
#             try , except ,finaly , raise
# try:)->>>>
#      code block that could throw an exceptiom
#                                                          try & except:
#def throw_exception(num):                                       #    throw_custom_exception()
#    if (num == 0): raise Exception("argument 0 is not accepted")#except myexceotion as :
#    else:print(0)                                               #    print(e)
#throw_exception(0)
#print(done)# it is nameError
#                    this problem is over come to below
def throw_exception(num):
    if (num == 0): raise Exception("argument 0 is not accepted")
    else:print(num)
try:
   throw_exception(4)
except Exception as ex:
    print(ex)
else:
    print("not thrown")
finally:         # finally:
#       code block that gets run even if an exception is thrown or not
    print('done')

# raise: ->>>>>
#class myException(Exception):
#def __init__(self):
#        super(Exception, self).__init__()
#        self.args = ("raised myException",)
#raise myException()# it is error statement
#                this problem is overcome in below
class myException(Exception):
    def __init__(self):
        super(Exception, self).__init__()
        self.args = ("raised myException",)
try:
  raise myException()
except myException as ex:
    print(ex)


