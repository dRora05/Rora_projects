import random

num = ("1234567890")

for i in range(10):
    print('.')
    
p = (random.choice(num))
print(p)

for i in range(40):
    print('.')

while True:
    c = input('Enter your guessing : ')
    if c > p:
        print('guess is greater than number')

    elif c < p:
        print('guess is lower than number')

    else:
        print('correct')
        print('thank you for playing')
        exit()
        
