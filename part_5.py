"""This module decrypts given ciphertext with substitution cipher and a key."""

from part_1 import UPPERCASE_ALPHABET
from part_1 import LOWERCASE_ALPHABET


def part_five(ciphertext, key):
    """Decrypt a given ciphertext with substitution cipher and a key."""
    plaintext = ''

    for i in ciphertext:
        plaintext += part_five_decrypt_char(i, key)

    return plaintext


def part_five_decrypt_char(cipherchar, key):
    """Decrypt a given char using substitution cipher and a key."""
    plainchar = cipherchar

    # if plainchar is in upper-case, use UPPERCASE_ALPHABET to encrypt
    if plainchar.upper() == plainchar and plainchar in UPPERCASE_ALPHABET:
        plain_letter_num = UPPERCASE_ALPHABET.index(plainchar)
        cipherchar = key[plain_letter_num]

    # if plainchar is in lower-case, use LOWERCASE_ALPHABET to encrypt
    if plainchar.lower() == plainchar and plainchar in LOWERCASE_ALPHABET:
        plain_letter_num = LOWERCASE_ALPHABET.index(plainchar)
        cipherchar = key[plain_letter_num]

    return cipherchar
