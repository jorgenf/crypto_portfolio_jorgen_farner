import math
import random

#predefined s-boxes
s_1 = [5, 2, 1, 6, 3, 4, 7, 0], [1, 4, 6, 2, 0, 7, 5, 3]
s_2 = [4, 0, 6, 5, 7, 1, 3, 2], [5, 3, 0, 7, 6, 2, 1, 4]

#checks input and runs the feistel network
def encrypt(input_12, key_9,rounds):
    if isinstance(input_12,str):
        input_12 = int(input_12,2)
    if isinstance(key_9,str):
        key_9 = int(key_9,2)
    input_12 = format(input_12, '#014b')
    return feistel(int(input_12[2:8:], 2), int(input_12[8:14], 2), key_9, 1, rounds)

#recursive feistel network with left and right input. the max round makes sure not to exceed max
def feistel(l, r, key, round, max_round):
    if round > max_round:
        return format(l, '#08b') + format(r, '#08b')[2:]
    new_r = function(r, get_key(key, round)) ^ l
    round += 1
    return feistel(r, new_r, key, round,max_round)

#main function. xor the expanded input with round key and returns the s-box output
def function(r_6, k_8):
    r = expander(r_6) ^ k_8
    return s_box(r)

#takes 8-bit input and splits into to and gets values from predefined s-box
def s_box(s_8):
    if isinstance(s_8,str):
        s_8 = int(s_8,2)
    s_8 = format(s_8, '#010b')
    first = s_1[int(s_8[2], 2)][int(s_8[3:6:], 2)]
    second = s_2[int(s_8[6])][int(s_8[-3:], 2)]
    return int(format(first, '#05b') + format(second, '#05b')[2:], 2)

#expands a 6bit input into 8bit
def expander(input_6):
    if isinstance(input_6,str):
        input_6 = int(input_6,2)
    input_6 = format(input_6, '#08b')
    output = input_6[0] + input_6[1] + input_6[2] + input_6[3] + input_6[5] + input_6[4] + input_6[5] + input_6[4] + \
             input_6[6] + input_6[7]
    return int(output, 2)

#gets 8 bit key form 9 bit main key. starts at index equal to round and wraps around
def get_key(key, round):
    if isinstance(key,str):
        key = int(key,2)
    return_key = (format(key, '#011b'))[round + 1:round + 9]
    next = 2
    while len(return_key) < 8:
        return_key += format(key, '#011b')[next]
        next += 1
    return int(return_key, 2)

def differential_cryptanalysis():
    #uses example inputs from book and rounds two rounds simultanously
    k = '001001101'
    print("Original key: ",k)
    k_1 = k[1:9] + k[0:1:]
    L1R1 = '000111011011'
    L_1R_1 = '101110011011'
    print("Set of inputs L1R1 and L*1R*1:\n", L1R1,L_1R_1)
    L1R1_2 = '010111011011'
    L_1R_1_2 = '101110011011'
    print("Set of inputs L1R1 and L*1R*1 for second round:\n", L1R1_2, L_1R_1_2)
    #runs the diff analysis with two differenct L1R1s
    L_k_4_1, R_k_4_1 = run_diff_analysis(L1R1,L_1R_1,k_1)
    print("Key candidates for left and right 4 bits of K4 from first round:\n",L_k_4_1,R_k_4_1)
    #the second round
    L_k_4_2, R_k_4_2 = run_diff_analysis(L1R1_2,L_1R_1_2,k_1)
    print("Key candidates for left and right 4 bits of K4 from second round:\n", L_k_4_2, R_k_4_2)
    #checks what sets are equal from round 1 and 2 for left bits
    L_k_4 = set(L_k_4_1).intersection(L_k_4_2)
    print("Correct left bits of K4: ",L_k_4)
    #checks what sets are equal from round 1 and 2 for right bits
    R_k_4 = set(R_k_4_1).intersection(R_k_4_2)
    print("Correct right bits of K4: ", R_k_4)
    #fourth round key
    k_4 = str(L_k_4)[4:8:] + str(R_k_4)[4:8:]
    #tries 0 and 1 for the third bit which is unknown and whichever gives correct encryption is chosen
    k_guess_1 = k_4[6:8:] + '0' + k_4[0:6:]
    k_guess_2 = k_4[6:8:] + '1' + k_4[0:6:]
    if encrypt(L1R1,k_guess_1,3) == encrypt(L1R1,k,3):
        print("Key: ",k_guess_1)
        return k_guess_1
    if encrypt(L1R1,k_guess_2,3) == encrypt(L1R1,k,3):
        print("Key: ",k_guess_2)
        return k_guess_2

def run_diff_analysis(L1R1, L_1R_1,k):
    #gets the 3 round encryption
    L4R4 = encrypt(L1R1,k,3)
    L_4R_4 = encrypt(L_1R_1,k,3)
    #expands the output
    E_L4=expander(L4R4[2:8:])
    E_L_4=expander(L_4R_4[2:8:])
    #xor the two expansions
    XORE_L4E_L_4 = E_L4 ^ E_L_4
    #xors the right 6 bits of the two L4R4
    diff_R4 = format(int(L4R4,2) ^ int(L_4R_4,2), '014b')[8:14:]
    #xors left 6 bits of the two L1R1's
    diff_L1 = format(int(L1R1,2) ^ int(L_1R_1,2), '014b')[2:8:]
    #these are xored
    diff_XOR_R_4L_1 = format(int(diff_R4,2) ^ int(diff_L1,2),'#08b')
    L_K_4 = []
    R_K_4 = []
    #tries all 4 bit combinations for xor of s1 and s2 outputs and check if they equal the inputs
    for i in range(0,15):
        for j in range(0,15):
            s_1 = format(s_box(i<<4) ^ s_box(j<<4), '#08b')[2:5]
            s_2 = format(s_box(i) ^ s_box(j), '#08b')[5:8]
            if s_1 == diff_XOR_R_4L_1[2:5:] and i^j == int(format(XORE_L4E_L_4,'#010b')[2:6:],2):
                L_K_4.append(format(i^int(format(E_L4,'#010b')[2:6:],2),'#06b'))
            if s_2 == diff_XOR_R_4L_1[5:8:] and i^j == int(format(XORE_L4E_L_4,'#010b')[6:10:],2):
                R_K_4.append(format(i^int(format(E_L4,'#010b')[6:10:],2),'#06b'))
    return L_K_4, R_K_4
