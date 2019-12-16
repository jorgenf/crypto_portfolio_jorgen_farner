import math
import random

import crypto_math

#function that takes the input to factor and which method to use
def factor(n, m):
    if crypto_math.miller_rabin(n) or n < 3:
        return -1
    elif m == 1:
        return fermat(n)
    elif m == 2:
        return pollard_rho(n)
    elif m == 3:
        return pollard_p1(n)
    elif m == 4:
        return shanks_square_forms(n)

#fermat method
def fermat(n):
    #starts the quessing by using the square root of n
    s = math.ceil(math.sqrt(n))
    #increases s until it creates a perfect square
    while math.sqrt(math.pow(s, 2) - n) != math.ceil(math.sqrt(math.pow(s, 2) - n)):
        s += 1
    #the square root of s^2-n is the +- from the s to get the two factors
    sum = math.sqrt(math.pow(s, 2) - n)
    r1 = int(s + sum)
    r2 = int(s - sum)
    return r1, r2


def pollard_rho(n):
    while True:
    #starts by getting to random numbers
        x = random.randint(0, 1000)
        c = random.randint(0, 1000)
        y = x
        #updates x to equal the function g(x)
        x = (math.pow(x, 2) + c) % n
        #updates y to equal g(g(y))
        y = (math.pow(math.pow(y, 2) + c, 2) + c) % n
        #gets the gcd of the absolute value of x-y and n, and if this is not equal to n or 1,
        #then it is one of the factors and the other can then also be found
        GCD = crypto_math.gcd(abs(x - y), n)
        if GCD != n and GCD != 1:
            return int(GCD), int(n / GCD)

def pollard_p1(n):
    a = 2
    #increments a until its not coprime with n
    while not crypto_math.is_coprime(n, a):
        a += 1
    #increments k in p=a^!k-1 mod n unti p is not equal to 1 which means its a factor
    count = 1
    p = crypto_math.gcd((pow(a, math.factorial(count), n)) - 1, n)
    while p == 1:
        p = crypto_math.gcd((pow(a, math.factorial(count), n)) - 1, n)
        count += 1
    return int(n / p), int(p)

def shanks_square_forms(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return int(math.sqrt(n)),int(math.sqrt(n))
    k = 1
    while True:
        #creates lists that hold all the updated values
        p = []
        p.append(math.floor(math.sqrt(k * n)))
        q = []
        q.append(1)
        q.append(k * n - math.pow(p[0], 2))
        b = ['']
        i = 1
        #updates all the lists according to the index i. this is the forward cycle
        while math.sqrt(q[i]) != math.ceil(math.sqrt(q[i])) and i % 2 != 0:
            b.append(math.floor((p[0] + p[i - 1]) / q[i]))
            p.append(math.floor(b[i] * q[i] - p[i - 1]))
            q.append(int(q[i - 1] + b[i] * (p[i - 1] - p[i])))
            i += 1
        b = []
        b.append((p[0]-p[i-1])/math.sqrt(q[i]))
        p_i_1 = p[i-1]
        p.append(b[0]*math.sqrt(q[i])+p_i_1)
        q_i = q[i]
        q = []
        q.append(math.sqrt(q_i))
        q.append((k*n-math.pow(p[0],2))/q[0])
        i = 1
        #updates the list in the backward cycle
        while p[i] == p[i-1]:
            b.append(int((p[0]+p[i-1])/q[i]))
            p.append(b[i]*q[i]-p[i-1])
            q.append(q[i-1] + b[i]*(p[i-1]-p[i]))
            i += 1
        f = crypto_math.gcd(n,p[i])
        #if the gcd of n and last iteration of p is not n or 1 then it is a factor
        if f != n and f != 1:
            return f,int(n/f)
        else:
            k += 1

