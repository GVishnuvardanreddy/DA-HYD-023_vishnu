#Grade Checker
'''
marks = int(input('Enter marks:'))

if marks <0 or marks >100:
   print('Invalid marks enetred')
                  
elif marks >=90:
    print('Grade:A')
    print('Remark:Outstanding!')
elif marks >=80:
     print('Grade:B')
     print('Remark:Excellent')

elif marks >=70:
     print('Grade:C')
     print('Remark:Good')

elif marks >=60:
     print('Grade:D')
     print('Remark:Fair,need improvement')

elif marks >=50:
     print('Grade:E')
     print('Remark:Poor,needs serious improvement')

else:
    marks <50
    print('Grade:F')
    print('Remark:Failed,needs to reappear')
'''
#Even-Odd Checker
'''
num = int(input('Enter a number:'))
if num == 0:
    print('Zero is neither even nor odd')

elif num%2 == 0:
    print('Even Number')

elif num%2 == 1:
     print('Odd Number')

elif num<0 and num%2 == 1:
    print('Negative Odd Number')

else:
    print('Negative Even Number')
'''
#Season Identifier

month = int(input('Enter the month number:'))
if month <1 or month>12:
    print('Invalid month entered')

elif month ==12 or month ==1 or month ==2:
     print('Season:Winter')

elif month ==3 or month ==4 or month ==5:
     print('Season:Spring')
     
elif month ==6 or month ==7 or month ==8:
    print('Season:Summer')
    
else:
    print('Season:Autumn')










    

    
      
                  
