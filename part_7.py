"""Handle key tranformation for 7 character key substitution cipher."""

from part_1 import LOWERCASE_ALPHABET
from part_3 import print_list


def create_key(password):
    """Create a short substituion cipher key.

    The process is as follows:

    1. Remove any duplicate letters from the password.
    2. Split the alphabet into two halves The letters up to and including the
    last letter in the password and the rest of the alphabet.
    3. Remove any letters in your password from the two halves of the alphabet.
    4. The key is the concatenation of the password (without duplicate letters)
    followed by the second part of the split alphabet followed by the first
    part of the alphabet.
    """
    # Step 1
    short_key = remove_duplicates(password)

    # Step 2
    pre_key, post_key = split_alphabet(LOWERCASE_ALPHABET, short_key)

    # Step 3
    pre_key = remove_password_chars_from_alphabet(password, pre_key)
    post_key = remove_password_chars_from_alphabet(password, post_key)

    # Step 4
    long_key = join_key(password, post_key, pre_key)

    return long_key


def remove_duplicates(string):
    """Remove duplicate symbols from a string."""
    for i in string:
        if string.count(i) > 1:
            index = string.index(i)
            string = string[0:index:] + string[index+1::]
    return string


def split_alphabet(alphabet, key):
    """Split alphabet into 2 halves, up to key and after last letter in key."""
    last_char_in_key = key[len(key)-1]
    pre_key = alphabet[0:alphabet.index(last_char_in_key):]
    post_key = alphabet[alphabet.index(last_char_in_key)+1::]
    return pre_key, post_key


def remove_password_chars_from_alphabet(password, mini_alphabet):
    """Remove letters in password from mini_alphabet."""
    for i in password:
        if i in mini_alphabet:
            mini_alphabet = str(mini_alphabet).replace(i, '')
    return mini_alphabet


def join_key(pw, post, pre):
    """Join the parts of the key together."""
    return pw + post + pre


# key = 'aaahaaaahoc'
# print_list(create_key(key))
