import ADFGX_cipher
import AES
import RSA
import affine_cipher
import crypto_math
import factoring
import sDES
import vigenere_cipher


def start():
    choice = first_menu()
    if choice == 1:
        classical_cryptosystems()
    elif choice == 2:
        basic_number_theory()
    elif choice == 3:
        des()
    elif choice == 4:
        rsa()

def first_menu():
    print()
    print("MAIN MENU")
    print("Choose module:")
    print("1: Classical cryptosystems\n2: Basic number theory\n3: Data Encryption Standard\n4: The RSA algorithm")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 4:
                raise Exception
            if choice == 1:
                return classical_cryptosystems()
            if choice == 2:
                return basic_number_theory()
            if choice == 3:
                return des()
            if choice == 4:
                rsa()
        except:
            print("Invalid input")


def classical_cryptosystems():
    print()
    print("CLASSICAL CRYPTOSYSTEMS")
    print("1: Affine Cipher\n2: Vigenère Cipher\n3: ADFGX Cipher\n4: Frequency calculation\n5: Main Menu")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 5:
                raise Exception
            if choice == 1:
                return affine_cipher_menu()
            if choice == 2:
                return vigenere_cipher_menu()
            if choice ==3:
                return ADFGX_menu()
            if choice == 4:
                return frequency_menu()
            if choice == 5:
                return start()
        except:
            print("Invalid input")
        print()


def affine_cipher_menu():
    print()
    print("AFFINE CIPHER")
    print("1: Encrypt\n2: Decrypt\n3: Brute force attack\n4: Known plaintext attack\n5: Back")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 5:
                raise Exception
            if choice == 1:
                print(affine_cipher_encrypt())
            if choice == 2:
                print(affine_cipher_decrypt())
            if choice == 3:
                print(affine_brute_force())
            if choice == 4:
                print(affine_known_plaintext())
            if choice == 5:
               return classical_cryptosystems()
        except:
            print("Invalid input")

def affine_cipher_encrypt():
    print()
    while True:
        try:
            plaintext = input("Enter plaintext: ")
            a = int(input("Enter α: "))
            b = int(input("Enter β: "))
            c = affine_cipher.encrypt(a, b,plaintext)
            if c == -1:
                raise Exception
            print("Ciphertext: ",c)
            return affine_cipher_menu()
        except:
            print("Invalid input")

def affine_cipher_decrypt():
    print()
    while True:
        try:
            ciphertext = input("Enter ciphertext: ")
            a = int(input("Enter α: "))
            b = int(input("Enter β: "))
            m = affine_cipher.decrypt(a, b,ciphertext)
            if m == -1:
                raise Exception
            print("Plaintext: ",m)
            return affine_cipher_menu()
        except:
            print("Invalid input")

def affine_brute_force():
    while True:
        try:
            ciphertext = input("Enter ciphertext: ")
            if not ciphertext.isalpha():
                raise Exception
            m = affine_cipher.brute_force(ciphertext)
            print("Possible plaintexts: ",m)
            return affine_cipher_menu()
        except:
            print("Invalid input")

def affine_known_plaintext():
    while True:
        try:
            x0 = input("Enter x0: ")
            x1 = input("Enter x1: ")
            y0 = input("Enter y0: ")
            y1 = input("Enter y1: ")
            if x0.isalpha() and x1.isalpha() and y0.isalpha() and y1.isalpha():
                a,b = affine_cipher.known_plaintext(x0,x1,y0,y1)
                print("a: ",a," b: ",b)
                return affine_cipher_menu()
            else:
                raise Exception
        except:
            print("Invalid input")


def vigenere_cipher_menu():
    print()
    print("VIGENERE CIPHER")
    print("1: Encrypt\n2: Decrypt\n3: Find key attack\n4: Back")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 4:
                raise Exception
            if choice == 1:
                print(vigenere_encrypt())
            if choice == 2:
                print(vigenere_decrypt())
            if choice == 3:
                print(vigenere_find_key())
            if choice == 4:
               return classical_cryptosystems()
        except:
            print("Invalid input")

