num = int(input('Enter a number: '))
#modulate the check value to use the divisible by functionality of this code or comment out to use one of the other functions
check = int(input('Give me a number to divide it by: '))

#simple check using the modulus notation
#mod = num % 2
#if mod > 0:
    #print('Your number is odd!')
#else:
    #print('Your number is even!')
    
#more complex conditionals for odds and evens and including multiples of 4 as a condition (need to make line 14 an elif line for the multiple function to work)
#if num % 4 == 0:
    #print(num, 'is a multiple of 4.')
#if num % 2 == 0:
    #print(num, 'is an even number!')
#else:
    #print(num, 'is an odd number!')
    
#checking if a number entered is divisible by a given number
if num % check == 0:
    print(num, 'is divisible by', check)
else:
    print(num, 'is not divisible by', check)