import math
import crypto_math


def decrypt(a, b, cipher_text):
    if check_input(a,cipher_text):
        char_array = list(cipher_text.lower())
        return_string = ""
        #runs through the ciphertext and subtracts b
        for i in char_array:
            numerical_value = ord(i) - 97 - b
            #if the subtraction leads to negative number, 26 is added until postitiv
            while numerical_value < 0:
                numerical_value += 26
            #checks if result can be divided by a and give an integer
            if numerical_value / a == math.floor(numerical_value / a):
                numerical_value /= a
            #if it cant, mod inverse is taken of a and multiplied with the numerical_value
            else:
                mod_inverse = crypto_math.modInv(a, 26)
                numerical_value *= mod_inverse
            #adds the resulting characters to a string
            return_string += chr((int)(numerical_value % 26) + 97)
        return return_string
    else: return -1


def encrypt(a, b, plaintext):
    #removes anything other than letters
    plaintext = crypto_math.clean_string(plaintext)
    if check_input(a, plaintext):
        char_array = list(plaintext.lower())
        return_string = ""
        #runs through string and multiplies by a and adds b (mod 26)
        for i in char_array:
            numerical_value = (((ord(i) - 97) * a + b) % 26) + 97
            return_string += chr(numerical_value)
        return (return_string)
    else:
        return -1

#checks that a and 26 are coprime and not characters
def check_input(a, text):
    if not crypto_math.is_coprime(a, 26) or not text.isalpha():
        return False
    else:
        return True

#known plaintext attack. x0 and x1 is two plaintext characters and y0 and y1 is their respective cipher characters
def known_plaintext(x0,x1,y0,y1):
    x0 = ord(x0)-97
    x1 = ord(x1)-97
    y0 = ord(y0)-97
    y1 = ord(y1)-97
    #checks which number is greater inorder to subtract and take mod inverse
    #this whole bit is basically solving two linear equations with two unknowns.
    if x0 >= x1:
        x = crypto_math.findModInverse(x0 - x1,26)
        y = (y0 - y1) % 26
        if x == -1:
            return -1
    else:
        x = crypto_math.findModInverse(x1 - x0, 26)
        y = (y1 - y0) % 26
        if x == -1:
            return -1
    a = (y*x)%26
    b = (y0-x0*a)%26
    return a,b

#this brute force attack just tries all combinations of a and b and checks the result with corncob_lowercase.txt
#which contain all english words.
def brute_force(cipchertext):
    return_list = []
    for a in range(26):
        for b in range(26):
            plaintext = decrypt(a,b,cipchertext)
            if crypto_math.word_check(plaintext):
                return_list += plaintext, a, b
    return return_list
