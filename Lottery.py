# guess a number from 1 to 20
# and user gets only 4 chances to guess the coreect no
# let the correct no is n=12
#Now lets play!!!
for i in range(5):
    if (i==4):
        print('Game over!')
        break
        
    n=int(input("guses no:"))

    if (n==12):
         print('you win')
         break
    elif (n<12 and n>6):
         print('opss your number is  little bit smaller')
    elif (n>12 and n<=16):
         print('opss your number  little bit bigger')
    elif (n>16 and n<21):
        print('your number is so big')
    elif (n<=6 and n>0):
        print('your number is too small')
    else:
        print('your number is out of range!')

    


