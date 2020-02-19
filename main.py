# 1. create two int variables and compare them using if keyword 
# 2. using and keyword - test if var1 > var 2 and var1 > var3



# 1. create two int variables and compare them using if keyword 
var1 = input('enter first number:')
var2 = input('enter second number:')

if var1 > var2:
    print('First number is greater.')
    print('--------------******--------------\n')

elif var2 > var1:
    print('Second number is greater.')
    print('--------------******--------------\n')

else: print('They are equal!')


# 2. using and keyword - test if var1 > var 2 and var1 > var3
var3 = input('enter the thrid number:')
if var1 > var2 and var1 > var3:
    print('First number is greater than both numbers!')
    print('--------------******--------------\n')


else: 
    print('First number is not greater than other numbers!')
    print('--------------******--------------\n')
