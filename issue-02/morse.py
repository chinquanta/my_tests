"""Morse Code Translator"""
import pytest


LETTER_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
}

MORSE_TO_LETTER = {morse: letter for letter, morse in LETTER_TO_MORSE.items()}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]
    return " ".join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    >>> decode('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- \
                .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- \
                ...-- ....- ..... -.... --... ---.. ----. ----- --..-- .-.-.- \
                ..--.. -..-. -....- -.--. -.--.-')
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.?/-()'
    """
    decoded_letters = [MORSE_TO_LETTER[let] for let in morse_message.split()]
    return ''.join(decoded_letters)


@pytest.mark.parametrize('s,exp',
                         [('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'),
                          ('-..', 'D'), ('.', 'E'), ('..-.', 'F'),
                          ('--.', 'G'), ('....', 'H'), ('..', 'I'),
                          ('.---', 'J'), ('-.-', 'K'), ('.-..', 'L'),
                          ('--', 'M'), ('-.', 'N'), ('---', 'O'),
                          ('.--.', 'P'), ('--.-', 'Q'), ('.-.', 'R'),
                          ('...', 'S'), ('-', 'T'), ('..-', 'U'),
                          ('...-', 'V'), ('.--', 'W'), ('-..-', 'X'),
                          ('-.--', 'Y'), ('--..', 'Z'), ('.----', '1'),
                          ('..---', '2'), ('...--', '3'), ('....-', '4'),
                          ('.....', '5'), ('-....', '6'), ('--...', '7'),
                          ('---..', '8'), ('----.', '9'), ('-----', '0'),
                          ('--..--', ','), ('.-.-.-', '.'), ('..--..', '?'),
                          ('-..-.', '/'), ('-....-', '-'), ('-.--.', '('),
                          ('-.--.-', ')'), (' ', '')])
def test_parameters(s, exp):
    assert decode(s) == exp


@pytest.mark.parametrize('s,exp',
                         [('.-.-.-.-.-.-', pytest.raises(KeyError)),
                          ('#@!~', pytest.raises(KeyError)),
                          (10, pytest.raises(AttributeError)),
                          (['.-'], pytest.raises(AttributeError)),
                          (type, pytest.raises(AttributeError))])
def test_raises(s, exp):
    with exp:
        assert decode(s) == exp


if __name__ == '__main__':
    msg = '-- .- .. -....- .--. -.-- - .... --- '\
          '-. -....- ..--- ----- .---- ----.'
    decoded_msg = decode(msg)
    print(decoded_msg)
    assert msg == encode(decoded_msg)
