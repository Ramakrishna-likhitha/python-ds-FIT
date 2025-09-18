# class sample():
#     a=10
# print(a)
#............................................
# class demp:
#     def demo1():
#         a=10
#         print(a)
#     demo1()
# class myclass():
#     a=5  
# p1=myclass()   
# print(p1.a)
#.......................................................................
# class myclass():
#     a=(name,id)
# p1=myclass()
# print(p1.name)
# print(p1.id)
#.....................................................................
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1=student('likhitha',20)
# p2=student('hema',21)
# print(p1.name,p1.age)
# print(p2.name,p2.age)
#................................................................................
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def results(self):
#         print(self.name,self.age)
# p1=student('likhitha',20)
# p2=student('hema',21)
# p1.results()
# p2.results()
# #...............................................................................................
# class car():
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def display(self):
#         print(self.name,self.color)
# p1=car('bmw','wight')
# p2=car('kia','red')
# p3=car('bench','brown')
# p1.display()
# p2.display()
# p3.display()         
# #---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class calculator:
#     def add(self, a ,b):
#         return (a+b)

# p1=calculator(12,34)
# p1.add()
#..................................................................................
# class car:
#     def __init__(self , name,brand):
#         self.name=name
#         self.brand=brand
#     # def display(self):
#     def __str__(self):
#         return f"carname :{self.name} car brand: {self.brand}" #inside the __str__ me use the return not print
# c1=car("tesla","model s")
# print(c1)



#....................................................................................................
# class Car:
#     def __init__(self, name, brand):
#         self.name = name
#         self.brand = brand

#     # def __str__(self):
#     #     return f"Car Name: {self.name}, Brand: {self.brand}"......................................method method is just a function inside a class that works with the object’s data.
# #t always has self as the first parameter.

# c1 = Car("Tesla", "Model S")
# print("name:",c1.name ,"rand",c1.brand)

# class calculator:
#     def add(self, a ,b):
#         return a+b
#     def sub(self , a, b):
#         return a-b
# p1=calculator()
# print(p1.add(10,20))
# #..............................normal method...............................
# class radha:
#             def __init__(self,name,age):
#                   self.name=name  #self.variable=parameter
#                   self.age=age
#             def display(self): #..........method must have self			  
#                 return f"name: {self.name} , age:{self.age}"	
# onj1=radha('likhitha',23)
# print(onj1.display())	
# #.........................................................specila method................................................abs
# class radhe :
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def __str__(self):
#         return f"name: {self.name} id: {self.id}"
# obj1=radhe('likhitha',12)
# print(obj1)
# #...............................modifing object after creation......................
# class student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
# p1=student('likhitha',12)
# p1.id=13
# print(p1.name,p1.id)
#.................................
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)S
class child(parent):
    pass
c1=child('likhitha',12)
