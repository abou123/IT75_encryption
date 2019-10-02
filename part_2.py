"""this module encrypts using a substitution cipher."""


UPPERCASE_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z']
# create a lower-case alphabet from uppercase_alphabet
LOWERCASE_ALPHABET = [letter.lower() for letter in UPPERCASE_ALPHABET]


def part_two(plaintext, shift_amount):
    """Encrypt a string with shift cipher and a given shift amount."""
    ciphertext = ""
    for i in plaintext:
        ciphertext += part_two_encrypt_char(i, shift_amount)

    return ciphertext


def part_two_encrypt_char(plainchar, shift):
    """Encrypt a char with shift cipher and a given shift amount."""
    # if the character is in upper-case then use UPPERCASE_ALPHABET to encrypt
    if plainchar.upper() == plainchar:
        letter_num = UPPERCASE_ALPHABET.index(plainchar)
        return UPPERCASE_ALPHABET[(letter_num+shift) % len(UPPERCASE_ALPHABET)]

    # if the character is in lower-case then use LOWERCASE_ALPHABET to encrypt
    if plainchar.lower() == plainchar:
        letter_num = LOWERCASE_ALPHABET.index(plainchar)
        return LOWERCASE_ALPHABET[(letter_num+shift) % len(LOWERCASE_ALPHABET)]


print(part_two('thequickbrownfoxjumpsoverthelazydog', 13))
