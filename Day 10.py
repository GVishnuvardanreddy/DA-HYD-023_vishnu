#To calculate the performance of the player to calculate the total score and number of boundries and dots.
'''
score=list(map(int,input().split()))
boundries=0
dot=0
runs=0
for i in score:
    runs=runs+i
#print(runs)     # her it calculate the total score of the player\

    if i == 4 or i == 6:
        boundries=boundries+1  # number of boundries calculate
        #print(boundries)
    elif i == 0:
        dot=dot+1     #number of dot
    #print(dot) 
print('boundries',boundries)
print('dot',dot)
print('runs',runs)
'''
#To ulock the phone by using password with only 3 max attempts
'''
pin='1255'
attempt = 3
count= 0
while count < attempt:
    entered_pin=input('enter the pin')
    if entered_pin == pin:
        print('unlock')
        break
    else:
        print('wrong pin')
        count=count+1
print('phone locked')

'''
#movies:
movies=input().split()
i=1
for movie in movies:
    print(i,movie)
    i=i+1
'''
# Python program to calculate a batsman's innings
total_score = 0
boundaries = 0
dot_balls = 0
balls = int(input("Enter the number of balls faced: "))
for i in range(1, balls + 1):
    runs = int(input(f"Enter runs scored on ball {i}: "))
    total_score += runs
    if runs == 0:
        dot_balls += 1
    if runs == 4 or runs == 6:
        boundaries += 1
print("\n----- Innings Summary -----")
print("Balls Faced :", balls)
print("Total Score :", total_score)
print("Boundaries  :", boundaries)
print("Dot Balls   :", dot_balls)
'''
'''
pin = "1234"
max_attempts = 5
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("enter the phoe lock:")
    if entered_pin == pin:
        print("login sucessful")
        break
    print("entered PIN is wrong..try again correctly")
    current_attempt +=1
else:
    print("account locked")
'''
pin = "0967"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("enter the ATM pin: ")
    if entered_pin == pin:
        print("login sucessful")
        break
    print("entered PIN is wrong..try again correctly")
    current_attempt +=1
else:
    print("account locked,try after 24 hours...")
































    
