#!/usr/bin/python3

import re

def read_words(file):
    with open(file, 'r') as palabras:
        content = palabras.read().splitlines()
    return content

def write_passwords(filename, passwords):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def generate_passwords(words):
    passwords = set()

    for word in words:
        word_lower = word.lower()
        word_upper = word.upper()
        word_capitalized = word.capitalize()

        word_numbered = re.sub(r'o', '0', word_lower)
        word_numbered = re.sub(r'i', '1', word_numbered)
        word_numbered = re.sub(r'e', '3', word_numbered)
        word_numbered = re.sub(r'a', '4', word_numbered)

        word_num_to_letter = re.sub(r'0', 'o', word_numbered)
        word_num_to_letter = re.sub(r'1', 'i', word_num_to_letter)
        word_num_to_letter = re.sub(r'3', 'e', word_num_to_letter)
        word_num_to_letter = re.sub(r'4', 'a', word_num_to_letter)

        symbols = ['@', '#', '$', '%', '&']
        for symbol in symbols:
            passwords.add(word_lower + symbol)
            passwords.add(word_upper + symbol)
            passwords.add(word_capitalized + symbol)
            passwords.add(word_lower + symbol + '123')
            passwords.add(word_upper + symbol + '123')
            passwords.add(word_capitalized + symbol + '123')

        passwords.add(word_lower + '2024')
        passwords.add(word_upper + '2024')
        passwords.add(word_capitalized + '2024')
        passwords.add(word_numbered + '2024')
        passwords.add(word_num_to_letter + '2024')

    return list(passwords)

def main(input_filename, output_filename):
    words = read_words(input_filename)
    passwords = generate_passwords(words)
    write_passwords(output_filename, passwords)
    print(f'Las contraseñas se han generado y guardado en {output_filename}')

if __name__ == '__main__':
    input_filename = 'palabras.txt' 
    output_filename = 'contraseñas.txt'  
    main(input_filename, output_filename)

