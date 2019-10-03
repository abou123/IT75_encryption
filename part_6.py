"""This encrypts or decrypts input using a given key & substitution cipher."""

from part_4 import part_four
from part_5 import part_five


def part_six():
    encrypt_or_decrypt = 'a'
    while (encrypt_or_decrypt[0] != 'e' and encrypt_or_decrypt[0] != 'E'
            and encrypt_or_decrypt[0] != 'd' and encrypt_or_decrypt[0] != 'D'):

        print('Do you want to encrypt or decrypt?')
        encrypt_or_decrypt = input('> ')

    print('Enter a substitution cipher key:')
    key = input('> ')

    print('Enter the text to encrypt/decrypt')
    text = input('> ')

    if encrypt_or_decrypt[0] == 'e' or encrypt_or_decrypt == 'E':
        return part_four(text, key)

    elif encrypt_or_decrypt[0] == 'd' or encrypt_or_decrypt[0] == 'D':
        return part_five(text, key)

print(part_six())
