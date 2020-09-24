import string


def solution(s):
    alphabet_list = list(string.ascii_lowercase)
    alphabet_list.append(' ')
    braille_list = ["100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110", "101000", "111000", "101100",
                    "101110", "101010", "111100", "111110", "111010", "011100", "011110", "101001", "111001", "010111", "101101", "101111", "101011", "000000"]
    braille_alphabet = dict(zip(alphabet_list, braille_list))
    cap_str = "000001"
    output = ""
    for letter in s:
        try:
            output += braille_alphabet[letter]
        except KeyError as err:
            output += cap_str
            output += braille_alphabet[letter.lower()]
    return output


if __name__ == "__main__":
    print(solution(input("Enter a word to be translated to braille: ")))
