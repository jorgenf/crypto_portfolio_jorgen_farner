#the s-box used for AES
s_box = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
         [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
         [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
         [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
         [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
         [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
         [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
         [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
         [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
         [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
         [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
         [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
         [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
         [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
         [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
         [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

#used in mixColumns
mix_column_matrix = [[2, 3, 1, 1],
                     [1, 2, 3, 1],
                     [1, 1, 2, 3],
                     [3, 1, 1, 2]]

#the rcon matrix used in roundkey generation
rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]]

#example input
input = [[0x32, 0x88, 0x31, 0xe0],
         [0x43, 0x5a, 0x31, 0x37],
         [0xf6, 0x30, 0x98, 0x07],
         [0xa8, 0x8d, 0xa2, 0x34]]
#example key
key = [[0x2b, 0x28, 0xab, 0x09],
       [0x7e, 0xae, 0xf7, 0xcf],
       [0x15, 0xd2, 0x15, 0x4f],
       [0x16, 0xa6, 0x88, 0x3c]]


#encrypt function
def encrypt(input, key):
    output = input
    #runs 11 rounds which includes the first addRoundkey
    for round in range(0, 11):
        if round == 0:
            output = add_roundKey(input, get_roundKey(key, round))
        #runs last round without mixcolumns
        if round == 11:
            output = sub_bytes(output)
            output = shift_rows(output)
            output = add_roundKey(output, get_roundKey(key, round))
            break
        #runs the main rounds
        output = sub_bytes(output)
        output = shift_rows(output)
        output = mix_columns(output)
        output = add_roundKey(output, get_roundKey(key, round))
    return output

#substitutes each byte with the correct value form the x-box
def sub_bytes(input):
    for row in range(0, len(input)):
        for column in range(0, len(input[0])):
            input[row][column] = s_box[int("0x{:02x}".format(input[row][column])[2], 16)][
                int("0x{:02x}".format(input[row][column])[3], 16)]
    return input

#function that is used in the key generation to do subBytes for a column at a time
def sub_bytes_list(input):
    for column in range(0, len(input)):
        input[column] = s_box[int("0x{:02x}".format(input[column])[2], 16)][int("0x{:02x}".format(input[column])[3], 16)]
    return input

#shifts the rows. 0 shift for first row, 1 shift for 2nd, 2 shift for 3rd and 3 shifts for 4th
def shift_rows(input):
    for i in range(3):
        input[3] = rotate(input[3])
        if i < 2:
            input[2] = rotate(input[2])
        if i < 1:
            input[1] = rotate(input[1])
    return input

#goes through matrix and calculates dot product in gf(8).
def mix_columns(input):
    for column in range(len(input)):
        result = 0
        for row in range(len(input)):
            for row_m in range(len(input)):
                result = result ^ mult_GF8(input[row_m][column], mix_column_matrix[row_m][column])
            input[row][column] = result
    return input

#xor the input with the roundkey, element for element
def add_roundKey(input, roundKey):
    for column in range(len(input)):
        for row in range(len(input)):
            input[row][column] = input[row][column] ^ roundKey[row][column]
    return input

#does one rotation of a row
def rotate(row):
    temp = row[0]
    row[0] = row[3]
    row[3] = row[2]
    row[2] = row[1]
    row[1] = temp
    return row

#this algorithm does multiplication in the 2^8 galois field
def mult_GF8(a, b):
    p = 0
    #checks if one side is 0, which will result in 0
    if a == 0 or b == 0:
        return 0
    #a loop to go through all 8 bits
    for i in range(8):
        #checks if b is odd and if thats the case p is set to equal p xored with a
        if b & 1 == 1:
            p = p ^ a
        #if the leftmost bit is set to 1, then the high_set is true, if not it is false
        if format(a, '#08b')[2] == '1':
            high_set = True
        else:
            high_set = False
        #a is rotated left one bit
        a = rol_1(a)
        #if high_set is true then a is xored with hex value 1b
        if high_set:
            a = a ^ 0x1b
        #b is rotated right 1 bit
        b = ror_1(b)
    return p

#rotates input left one bit
def rol_1(input_8):
    input_8 = list(format(input_8, '#010b'))
    for i in range(2, 9):
        input_8[i] = input_8[i + 1]
    input_8[9] = '0'
    return int(''.join(input_8), 2)

#rotates input right one bit
def ror_1(input_8):
    input_8 = list(format(input_8, '#010b'))
    for i in range(9, 2, -1):
        input_8[i] = input_8[i - 1]
    input_8[2] = '0'
    return int(''.join(input_8), 2)

#creates the round key
def get_roundKey(key, round):
    #keeps track of current column of rcon
    rcon_count = 0
    #loop for columns of the extended key from the end of the main key to the last column of the last round key
    for column in range(4, 44):
        for row in range(4):
            #add rows so that they can be acecced
            key[row].append("")
        #check for every 4th column, or every first column of a roundkey
        if column % 4 == 0:
            #takes the previous column and rotates it
            key = rotword(key, column)
            col = [i[column] for i in key]
            #does subBytes for col which is key
            sub = sub_bytes_list(col)
            #does XOR of the sub column, the correct rcon column, and the column 4 columns behind it
            for row_ in range(4):
                key[row_][column] = key[row_][column - 4] ^ sub[row_] ^ rcon[row_][rcon_count]
            rcon_count += 1
        else:
            #if its not a 4th column it is simply an xor of previous and 4 columns previous
            for row__ in range(4):
                key[row__][column] = key[row__][column-1] ^ key[row__][column-4]
    round_key = [[],[],[],[]]
    for row___ in range(4):
        for column_ in range(4):
            round_key[row___].append(key[row___][column_ + (4*round)])
    return round_key

#rotates a list 1 place
def rotword(key, column):
    temp = key[0][column - 1]
    key[0][column] = key[1][column - 1]
    key[1][column] = key[2][column - 1]
    key[2][column] = key[3][column - 1]
    key[3][column] = temp
    return key
