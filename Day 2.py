'''
Tokens --> variables, punctuators

variables --> Named memory location , its a placeholder for data
#rules to be followed
'''
#MultiAssignment of Variables

name,age,place = 'Codegnan',7,'Hyderabad'
print(name, age,place)
print(name, age,place,sep=',')
print(name, age,place,sep='------->')

#a,b = 2,4,5 #Value error as too many to unpack
#Reassigning variables

name = "Codegnan"
a,b = 45,1.5,
print(a,b)
a,b = b,a
print(a,b,sep=',')

#a,b = b,c#name error
#print(a,b)

#deleting the variables --->del
#del a
#print(a)
#del a,b
#print(a,b)

#punctuators ---> [lists], (tuples), [dict,sets]
name = "codegnan" ;age = 7; course = "data_analytics"
print(name,age,course)

#datatypes --> Numeric (int, float, complex),boolean,None
#sequences -->  Lists,Tuples,Sets, Strings,Frozensets,Mapping(dict)

age = 7 
print(age)
print(type(age))

print(type(234))

#quantity=03 it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
price= 750.24; discount = 2.5
print(price,discount)
print(type(price))

#complex --> combination of real and immaginary numbers
i2 = 4
data = 5+i2
print(data)

data = 5+2j #j is imp representation
print(data)
print(type(data))

#boolean -->true or false

valid = True
print(type(valid))

error=False
print(type(error))

#Typecasting -> Converting one type to another type
#python by default it follows Implicit type  (we need mot mention the datatype)

int,float,complex,bool

age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d=bool(age)
print(d)
e= bool(0)
print(e)

#float

age = 35.5
print(type(age))
b = int(age)
print(b)
c = complex(age)
print(c)
d=bool(age)
print(d)
e= bool(0)
print(e)

data = 2+5j
print(type(data))
d= bool(data)
print(d)
print(type(data))
e= float(True)
print(e)











