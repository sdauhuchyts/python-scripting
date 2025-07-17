#!/usr/bin/env python3

def ceasar(line, shift):
    coded = ''
    for ch in line:
        if not ch.isalpha():
            coded += ch
        else:
            if ch.isupper():
                if (ord(ch) + shift) > ord('Z'):
                    coded += chr(ord(ch) + shift - ord('Z') + ord('A') - 1)
                else:
                    coded += chr(ord(ch) + shift)
            else:
                if (ord(ch) + shift) > ord('z'):
                    coded += chr(ord(ch) + shift - ord('z') + ord('a') - 1)
                else:
                    coded += chr(ord(ch) + shift)
    return coded

input_line = input("Please, enter your line: ")

while True:
    try:
        input_shift = int(input("Please, enter your shift: "))
        if input_shift not in range(1, 26):
            print("Please, enter value in range 1 to 25")
        else:
            break
    except ValueError:
        print("Non-numeric value")
    except:
        print("Something went wrong")

print(ceasar(input_line, input_shift))
