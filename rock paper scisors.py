import random

print('''print
        rock
        paper or
        scisors ''')

r = 'rock'
p = ' paper'
s= 'scisors'

c = [r,p,s]

while True:

    i = input('enter : ')
    com = random.choice(c)
    
    
    
    if i == 'rock':
        print(com)
        if com == p:
            print('you loose')

        elif com == r:
            print('draw')
            
        elif com == s:
            print('you win')

    elif i == 'paper':
        print(com)
        if com == s:
            print('you loose')

        elif com == p:
            print('draw')
            
        elif com == r:
            print('you win')

    elif i == 'scisors':
        print(com)
        if com == r:
            print('you loose')

        elif com == s:
            print('draw')
            
        elif com == p:
            print('you win')

    
