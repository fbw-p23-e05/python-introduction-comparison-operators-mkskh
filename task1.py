

for i in range(3):

    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))

    if first != second:
        print('Numbers are not equal')
    else: 
        print('Numbers are equal')

    if first > second:
        print('First number is greater than first number')
    elif first < second:
        print('Second number is greater than first number')
    else:
         print('-')

    if first >= 100 or second >= 100:
        print('One of the number is big')
        print('')
    else:
        print('The numbers is not big')
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

