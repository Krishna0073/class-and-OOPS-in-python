#define a class Student
class Student:
        def __group(self,__group="ECE"):
		if __group is not None:
			self.__group = __group
		else:
			self.__group=__group
	#define two private variables __group, __report with default values
	def __report(self,__report="fail"):
		if __report is not None:
			self.__report = __report
		else:
			self.__report=__report
	#define the __init__ method
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	#define the setDetails method with the two private variables
	def setDetails(self,__group,__report):
		self.__group=group
		self.__group=group
	#define the getDetails method
	def getDetails(self):
		print(self.name)
		print(self.age)
		print(self.__group)
		print(self.__report)

#take the inputs from the user
name = input("name: ")
age = int(input("age: "))
group = input("group: ")
report = input()

print("Student Report Card")
#create an instance s1 of Student with name and age as arguments
s1 = Student()
s1.getDetails(name,age,group,report)
#call the setDetails method with group and report as arguments


#call the getdetails method with s1 object

