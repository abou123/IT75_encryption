"""Handle key tranformation for 7 character key substitution cipher."""


def create_key(long_key):
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
    long_key = remove_duplicates(long_key)
    return long_key


def remove_duplicates(string):
    """Remove duplicate symbols from a string."""
    for i in string:
        if string.count(i) > 1:
            index = string.index(i)
            string = string[0:index:] + string[index+1::]

    return string


key = 'aaahaaaaho'
print(create_key(key))
