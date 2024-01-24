### Binary ###

def binary_to_decimal(input):
  decimal = 0
  exp = 0

  if input == '1' or input == '0':
    return input

  if input[-1] == '1':  
    input = input[::-1]

    for i in input:    
      decimal += int(i)*2**exp
      exp += 1

    return decimal
 
  if input[-1] == '0': 
    exp = len(input) - 1
    
    for i in input:    
      decimal += int(i)*2**exp
      exp -= 1

    return decimal
  
def decimal_to_binary(input):
  binary = ''
  input = int(input)

  while True: 
    if input == 1 or input == 0:
      binary += str(input)

      return binary[::-1]

    if input % 2 == 1:
      binary += '1'
      input = input // 2
    else:
      binary += '0'
      input = input // 2


### Octal ###

def octal_to_decimal(input):
  decimal = 0
  exp = len(input)-1

  for i in input:    
    decimal += int(i)*8**exp
    exp -= 1

  return decimal

def decimal_to_octal(input):
  octal_array = []
  input = int(input)

  if input == 1 or input ==0:
      octal_array.insert(0,str(input))

      return input

  while True:
    if input == 1:
      octal_array.insert(0,str(input))
      break

    if input ==0:
      break
  
    if input % 8 == 0:
      digit = '0'
      octal_array.insert(0,str(digit))
      input = input // 8
    else:
      digit = input % 8
      octal_array.insert(0,str(digit))
      input = input // 8

  octal = '' 
  for i in octal_array:
    octal += i

  return octal


### Hex ###

def hex_to_decimal(input):
  decimal = 0
  exp = len(input)-1
  hex_letter = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

  for i in input:    
    if i in hex_letter.keys():
      i = hex_letter[i]
      decimal += int(i)*16**exp
      exp -= 1
    
    else:
      decimal += int(i)*16**exp
      exp -= 1

  return decimal

def decimal_to_hex(input):
  hex_array = []
  hex_letter = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
  input = int(input)

  if input == 1 or input ==0:
      hex_array.insert(0,str(input))

      return input
  
  while True:
    if input == 1:
      hex_array.insert(0,str(input))
      break

    if input ==0:
      break
  
    if input % 16 == 0:
      digit = '0'
      hex_array.insert(0,str(digit))
      input = input // 16
    else:
      digit = input % 16

      if digit >= 10:
        hex_array.insert(0,str(hex_letter[digit]))
        input = input // 16
      else:
        hex_array.insert(0,str(digit))
        input = input // 16

  hex = '' 
  for i in hex_array:
    hex += i

  return hex


###Converter_check###

def converter_check(input):
  hex_array = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e','f']
  counter_binary = 0
  counter_octal = 0
      
  if input == '':
      print('Input is empty \n')
      print('input',input)
      return enter_input()

  for i in input:
    if i in hex_array:
      return 'hex', input

    if i == '0' or i == '1':
      counter_binary += 1
      if counter_binary == len(input):
        if input[0] == '0':
          return 'binary', input
        else:
          return 'binaryordecimal', input
    
    if i < '8':
      counter_octal += 1
      if counter_octal == len(input):
        return 'octalordecimal' ,input   
      
  return 'decimal', input  


 ### Converter ###
    
