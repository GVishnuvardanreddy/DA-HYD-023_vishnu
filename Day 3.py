
age = int(float(input('Enter the age:')))
print(age)
print(type(age))


name = input("Enter the name:")
print(name)
print(type(name))


marks = int(input("Enter the marks:")).split(
print(marks)

a = input("Enter the valiues:").split(',')
print(a)


#List of intgers
marks= list(map(int,input("Enter the values:").split(',')))
print(marks)

#now we want to accept two users
age,salary=map(int,input("Enter the values:").split(','))
print(age)
print(salary)

#single input--> int(input())
age,salary=map(float,input("Enter the values:").split(','))
print(age,salary)
#arithmetic operations
print(5*3)
print(5/3)#divided
print(5//3)#integer quotient
print(5%3)#remainder
print(5**3)#exponential or 
#find the area=length * breadth

length,breadth =map(int,input("Enter the values:").split(','))
area=length*breadth
print(area)
#assignment operators
a=45
print(a)
a=a+5
print(a)

b=35
b+= a
print(b)

#comparison operators
age = 25
print(age == 25)
print(age != 45)
print(age < 25)
print(age > 55)

#membership operators--> in ,notin
marks=[45,55,98,69]
print( 55 in marks)
print( 66 in marks)
print( 555 not in marks)

#Logical operators
#and--> all conditions to be satisfied
#or --> any one condition to  be satisfied
a= (25 in [65,25,65]) and 45 < 56
print(a)
b= 45>56 or 25<= 45
print(b)
c=not(True)
print(c)
#identity operators--> is and isnot4
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)





















