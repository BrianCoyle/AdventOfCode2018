import numpy as np
import collections


def LoadElfInfo():
    elf_info = np.loadtxt('Advent_of_Code_day_3_data', comments=[''])
    # dtype={'names': ('elf_no', '@', 'firs_index', 'second_index','stuff', 'stuff2') ,'formats': (str, str, str, str, str, str, str)})
#1 @ 185,501: 17x15
    return elf_info

elf_info = LoadElfInfo()
