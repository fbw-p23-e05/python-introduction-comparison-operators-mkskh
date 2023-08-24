big_number = []

for i in range(3):

    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))

    if first != second:
        print('Numbers are not equal')
    else: 
        print('Numbers are equal')

    if first > second:
        print('First number is greater than second number')
    elif first < second:
        print('Second number is greater than first number')
    else:
        None

    if first < second or first == second:
        print('Second number is greater than or equal to first number')
    elif (first > second) or (first == second):
        print('First number is greater than or equal to first number')
    elif first < second or first != second:
        print('Second number is greater than or not equal to first number')
    elif first > second or first != second:
        print('First number is greater than or not equal to first number')
    else:
        None

    if first >= 100 or second >= 100:
        print('At least one of the number is big')
    else:
        print('Both numbers are not big')

    if first >= 100 or second >= 100:
        tempList = []
        tempList = int(first)
        tempList = int(second)     
        big_number.append (tempList)
        print('big_numbers is set to ', first >= 100 or second >= 100)
        print('')
    else:
        print('big_numbers is set to ', first >= 100 or second >= 100)
        print('')





# failed try with while


# while True:
#     first = input('Enter first number (or write "quit" to exit): ')
#     second = input('Enter second number: ')
    
#     if first.isdigit() and second.isdigit():
#         first = int(first)
#         second = int(second)

#         if first != second and first > second and :
#             print('Numbers are not equal')
#             print('Second number is greater than first number')
#         else:
#             print('Numbers are  equal')
#     elif first == 'quit':
#         exit()
#     else:
#         print('Please enter a number or type "quit"!"')

