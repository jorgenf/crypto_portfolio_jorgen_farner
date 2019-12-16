import math
import random

#checks if a and b are coprime.
def is_coprime(a, b):
    #first runs the miller rabin primality test to see i either are primes which would mean they are coprime
    if miller_rabin(a) or miller_rabin(b):
        return True
    #if gcd is 1 then they share no factors and are coprime
    if math.gcd(a, b) == 1:
        return True
    else:
        return False

#alternately takes the modulus of one side until b is 0, which indicates they share a factor a
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

#runs through string and increments positions in a list based on numerical value of the number
def calculate_frequency(text):
    text = clean_string(text.lower())
    freq_array = [0] * 26
    for char in text:
        freq_array[ord(char) - 97] += 1
    return freq_array

#gets the extended gcd by taking the mod of one side until m is 0
# and updating x1 to y minus int of n/m times x. y1 is then set to x
def extended_gcd(m, n):
    if m == 0:
        return 0, 1
    else:
        x, y = extended_gcd(n % m, m)
        x1 = y - (n // m) * x
        y1 = x
        return x1, y1

#slow algorithm for checking primality
def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or n == 0 or n%2 == 0:
        return False
    x = 3
    #runs a loop from x to sqrt(n) and checks if x divides n
    while x <= math.sqrt(n):
        if n % x == 0:
            return False
        x += 2
    return True

#checks if p is a primitive root of n
def is_primitive_root(p,n):
    if not is_prime(n):
        return False
    #creates list of all numbers coprime to n
    co_primes = []
    #the set of p to the power of a nummber between 1 and n
    p_set = set()
    for i in range (1,n):
        p_set.add(int(math.pow(p,i)%n))
        if is_coprime(i,n):
            co_primes.append(i)
        #if all numbers coprime to n is in the p_set then p is a primitive root of n
    if all(elem in p_set for elem in co_primes):
        return True
    else:
        return False

#checks if the input word is in the file corncob_lowercase.txt which is a list of all english words
def word_check(word):
    dictionary = open("corncob_lowercase.txt","r").read().splitlines()
    if word in dictionary:
        return True
    else:
        return False

#shifts a list to the right for a specified number
def shift_list(text,shifts):
    for shift in range(shifts):
        last = text[len(text) - 1]
        for i in range(len(text)-1,-1,-1):
            text[i] = text[i-1]
        text[0] = last
    return text

#inserts a 0 at index 0
def shift_text(text):
    return_text = text
    return_text.insert(0,"0")
    return return_text

#filters out all special characters and numbers
def clean_string(plaintext):
    return_text = ''.join(filter(str.isalpha,list(plaintext)))
    return return_text

#removes duplicates in string
def remove_duplicate(text):
    return ''.join(dict.fromkeys(text))

#creates a random prine between 2^b-1 to s^(b-1)-1
def random_prime(b):
    #creates a list of all the primes in the range and chooses a random from that list
    if (math.pow(2, b) - 1) % 2 == 0:
        p = [i for i in range(int(math.pow(2,b)),int(math.pow(2,b+1)-1),2) if is_prime(i)]
    else:
        p = [i for i in range(int(math.pow(2, b)-1), int(math.pow(2, b + 1) - 1), 2) if is_prime(i)]
    return random.choice(p)

#creates an arbitrary large prime by creating a string of random bits and checking if it is prime by miller rabin
def random_n_bit_prime(n):
    while True:
        bits = []
        bits.append('1')
        for i in range(n-2):
            bits.append(str(random.randint(0,1)))
        bits.append('1')
        num = int("".join(bits),2)
        if miller_rabin(num):
            return num

#a quick way of checking primality
def miller_rabin(n,k=128):
    #checks if 2 divides n or n is less than two
    if n%2 == 0 or n < 2:
        return False
    s = 0
    d = n - 1
    #counts how many times d can be divided by two by incrementing s each time
    while d & 1 == 0:
        s += 1
        d //= 2
    #runs a loop specified by input. higher k will give higher certainty
    for i in range(k):
        #creates a random a
        a = random.randint(2,n-1)
        #x is set to a^d mod n
        x = pow(a,d,n)
        #if the result is not 1 or n-1 an inner loop is run
        if x != 1 and x != n - 1:
             j = 1
             #runs until j equal s and x is not equal to n-1
             while j < s and x != n-1:
                x = pow(x,2,n)
                j += 1
                #if x==1 then n is not a prime
                if x == 1:
                    return False
             #if n is not equal to n-1 then n is not a prime
             if x != n-1:
                return False
    return True

#an algorithm i found online to avoid recursion errors that happen with the modInv at the huge
#numbers used in RSA. Dont know how this thing works...
def findModInverse(a, n):
    if not is_coprime(a,n):
        return -1
    n0 = n
    y = 0
    x = 1
    if (n == 1):
        return 0
    while (a > 1):
        q = a // n
        t = n
        n = a % n
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + n0
    return x

#simply gets the mod inverse by taking the extended gcd
def modInv(a,n):
    x,y = extended_gcd(a,n)
    return x%n