def vigenere_encrypt():
    print()
    while True:
        try:
            plaintext = input("Enter plaintext: ")
            key = input("Enter key: ")
            c = vigenere_cipher.encrypt(plaintext,key)
            if c == -1:
                raise Exception
            print("Ciphertext: ",c)
            return vigenere_cipher_menu()
        except:
            print("Invalid input")

def vigenere_decrypt():
    print()
    while True:
        try:
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")
            m = vigenere_cipher.decrypt(ciphertext,key)
            if m == -1:
                raise Exception
            print("Plaintext: ",m)
            return vigenere_cipher_menu()
        except:
            print("Invalid input")

def vigenere_find_key():
    print()
    print("WARNING: Does not work very well")
    while True:
        try:
            ciphertext = input("Enter ciphertext: ")
            key = vigenere_cipher.find_key(ciphertext)
            print("Key: ",key)
            return vigenere_cipher_menu()
        except:
            print("Invalid input")

def ADFGX_menu():
    print()
    print("WARNING: Decryption works with ciphertext with lenght that is a multiple of the keylength")
    print("ADFGX CIPHER")
    print("1: Encrypt\n2: Decrypt\n3: Back")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 3:
                raise Exception
            if choice == 1:
                print(ADFGX_encrypt())
            if choice == 2:
                print(ADFGX_decrypt())
            if choice == 3:
               return classical_cryptosystems()
        except:
            print("Invalid input")

def ADFGX_encrypt():
    print()
    while True:
        try:
            plaintext = input("Enter plaintext: ")
            key = input("Enter key: ")
            ciphertext = ADFGX_cipher.encrypt(plaintext,key)
            print("Ciphertext: ",ciphertext)
            return ADFGX_menu()
        except:
            print("Invalid input")

def ADFGX_decrypt():
    print()
    while True:
        try:
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")
            plaintext = ADFGX_cipher.decrypt(ciphertext,key)
            print("Plaintext: ",plaintext)
            return ADFGX_menu()
        except:
            print("Invalid input")


def frequency_menu():
    print()
    while True:
        try:
            string = input("Enter string: ")
            list = crypto_math.calculate_frequency(string)
            alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
            return_list = []
            for a,b in zip(alf,list):
                elem = str(a)+": "+str(b)
                return_list.append(elem)
            print("Frequency list: ",return_list)
            return classical_cryptosystems()
        except:
            print("Invalid input")

def basic_number_theory():
    print()
    print("BASIC NUMBER THEORY")
    print("1: GCD\n2: Extended GCD\n3: Find modular inverse\n4: Verify primitive root\n5: Main Menu")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 5:
                raise Exception
            if choice == 1:
                return gcd_menu()
            if choice == 2:
                return extendedGCD_menu()
            if choice ==3:
                return modInv_menu()
            if choice == 4:
                return primRoot_menu()
            if choice == 5:
                return start()
        except:
            print("Invalid input")
        print()

def gcd_menu():
    print()
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            gcd = crypto_math.gcd(a,b)
            print("GCD: ",gcd)
            return basic_number_theory()
        except:
            print("Invalid input")

def extendedGCD_menu():
    print()
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            gcd = crypto_math.extended_gcd(a,b)
            print("Extended GCD: ",gcd)
            return basic_number_theory()
        except:
            print("Invalid input")

def modInv_menu():
    print()
    while True:
        try:
            a = int(input("Enter number: "))
            b = int(input("Enter modulus: "))
            modInv = crypto_math.modInv(a,b)
            print("Modular inverse: ",modInv)
            return basic_number_theory()
        except:
            print("Invalid input")

def primRoot_menu():
    print()
    while True:
        try:
            a = int(input("Enter number: "))
            b = int(input("Enter prime: "))
            isPrimRoot = crypto_math.is_primitive_root(a,b)
            print("Is primitive root: ",isPrimRoot)
            return basic_number_theory()
        except:
            print("Invalid input")

def des():
    print()
    print("DATA ENCRYPTION STANDARD")
    print("1: DES\n2: AES\n3: Main Menu")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 3:
                raise Exception
            if choice == 1:
                return DES_menu()
            if choice == 2:
                return AES_menu()
            if choice ==3:
                return start()
        except:
            print("Invalid input")

