#!/usr/bin/python3

import re

flag = input('Flag: ')

# Add flag format if not included
if not re.match(r'Gateway{[^}]+}', flag):
	flag = f'Gateway{{{flag}}}'

flag = flag.encode()

# XOR each 2 bytes
def xor_round(x):
	x_len = len(x)
	return bytes(x[i] ^ x[(i+1)%x_len] for i in range(x_len))

# Rotate bits to the right inside of each byte
def rotate_bits(x):
	x_len = len(x)
	return bytes((x[i] << 8-(i%8))&0xff | (x[i] >> (i%8)) for i in range(x_len))

# 9 Rounds of hashing power! Uncrackable!
for i in range(9):
	flag = xor_round(flag)
	flag = rotate_bits(flag)

if flag.hex() == 'da44355ee49c42faebe43e1b5088b25b10b383b367e32dccb01699f2df':
	print('Flag is correct!')
else:
	print('Incorrect flag!')