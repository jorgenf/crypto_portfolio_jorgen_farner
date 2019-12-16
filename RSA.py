import random

import crypto_math

#encryption function that does the math c=m^e mod n
def encrypt(m,key_lenght=1024):
    m = crypto_math.clean_string(m.lower())
    c = ""
    for letter in m:
        c += format(ord(letter),"#03")
    c = int(c)
    e,d,n = generate_keys(key_lenght)
    c = pow(c,e,n)
    return c,d,n,e



def generate_keys(bits):
    p = crypto_math.random_n_bit_prime(bits)
    q = crypto_math.random_n_bit_prime(bits)
    #create modulus
    n = p*q
    #creates the euler totient function
    o = (p-1)*(q-1)
    #creates public key exponent
    e = random.randint(1,o)
    while not crypto_math.is_coprime(e,o):
        e = random.randint(1, o-1)
    #creates private key exponent
    d = crypto_math.findModInverse(e,o)
    return e,d,n

#decrypts by doing d^d mod n
def decrypt(c,d,n):
    m = str(pow(c,d,n))
    ret = ""
    for letter in range(0,len(str(m)),3):
        ret += chr(int(m[letter:letter+3]))
    return ret


