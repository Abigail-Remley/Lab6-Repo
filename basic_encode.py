
# Abigail Remley
# Here is the encode function which takes a string of inputted integers and increments them by three.
# The now "encoded" password is returned.
def encode(raw_password):
    encoded_password = ""
    # Adding functionality for numbers which would be incremented to double digits. -DP
    for i in raw_password:
        i = int(i)
        if i == 7:
            i -= 7
        elif i == 8:
            i -= 7
        elif i == 9:
            i -= 7
        else:
            i += 3
        # ... I got some very weird bugs trying the preceding as a shorter statement...  -DP
        encoded_password = encoded_password + str(i)
        print(encoded_password)
    return encoded_password


# Decoding function which takes an encoded hash and decrements them by three.
# The now "decoded" password is returned.    -DP
def decode(hashed_password):
    decoded_password = ""
    for i in hashed_password:
        i = int(i)
        if i == 0:
            i += 7
        elif i == 1:
            i += 7
        elif i == 2:
            i += 7
        else:
            i -= 3
        decoded_password = decoded_password + str(i)
        print(decoded_password)
    return decoded_password


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
            stored_decoded = decode(stored_encoded)
            print(f'The encoded password is {stored_encoded}, and the original password is {stored_decoded}')
        if input_option == 3:
            loop_var = 1
            break

if __name__ == '__main__':
    main()
