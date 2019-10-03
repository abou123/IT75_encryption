"""this module decrypts a substitution cipher."""

UPPERCASE_ALPHABET = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
# create a lower-case alphabet from uppercase_alphabet
LOWERCASE_ALPHABET = [letter.lower() for letter in UPPERCASE_ALPHABET]


def part_one(ciphertext, shift_amount, hint=None):
    """
    Decrypts a given ciphertext encrypted with a substitution cipher.

    Takes in the ciphertext and either the actual shift amount or one letter
    and its shifted counterpart (the shifted character should be farther in the
    alphabet than the unshifted character).  This function does not support
    having numbers in the ciphertext.
    """
    if hint:
        shift_amount = ord(hint) - ord(shift_amount)
    plaintext = ""

    # for i in range(len(ciphertext)):
    #     # if the current character is upper-case
    #     plaintext += part_one_decode_char(ciphertext[i], shift_amount)

    for i in ciphertext:
        # if the current character is upper-case
        plaintext += part_one_decode_char(i, shift_amount)

    return plaintext


def part_one_decode_char(cipherchar, shift):
    """
    Decrypts a single character encrypted with a shift cipher.

    This function takes in the character and the amount the character has been
    shifted by.
    """
    # if the letter is upper-case then use uppercase_alphabet for decryption
    if cipherchar.upper() == cipherchar:
        letter_num = UPPERCASE_ALPHABET.index(cipherchar)
        return UPPERCASE_ALPHABET[(letter_num+shift) % len(UPPERCASE_ALPHABET)]

    # if the letter is lower-case then use lowercase_alphabet for decryption
    letter_num = LOWERCASE_ALPHABET.index(cipherchar)
    return LOWERCASE_ALPHABET[(letter_num+shift) % len(LOWERCASE_ALPHABET)]


# print(part_one('BKFTAZDAOWE', 'a', 'o'))
