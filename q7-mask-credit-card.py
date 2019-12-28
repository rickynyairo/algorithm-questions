'''Solution to Q7'''


def mask(card_number):
    char_list = list(card_number)
    # loop through character list
    # replace appropriate characters with #
    position_from_last = len(char_list) - 4
    for i, char in enumerate(char_list):
        # do not replace letters
        try:
            # non-numbers will throw a value error
            int(char)
            if not (i < 4 or i - position_from_last >= 0):
                char_list[i] = '#'
        except ValueError:
            continue
    return ''.join(char_list)

def main():
    card_numbers = [
        '4556364607935616',
        '4556-3646-0793-5616',
        '64607935616',
        'ABCD-EFGH-IJKLM-NOPQ',
        '',
        'Skippy'
    ]
    masked_numbers = [ mask(card) for card in card_numbers ]
    print('Masked card numbers => \n', masked_numbers)

if __name__ == "__main__":
    main()