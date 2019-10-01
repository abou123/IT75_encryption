uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z']
# create a lower-case alphabet from uppercase_alphabet
lowercase_alphabet = [letter.lower() for letter in uppercase_alphabet]


def part_one(ciphertext, shift_amount, hint=None):
    # shift_amount can either be the actual shift amount or the first part of
    # the hint; if it's the first part of the hint (i.e. hint is the other part
    # of the hint), then calculate the actual shift amount from the difference
    # between the second and first and second parts of the hint
    if hint:
        shift_amount = ord(hint) - ord(shift_amount)
    plaintext = ""

    for i in range(len(ciphertext)):
        # if the current character is upper-case
        plaintext += part_one_decode_char(ciphertext[i], shift_amount)

    return plaintext


def part_one_decode_char(cipherchar, shift):
    # if the letter is upper-case then use uppercase_alphabet for decryption
    if cipherchar.upper() == cipherchar:
        letter_num = uppercase_alphabet.index(cipherchar)
        return uppercase_alphabet[(letter_num+shift) % len(uppercase_alphabet)]

    # if the letter is lower-case then use lowercase_alphabet for decryption
    if cipherchar.lower() == cipherchar:
        letter_num = lowercase_alphabet.index(cipherchar)
        return lowercase_alphabet[(letter_num+shift) % len(lowercase_alphabet)]


print(part_one('BKFTAZDAOWE', 'a', 'o'))
