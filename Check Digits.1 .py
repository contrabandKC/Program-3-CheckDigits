##########################################################################
# CS 101
# Program : 3 Check Digits
# Name Erik Marquez
# Email eemxr9@mail.umkc.edu
# PROBLEM : Check Digits - Take input from a user. Validate and out put
# ALGORITHM :
#   1. Ask user for input
#   2. Validate the input
#   3. Interpret the output
#   4. Repeat
# ERROR HANDLING:
# Any Special Error handling to be noted.
# OTHER COMMENTS:
# Any special comments
###########################################################################


valid_chars = ('1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F')
char_weights = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
first_char = ('A','B','C','D')
second_char = ('A','B','C','D','E')
first_char_table = {'A':'CS101','B':'CS191','C':'CS201','D':'CS291'}
sec_char_table = {'A':'Test','B':'Program','C':'Quiz','D':'Final','E':'Other'}
user_input_list = []

def digits_length (value):
    '''checks if user input  equals 13 digits'''
    check = True
    digit = 0
    for num in value:
        digit += 1
    if digit != 13:
        check = False
    return check

def digit_valadation(value):
    '''checks to see if all digits are valid'''
    check = True
    digit = 0
    false_digit = ''
    for idx in range(2, 13):
        if value[idx] not in valid_chars:
            false_digit = value[idx]
            check = False
            break
    return check,false_digit


def first_digit(value):
    '''checks to see if first digit is valid'''
    check = True
    false_digit = ''
    if value[0] not in first_char:
        check = False
        false_digit  = value[0]
    return check,false_digit

def second_digit(value):
    '''checks to see second digit is valid'''
    check = True
    false_digit = ''
    if value[1] not in second_char:
        check = False
        false_digit  = value[1]
    return check,false_digit


def check_digit(value):
    '''uses the last value as a check digit'''
    digit = False
    add = 0
    for char in range(0,len(value)-1):
        add = add + (char * char_weights[value[char]])
    result = add % 10
    if result == int(value[12]):
        digit = True
    return digit

def digit_meaning(value):
    '''outputs the value/ meaning of the digit'''
    first = first_char_table[value[0]]
    second = sec_char_table[value[1]]
    return first,second

def total_input_list(loclist):
    '''if user has made valid inputs it prints a list of inputs. Else prints nothing entered'''
    if user_input_list == []:
        print('\nNothing has been entered.')
    else:
        print("\nYou have entered:\n")

        for idx in range(0,len(user_input_list)):
            print(user_input_list[idx])



#Main loop

print('Welcome to the assignment')

while True:



    # Validation loop

    while True:

        user_digits = input('\nEnter the assignment number, Z to see inputs, or Q to Quit ==>').upper()

        if user_digits == "Q":
            break

        if user_digits == 'Z':
            total_input_list(user_input_list)
            break

        print()

        # Checks total length of entry
        if digits_length(user_digits) == False:
            print('The value entered was incorrect')
            print('Assignment # must be 13 characters in length\n')
            break
        #Checks first Character of entry
        if first_digit(user_digits)[0]  == False:
            print('The value entered was incorrect')
            print('Incorrect, the first character cannot be {}, only A-D\n'.format(user_digits[0]))
            break

        #Checks second character of entry
        if second_digit(user_digits)[0] == False:
            print('The value entered was incorrect')
            print('Incorrect, the second character cannot be {}, only A-E\n'.format(user_digits[1]))
            break

        #Checks if all characters are Valid
        if digit_valadation(user_digits)[0] == False:
            print('The value entered was incorrect')
            print('Assigment number contains invalid character {} in the value\n'.format(digit_valadation(user_digits)[1]))
            break
        #checks to make sure check digit checks out
        if check_digit(user_digits) == False:
            print('The value entered was incorrect')
            print('The last digit {} is invalid\n'.format(user_digits[12]))
            break

        False

    # Program output

        meaning = digit_meaning(user_digits)

        print('Value given was valid')
        print('Assignment {} is for {}, and is a {}\n'.format(user_digits,meaning[0],meaning[1]))


        user_input_list.append('#{} is Class-{} assignment-{}'.format(user_digits,meaning[0],meaning[1]))

    if user_digits == "Q":
        break

        print(user_input_list)

## closing loop and Thanking the user. Printing the final out put to the user

print("\nThank you for using Check digits!\n")

if user_input_list == []:
    print('')
else:
    total_input_list(user_input_list)