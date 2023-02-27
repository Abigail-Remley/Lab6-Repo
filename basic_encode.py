
# Abigail Remley
# Here is the encode function which takes a string of inputted integers and increments them by three.
# The now "encoded" password is returned.
def encode(raw_password):
    encoded_password = ""
    for i in raw_password:
        i = int(i)
        i += 3
        encoded_password = encoded_password + str(i)
    return encoded_password


# Here is the main function, containing the main body and loop of the program.
def main():
# Here are all the variables utilized throughout the main function.
    input_option = 0
    stored_original = ""
    stored_encoded = ""
    loop_var = 0

# Here is the main loop of the program: printing a menu, taking input, and printing the result.
    while loop_var == 0:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        input_option = int(input('Please enter an option: '))
        if input_option == 1:
            stored_original = input('Please enter your password to encode: ')
            stored_encoded = encode(stored_original)
            print('Your password has been encoded and stored! \n')
        if input_option == 2:
# This part I have left intentionally unfinished.
            print('Run the decode function.')
        if input_option == 3:
            loop_var = 1
            break

if __name__ == '__main__':
    main()