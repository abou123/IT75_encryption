"""This module encrypts given plaintext using substitution cipher and a key."""

from part_1 import UPPERCASE_ALPHABET
from part_1 import LOWERCASE_ALPHABET


def part_four(plaintext, key):
    """Encrypt a given string using substitution cipher and a given key."""
    ciphertext = ""

    for i in plaintext:
        ciphertext += part_four_encrypt_char(i, key)

    return ciphertext


def part_four_encrypt_char(plainchar, key):
    """Encrypt a given char using substitution cipher and a given key."""
    cipherchar = plainchar

    # if plainchar is in upper-case, use UPPERCASE_ALPHABET to encrypt
    if plainchar.upper() == plainchar and plainchar in UPPERCASE_ALPHABET:
        plain_letter_num = UPPERCASE_ALPHABET.index(plainchar)
        cipherchar = key[plain_letter_num]

    # if plainchar is in lower-case, use LOWERCASE_ALPHABET to encrypt
    if plainchar.lower() == plainchar and plainchar in LOWERCASE_ALPHABET:
        plain_letter_num = LOWERCASE_ALPHABET.index(plainchar)
        cipherchar = key[plain_letter_num]

    return cipherchar


# SAMPLE_KEY = 'mwgpbdzxrylacsokjfhtnueivq'
# SAMPLE_PLAINTEXT = 'of shoes and ships and sealing wax of cabbages and kings'
# print(part_four(SAMPLE_PLAINTEXT, SAMPLE_KEY))