def DES_menu():
    print()
    print("SIMPLIFIED DES")
    print("1: Encrypt\n2: Cryptanalysis\n3: Back")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 3:
                raise Exception
            if choice == 1:
                print(DES_encrypt())
            if choice == 2:
                DES_cryptanalysis()
            if choice == 3:
               return des()
        except:
            print("Invalid input")

def DES_encrypt():
    print()
    while True:
        try:
            print("Plaintext must be a 12-bit string or equivalent numeric value")
            plaintext = input("Enter plaintext: ")
            print("Key must be a 9-bit string or equivalent numeric value")
            key = input("Enter key: ")
            rounds=int(input("Enter number of rounds: "))
            c = sDES.encrypt(plaintext,key,rounds)
            print("Ciphertext:",c)
            return DES_menu()
        except:
            print("Invalid input")

def DES_cryptanalysis():
    print()
    print("Demonstration of cryptanalysis of DES")
    sDES.differential_cryptanalysis()
    return DES_menu()

def AES_menu():
    print()
    print("ADVANCED ENCRYPTION STANDARD")
    print("1: Encrypt\n2: Back")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 3:
                raise Exception
            if choice == 1:
                print(AES_encrypt())
            if choice == 2:
               return des()
        except:
            print("Invalid input")

def AES_encrypt():
    print()
    while True:
        input_matrix = []
        key_matrix = []
        try:
            print("Enter values for the input matrix")
            for row in range(4):
                list = []
                for column in range(4):
                    inp = int(input("Enter a 2-digit hex value: "))
                    while inp < 0 or inp > 255:
                        inp = int(input("Enter a 2-digit hex value: "))
                    list.append(inp)
                input_matrix.append(list)
            print("Enter values for the key matrix")
            for row in range(4):
                key_list = []
                for column in range(4):
                    inp2 = int(input("Enter a 2-digit hex value: "))
                    while inp2 < 0 or inp2 > 255:
                        inp2 = int(input("Enter a 2-digit hex value: "))
                    key_list.append(inp2)
                key_matrix.append(key_list)
            print(AES.encrypt(input_matrix,key_matrix))
            return DES_menu()
        except:
            print("Invalid input")

def rsa():
    print()
    print("The RSA algorithm")
    print("1: RSA\n2: Factorization algorithms\n3: Main Menu")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 3:
                raise Exception
            if choice == 1:
                return RSA_menu()
            if choice == 2:
                return factorization_menu()
            if choice ==3:
                return start()
        except:
            print("Invalid input")


def RSA_menu():
    print()
    print("RSA")
    print("1: Encrypt\n2: Decrypt\n3: Back")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 3:
                raise Exception
            if choice == 1:
                print(RSA_encrypt())
            if choice == 2:
                print(RSA_decrypt())
            if choice == 3:
               return rsa()
        except:
            print("Invalid input")


def RSA_encrypt():
    print()
    while True:
        try:
            plaintext = input("Enter plaintext: ")
            c,d,n,e = RSA.encrypt(plaintext)
            print("Ciphertext:           ",c)
            print("Private key exponent: ",d)
            print("Modulus:              ", n)
            print("Public key exponent:  ", e)
            return RSA_menu()
        except:
            print("Invalid input")


def RSA_decrypt():
    print()
    while True:
        try:
            c = int(input("Enter ciphertext: "))
            d = int(input("Enter private key exponent: "))
            n = int(input("Enter modulus: "))
            m = RSA.decrypt(c, d,n)
            print("Plaintext: ", m)
            return RSA_menu()
        except:
            print("Invalid input")

def factorization_menu():
    print()
    print("Factorization methods")
    print("1: Fermat\n2: Pollard's rho\n3: Pollard's p-1\n4: Shanks's square forms\n5: Back")
    while True:
        try:
            choice = input("Choice: ")
            choice = int(choice)
            if choice < 1 or choice > 5:
                raise Exception
            if choice == 5:
                rsa()
            number = int(input("Enter number to factor: "))
            print(factoring.factor(number,choice))
            return factorization_menu()
        except:
            print("Invalid input")