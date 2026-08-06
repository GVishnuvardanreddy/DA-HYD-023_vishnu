'''#cart value or add sum of numbers
products = list(map(int,input("enter").split(',')))
total = 0
for i in products:
    total= total +i
print(total)
'''
'''
password = input()
upper = lower = digit = special=0
for ch in password:
    if 'A'<= ch<='Z':
        upper+=1
    elif 'a'<=ch <='z':
        lower+=1
    elif '0'<= ch <='9':
        digit+=1
    else:
        special+=1
print("upper",upper)
print("lower",lower)
print("digit",digit)
print("special",special)
'''
'''
email=input().split()
for mail in email:
    print(mail.split("@")[1])
'''























































































































