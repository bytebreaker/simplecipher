#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Caesar Cipher http://goo.gl/23MVS
# adopted from code by Al Sweigart http://goo.gl/Of5DSb
# abe@3vilgenius.com

import os

#Assume that we don't want to shift characters more than 26 places (based on standard English character set)
MAX_KEY_SIZE = 26

plain_text = "Allow myself to introduce, myself.  (Austin Powers)"

def translate(mode, message, key):
    """
    This function accepts a mode ('e' for encrypt, 'd' for decrypt)
    a message (the plain text to encrypt, or the cipher text to decrypt)
    and a key (an integer value between 1 and 26 that is used for the character substitution shift).
    Have fun!
    """
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

def translate_file(mode, input_filename, key, output_filename='converted_text.txt'):
    """
    This function translates all of the contents of a file from one encoding to a shifted Caesar Cipher encoding.
    mode ('e' for encrypt, 'd' for decrypt)
    input_filename (the file used as an input)
    key (an integer value between 1 and 26 that is used for the character substitution shift).
    output_filename (the file that stores the converted text).
    WARNING: Don't use this if you are up against the National Security Agency.
    """
    print 'Translating file(%s) to file(%s)' %(input_filename,output_filename)
    fout = open(output_filename,'w')
    output_text = []
    for line in open(input_filename):
        line = line.strip()
        translated_line = translate(mode,line,key)
        fout.write(translated_line+'\n')
        output_text.append(translated_line)
    final_output = '\n'.join(output_text)
    print 'All done converting text.\n'
    if len(final_output) > 2000:
        final_output = final_output[:2000]
    print 'Converted text looks like:'
    print final_output

def try_file_translate():
    if os.path.exists('quotes.txt'):
        #turn a file of quotes into a substitution cipher encrypted file named 'quotes_encrypted.txt'
        translate_file('e', 'quotes.txt',24, output_filename='quotes_encrypted.txt')
    if os.path.exists('quotes_encrypted.txt'):
        #if the file 'quotes_encrypted.txt' exists, then read it and convert it to plain text named 'quotes_decrypted.txt'
        translate_file('d', 'quotes_encrypted.txt',24, output_filename='quotes_decrypted.txt')


def main():
    cipher_text = translate('e',plain_text, 24)
    decrypted_text = translate('d',cipher_text,24)
    print 'original: %s' % (plain_text)
    print
    print 'cipher: %s' % str(cipher_text)
    print
    print 'decrypted: %s' % str(decrypted_text)
    print 
    try_file_translate()


if __name__ == '__main__':
    main()