# Number Converter

## Overview
This is a project to convert numbers. According with the input the number will be converted.

Numbers types => Decimal Binary Octal Hexadecimal

## The Project
The input should be checked and recognized before the convertion. If there is a invalid value, it should be removed from the input. Some inputs can be two types of numbers for example octal and decimal, in this case both numbers should be recognized and converted. A binary number that begin with '0' will be only a binary number.

## Conversion

### Decimal to binary 
Divide the value by 2 and write out the remainder aside. Repeat this step while value is not 1 or 0.

### Binary to decimal <br>
odd number 110011 => 1x2** 0 + 1x2** 1  + 0x2 ** 2 + 0x2 ** 3 + 1x2** 4 + 1x2** 5 => 51 <br>
even number 110010 => 1x2** 5 + 0x2** 4 + 0x2** 3 + 1x2** 2 + 0x2** 1 + 1x2** 0 => 50

### Decimal to octal <br>
Divide the value by 8 and write out the remainder aside. Repeat this step while value is not 1 or 0.

### Octal to decimal <br>
Octal number 3671 => 3x8** 3 + 6x8** 2 + 7x8** 1 + 1x8** 0 => 1977

### Decimal to hexadecimal <br>
Divide the value by 16 and write out the remainder aside. Repeat this step while value is not 1 or 0.

### Hexadecimal to decimal <br>
Hexadecimal number 19BCF => 1x16** 4 + 9x16** 3 + 11x16** 2 + 12x16** 1 + 15x16** 0 => 105423

Hexadecimal values:
A = 10 
B = 11
C = 12
D = 13
E = 14
F = 15

## Credits
This was pratice project in python. I added some print() statements to checkout the conversions. <br>The main goal was that the input could be any value, if it is not possible to convert the program should to ajust it.
