import numpy as np
import collections


def LoadSerialNumbers():
    serial_codes = list(np.loadtxt('Advent_of_Code_day_2_data', dtype = str))

    return serial_codes

def CountLetters(serial_codes):

    letter_counts = {}
    sum_one = 0
    sum_two = 0
    for code in serial_codes:    
        letter_counts[code] = collections.Counter(code)
    
        if 2 in letter_counts[code].values():
            print(code, 'has two letters repeated')
            sum_one += 1 #Everytime a serial code appears which has two letters repeated, increment sum_one
        if 3 in letter_counts[code].values():
            print(code, 'has three letters repeated')
            sum_two += 1 #Everytime a serial code appears which has three letters repeated, increment sum_two

    checksum = sum_one*sum_two #Answer is the product of sum_one and sum_two
    return checksum

serial_codes = LoadSerialNumbers()
# checksum = CountLetters(serial_codes)
# print('The answer to Advent day two is:', checksum)


def CheckStringDifferent(string_one, string_two):
    '''This function checks where two strings are different'''
    # for char in string_one:
    numbered_string_one = [ord(char) - 96 for char in string_one]
    numbered_string_two = [ord(char) - 96 for char in string_two]
    numbered_string_difference = np.abs(np.asarray(numbered_string_one) - np.asarray(numbered_string_two))

    # print(string_one, numbered_string_one)
    # print( numbered_string_difference)

    correct_string_one = None
    correct_string_two = None
    # print(np.count_nonzero(numbered_string_difference))
    # print(number_of_same_elements)
    if np.count_nonzero(numbered_string_difference) == 1:
        print('These two strings differ in exactly 1 places')
        correct_string_one = string_one
        correct_string_two = string_two
    # print(number_of_same_elements)
    return correct_string_one, correct_string_two


def FindSimilarCodes(serial_codes):
    '''This function finds two codes which differ in exactly one place'''
    for code_one in serial_codes:
        for code_two in serial_codes:
            correct_code_one, correct_code_two = CheckStringDifferent(code_one, code_two)
            if correct_code_one is not None and correct_code_two is not None:
                print('The correct codes are:', correct_code_one, correct_code_two)
FindSimilarCodes(serial_codes)
