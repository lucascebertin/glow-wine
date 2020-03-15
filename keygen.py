#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

maxChars = 3
keyStart = '1@'
asciiSum=0x12c
letters=b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateKey():
    key = ''
    asciiCount = 0x0

    for keyLetter in range(maxChars):
        randomKey = letters[random.randrange(0, len(letters))]
        asciiCount = asciiCount + randomKey
        key = key + chr(randomKey)

    return asciiCount, key

def main():
    count = 0
    someKey = ''

    while(count != asciiSum):
        count, someKey = generateKey()

    finalKey = keyStart + someKey
    print(finalKey)

main()
