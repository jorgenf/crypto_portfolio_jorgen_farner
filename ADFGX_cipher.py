import math
import textwrap
import numpy as np
import crypto_math

#This matrix is a predefined matrix used for the ADFGX cipher
adfgx = [['null', 'a', 'd', 'f', 'g', 'x'],
         ['a', 'p', 'g', 'c', 'e', 'n'],
         ['d', 'b', 'q', 'o', 'z', 'r'],
         ['f', 's', 'l', 'a', 'f', 't'],
         ['g', 'm', 'd', 'v', 'i', 'w'],
         ['x', 'k', 'u', 'y', 'x', 'h']]

#list of the alphabet used
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

#the encrypt function for ADFGX cipher.
def encrypt(plaintext, keyword):
    #turns input string into a string of all characters
    plaintext = crypto_math.clean_string(plaintext)
    #removes duplicates and adjust the lenght of the keyword in case its
    #longer than the plaintext
    keyword = adjust_keyword_length(crypto_math.remove_duplicate(keyword), plaintext)
    ciphertext = []
    #runs through all characters of the plaintext and changes them according to the matrix
    for i in list(plaintext):
        ciphertext.append(''.join(change_character(i)))
    ciphertext = ''.join(ciphertext)
    #creates the matrix based on keyword
    matrix = create_matrix(ciphertext, keyword)
    rows, columns = matrix.shape
    return_string = ""
    #sorts the columns based on the keyword
    for character in alphabet:
        for i in range(rows - 1, -1, -1):
            if str(matrix[i][0])[2] == character:
                for j in range(1, len(matrix[i])):
                    add_char = str(matrix[i][j])[2]
                    if add_char.isalpha():
                        return_string += add_char
    return return_string

#creates the matrix for encryption
def create_matrix(ciphertext, keyword):
    keyword = list(keyword)
    ciphertext = list(ciphertext)
    #sets the size of the matrix
    column = math.ceil((len(ciphertext) / len(keyword))) + 1
    row = len(keyword)
    matrix = np.chararray((row, column))
    #fills matrix with '?' so that values and non-value can be distinguished
    matrix[:] = '?'
    count = 0
    #inputs the keyword into the first row, which is technically the first column
    for i in range(len(keyword) - 1, -1, -1):
        matrix[i][0] = keyword[count]
        count += 1
    column = 1
    row = len(keyword) - 1
    #inputs the text into the matrix
    for i in range(0, len(ciphertext)):
        matrix[row][column] = ciphertext[i]
        row -= 1
        if row == -1:
            row = len(keyword) - 1
            column += 1
    return matrix

#changes a plaintext character into its correspondig two characters from the matrix
def change_character(character):
    if character == 'j':
        character = 'i'
    for row in range(len(adfgx)):
        for column in range(len(adfgx[row])):
            if adfgx[row][column] == character and column != 0 and row != 0:
                return_character = adfgx[row][0] + adfgx[column][0]
                return return_character

#changes the lenght of the keyword if it is longer than the plaintext. If so, it is set to equal the plaintext
def adjust_keyword_length(keyword, text):
    if len(keyword) > len(text):
        keyword = keyword[0:len(text)]
    return keyword

#creates the matrix for decryption. A different function was needed because rows and columns
#are filled in different order for encryption and decryption
def create_decrypt_matrix(ciphertext,sorted_keyword):
    #creates lists of equal lenghts
    matrix = textwrap.wrap(ciphertext, math.ceil(len(ciphertext)/len(sorted_keyword)))
    #the wrap function fills the first lists first, so there could be a difference in lenght
    #of 2. this for loop makes sure the biggest difference in lenght is 1.
    for i in range(1,len(matrix)):
        if len(matrix[0]) > len(matrix[i])+1:
            matrix[i] = matrix[i-1][-1:] + matrix[i]
            matrix[i-1] = matrix[i-1][:-1]
    matrix = [cipher + elem for cipher, elem in zip(list(sorted_keyword), matrix)]
    return matrix

#changes two characters at a time back to their on character plaintext character.
def change_back_character(character_1, character_2):
    for row in range(len(adfgx)):
        if adfgx[row][0] == character_1:
            char_row = row
            for column in range(len(adfgx[row])):
                if adfgx[0][column] == character_2:
                    return_character = adfgx[char_row][column]
    return return_character

#encryption method reversed.
def decrypt(ciphertext, keyword):
    ciphertext = crypto_math.clean_string(ciphertext)
    sorted_keyword = list(adjust_keyword_length(crypto_math.remove_duplicate(crypto_math.clean_string(keyword)), ciphertext))
    #the first row of the matrix needs to be sorted
    sorted_keyword.sort()
    matrix = create_decrypt_matrix(ciphertext,sorted_keyword)
    str = ""
    maxl = (len(max(matrix, key=len))-1)
    return_matrix = ['']*len(matrix)
    for key in range(len(keyword)):
        for i in range(len(matrix)):
            #sorts the columns back to keyword
            if keyword[key] == matrix[i][0]:
                #fills up lists with '?' so their lenght will be equal(left adjust) to check for real values
                return_matrix[key] = matrix[i][1::].ljust(maxl, '?')
    for row in range(len(max(return_matrix, key=len))):
        for column in range(len(return_matrix)):
            if return_matrix[column][row] != '?':
                #gets return string by check if value is '?' or a real value
                str += return_matrix[column][row]
    str = ''.join(str)
    return_string = ""
    for character in range(0,len(str),2):
        return_string += change_back_character(str[character],str[character+1])
    return return_string
