"""Brute forces all iterations of Caesar cipher on a ciphertext."""

import part_1


def part_three(ciphertext):
    """Attempt all keys of the Caesar cipher on ciphertext."""
    plaintext_possibilities = []

    for i in range(1, len(part_1.UPPERCASE_ALPHABET)):
        plaintext_possibilities.append(str(i) + ":  "
                                       + part_1.part_one(ciphertext, i))

    return plaintext_possibilities


def print_list(param_list):
    """Print all items of a list on separate lines."""
    for i in param_list:
        print(i)


# print_list(part_three('dzeevjfkrlezkvuwffksrcctcls'))
