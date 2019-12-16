import re
import crypto_math

#letters ordered by frequency in english language
freq = ['e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z']
#frequency of letters a to z
freq_let = [0.08167,0.01492,0.02202,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.0153,0.01292,0.04025,0.02406,0.06749,0.07507,0.01929,0.0095,0.05987,0.06327,0.09356,0.02758,0.00978,0.02560,0.0015,0.01994,0.0077]


def encrypt(plaintext, key):
    plaintext = crypto_math.clean_string(plaintext)
    if not check_input(plaintext, key):
        return -1
    text_array = list(plaintext.lower())
    key_array = list(match_key_to_text(plaintext, key).lower())
    return_string = ""
    #runs through both key and input array and adds the key to the plaintext
    for text, key in zip(text_array, key_array):
        text = chr(((ord(text) - 97 + ord(key) - 97) % 26) + 97)
        return_string += text
    return return_string


def decrypt(ciphertext, key):
    if not check_input(ciphertext, key):
        return -1
    text_array = list(ciphertext.lower())
    key_array = list(match_key_to_text(ciphertext, key).lower())
    return_string = ""
    #reverses encryption by running through both arrays and subtracting the key
    for text, key in zip(text_array, key_array):
        text = (ord(text) - ord(key) + 97)
        while (text < 97):
            text += 26
        return_string += chr(text)
    return return_string

#repeats key if it is shorter than input and cuts in short if it is longer
def match_key_to_text(text, key):
    if len(key) > len(text):
        key = key[0:len(text)]
    else:
        while (len(key) < len(text)):
            key += key
            if len(key) > len(text):
                key = key[0:len(text)]
    return key


def check_input(text, key):
    if not text.isalpha() or not key.isalpha():
        return False
    else:
        return True

#finds keylenght using method described in books. takes two lists and moves one iteratively to the right
# and checks for matching characters. the shift that produces most matches is the keylenght
def find_keylenght(ciphertext):
    ciphertext = re.sub("[^a-zA-Z]","", ciphertext).lower()
    ciphertext_original = list(ciphertext)
    ciphertext_shifted = list(ciphertext)
    count = len(ciphertext)*[0]
    for i in range(1,len(ciphertext)):
        ciphertext_shifted = crypto_math.shift_text(ciphertext_shifted)
        for j in range(i,len(ciphertext)):
            if ciphertext_original[j] == ciphertext_shifted[j]:
                count[i-1] += 1
    return count.index(max(count)) + 1

#uses the second method described in the book.
#say keylenght is 3. takes all 0th+k*3 and runs a frequancy analysis. then the 1th+k*3 and so on
def find_key(ciphertext):
    keylength = find_keylenght(ciphertext)
    key = ""
    for i in range(keylength):
        text = ""
        for j in range(i,len(ciphertext),keylength):
            text += ciphertext[j]
        w = [x / len(text) for x in crypto_math.calculate_frequency(text)]
        dot = []
        for a_i in range(25):
            a = crypto_math.shift_list(freq_let, a_i)
            sum = 0
            for w_i,a_i in zip(w,a):
                sum += w_i*a_i
            dot.append(sum)
        key += chr(dot.index(max(dot))+97)
    return key
