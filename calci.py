# let us build a calculater hurray!!!....

first= input('enter first number: ')
operater= input('choose operater (+,-,*,/,%): ')
second= input('enter second number: ')    

first=int(first)
second= int(second)

if operater== '+':
    print(first + second)
elif operater== '-':
    print(first - second)
elif operater== '*':
    print(first * second)
    
elif operater== '/':
    print(first / second)
elif operater== '%':
    print(first % second)

else:
    print('invalid choice')    

