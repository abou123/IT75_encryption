"""This module decrypts given ciphertext with substitution cipher and a key."""

LOWERCASE_ALPHABET = 'abcdefghijklmnopqrstuvwxyz '
UPPERCASE_ALPHABET = ''
for i in LOWERCASE_ALPHABET:
    UPPERCASE_ALPHABET += i.upper()


def part_five(ciphertext, key):
    """Decrypt a given ciphertext with substitution cipher and a key."""
    plaintext = ''

    for i in ciphertext:
        plaintext += part_five_decrypt_char(i, key)

    return plaintext


def part_five_decrypt_char(cipherchar, key):
    """Decrypt a given char using substitution cipher and a key."""
    plainchar = cipherchar

    # if cipherchar is in upper-case, use UPPERCASE_ALPHABET to decrypt
    if cipherchar.upper() == cipherchar and cipherchar in UPPERCASE_ALPHABET:
        cipher_letter_num = key.index(cipherchar)
        plainchar = UPPERCASE_ALPHABET[cipher_letter_num]

    # if cipherchar is in lower-case, use LOWERCASE_ALPHABET to decrypt
    if cipherchar.lower() == cipherchar and cipherchar in LOWERCASE_ALPHABET:
        cipher_letter_num = key.index(cipherchar)
        plainchar = LOWERCASE_ALPHABET[cipher_letter_num]

    return plainchar


# teacher provided ciphertext that doesn't decrypt
# TEST_CIPHERTEXT = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'
# TEST_KEY = 'mwgp bdzxrylacsokjfhtnueivq'
# encrypted result from previous part
# TEST_CIPHERTEXT = 'od hxobh msp hxrkh msp hbmarsz emi od gmwwmzbh msp lrszh'
# TEST_KEY = 'mwgpbdzxrylacsokjfhtnueivq'
# print(part_five(TEST_CIPHERTEXT, TEST_KEY))