def converter(input):
  
  if input[0] == 'hex':
    print(f'Input = {input[1]} => {input[0]}')

    decimal = hex_to_decimal(input[1])
    octal = decimal_to_octal(hex_to_decimal(input[1]))
    binary = decimal_to_binary(hex_to_decimal(input[1]))

    print(f'Decimal = {decimal} \nOctal = {octal} \nBinary = {binary}\n')

  if input[0] == 'binary':
    print(f'Input = {input[1]} => {input[0]}')

    decimal = binary_to_decimal(input[1])
    octal = decimal_to_octal(binary_to_decimal(input[1]))
    hex = decimal_to_hex(binary_to_decimal(input[1]))

    print(f'Decimal = {decimal} \nOctal = {octal} \nHex = {hex}\n')

  if input[0] == 'binaryordecimal':
    print(f'Input = {input[1]} => binary')

    decimal = binary_to_decimal(input[1])
    octal = decimal_to_octal(binary_to_decimal(input[1]))
    hex = decimal_to_hex(binary_to_decimal(input[1]))

    print(f'Decimal = {decimal} \nOctal = {octal} \nHex = {hex}\n')

    print(f'Input = {input[1]} => decimal')

    octal = decimal_to_octal(input[1])
    hex = decimal_to_hex(input[1])
    binary = decimal_to_binary(input[1])

    print(f'Octal = {octal} \nHex = {hex} \nBinary = {binary}\n')

  if input[0] == 'octalordecimal':
    print(f'Input = {input[1]} => octal')

    decimal = octal_to_decimal(input[1])
    hex = decimal_to_hex(octal_to_decimal(input[1]))
    binary = decimal_to_binary(octal_to_decimal(input[1]))

    print(f'Decimal = {decimal} \nHex = {hex} \nBinary = {binary}\n')

    print(f'Input = {input[1]} => decimal')

    octal =  decimal_to_octal(input[1])
    hex =  decimal_to_hex(input[1])
    binary = decimal_to_binary(input[1])

    print(f'Octal = {octal} \nHex = {hex} \nBinary = {binary}\n')

  if input[0] == 'decimal':
    print(f'Input = {input[1]} => {input[0]}')

    octal =  decimal_to_octal(input[1])
    hex = decimal_to_hex(input[1])
    binary = decimal_to_binary(input[1])
  
    print(f'Octal = {octal} \nHex = {hex} \nBinary = {binary}\n')


### enter_input ##

def enter_input():
  hex_array = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e','f']
  number_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']

  while True:
    input_to_convert = ''
    input_to_convert = input('Enter a value to convert or "x" to exit: ')

    if input_to_convert == 'x':
      break

    for i in input_to_convert:
      if i not in hex_array and i not in number_array:
        print('Input =', input_to_convert, '=>', i, 'is not lavid in the number types and will be removed.')
        input_to_convert = input_to_convert.replace(i,'') 

        if input_to_convert == '':
          print('Input is empty')
          break
      
    if input_to_convert == '':
      print('Error: No input!\n')
      
    else:
      print('')
      converter(converter_check(input_to_convert))


#Converter(Converter_check('1F')) # hex
#Input = 1F => hex
#Decimal = 31
#Octal = 37
#Binary = 11111

#Converter(Converter_check('011111')) # binary
#Input = 011111 => binary
#Decimal = 31
#Octal = 37
#Hex = 1F
    
#Converter(Converter_check('11111')) # binaryordecimal
#Input = 11111 => binary
#Decimal = 31
#Octal = 37
#Hex = 1F

#Input = 11111 => decimal
#Octal = 25547
#Hex = 2B67
#Binary = 10101101100111

#Converter(Converter_check('31')) # octalordecimal
#Input = 31 => octal
#Decimal = 25
#Hex = 19
#Binary = 11001

#Input = 31 => decimal
#Octal = 37
#Hex = 1F
#Binary = 11111

#Converter(Converter_check('128')) # decimal
#Input = 128 => decimal
#Octal = 200
#Hex = 80
#Binary = 10000000


#Converter(Converter_check('acbfde')) # lowercase letter for hex number
#Input = acbfde => hex
#Decimal = 11321310
#Octal = 53137736
#Binary = 101011001011111111011110

#enter_input() # invalid input '10!gh5Aijk'
#Input = 10!gh5Aijk => ! is not lavid in the number types and will be removed.
#Input = 10gh5Aijk => g is not lavid in the number types and will be removed.
#Input = 10h5Aijk => h is not lavid in the number types and will be removed.
#Input = 105Aijk => i is not lavid in the number types and will be removed.
#Input = 105Ajk => j is not lavid in the number types and will be removed.
#Input = 105Ak => k is not lavid in the number types and will be removed.

#Input = 105A => hex
#Decimal = 4186
#Octal = 10132
#Binary = 1000001011010

enter_input()
