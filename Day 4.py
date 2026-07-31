'''
a = [1,3,5,6]
b= a
print(id(a))
print(id(b))
c= [1,3,5,6]#List (Mutable collections) ,ids are diff
print(id(c))
print(c is a)#output false
print(c==a)#output True
print(a is not c)
#Bitwise operators--> we perform bitwise operators over operands &(and),|(or),^(xor),shifting operators(<<,>>
print(5&3) #converted to bit-wise operators
print(5|3)#Bit-wise or
print(5^3)#Bit-wise XOR
print(5 and 3)#Returns only first digit
print(5 or 3)#Returns second digit

print(5<1)#false comparison
print(5<<1)#left shift by 1 position in binary 5(0101-->1010)_10(o/p)
print(5>>1)#Right shift by 1 position in binary5(0101-->0010)_2(o/p)
print(15<<2)#convert 15 to binary and perform 2 times left shifting
print(15>>2)

names = input("enter the name:").split(',')
print(names)

name1,name2 =map(str,input("enter the name:").split(','))
print(name1,name2 )


#conditional statements-->if usage

#age = 15
age=int(input("Enter the age:"))
if age>=18:
    print("Your age is:",age)

#age = 15
age=int(input("Enter the age:"))
if age>=18 and age in [21,19,20]:
    print("Your age is:",age)
print(age)
#ex: voter eligibility
age= int(input("enter the age:"))
if age >18:
    print("you are eligible",age)
    print("Access Granted")
else:
    age = 18-age
    #print("You are ineligible,as ur age is:",age,"years")
    print("You need to wait for more",age,"years")'''

#nested if
if age >0:
    if age >=18:
        print("you are eligible",age)
        print("Access Granted")
    else:
        age = 18-age
        #print("You are ineligible,as ur age is:",age,"years")
        print("You need to wait for more",age,"years")
else:
    print("You have entered -ve values")















