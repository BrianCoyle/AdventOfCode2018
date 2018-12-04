import numpy as np
import os
import collections
def EditElfData():

    with open('Advent_of_Code_day_3_Data.txt') as f:
        with open('Advent_of_Code_day_3_data_edited.txt', "w+") as f2:
            for line in f:
                new_line1 = line.partition(',')[0]
                new_line2 = line.partition(',')[2]
                new_new_line1 = new_line1 + ' ' + new_line2
                # print(new_new_line1)
                new_line3 = new_new_line1.partition('@')[0]
                new_line4 = new_new_line1.partition('@')[2]
                new_new_line2 = new_line3 + new_line4
                # print(new_new_line2)
                new_line5 = new_new_line2.partition('#')[0]
                new_line6 = new_new_line2.partition('#')[2]
                new_new_line3 = new_line5 + new_line6
                # print(new_new_line3)
                new_line7 = new_new_line3.partition('x')[0]
                new_line8 = new_new_line3.partition('x')[2]
                new_new_line4 = new_line7 + ' ' +new_line8
                # print(new_new_line4)
                new_line9 = new_new_line4.partition(':')[0]
                new_line10 = new_new_line4.partition(':')[2]
                new_new_line5 = new_line9 + new_line10
                print(new_new_line5)
                f2.write(new_new_line5)

    return

def ReadElfData():
    elf_data = np.loadtxt('Advent_of_Code_day_3_data_edited.txt',  dtype = int)

    return elf_data


elf_data = ReadElfData()

number_of_elves =  np.amax(elf_data[:,0])
print(number_of_elves)
width = np.amax(elf_data[:,1])
length =  np.amax(elf_data[:,2])
max_elf_patch_width = np.amax(elf_data[:,3])
max_elf_patch_length = np.amax(elf_data[:,4])

print(width, length, max_elf_patch_length, max_elf_patch_width)

fabric_patch_array = np.zeros((number_of_elves, width + max_elf_patch_width, length + max_elf_patch_length), dtype = int)

for elf in range(0, number_of_elves):
    elf_info = elf_data[elf]
    
    for width in range(elf_info[1],  elf_info[1]+elf_info[3]):
        for height in range(elf_info[2],  elf_info[2]+elf_info[4]):
            fabric_patch_array[elf, height, width] = int(1)

full_array = fabric_patch_array.sum(axis = 0)

print('The number of overlapping elements is:', np.count_nonzero(full_array>=2))
count = {}
new_elf_array = {}

for elf in range(0, number_of_elves):
    # print(elf)
    elf_info = elf_data[elf]
    # new_elf_array[elf] = np.zeros(height- elf_info[2], width- elf_info[1])
    count[elf] = 0
    for width in range(elf_info[1],  elf_info[1]+elf_info[3]):
        for height in range(elf_info[2],  elf_info[2]+elf_info[4]):
            # print(height, width)
            if elf == 15:
                print(full_array[height, width])
            if full_array[height, width] !=1:
                count[elf] += 1 #If there is an element of the elf square not equal to one, it overlaps
                break
            else:
                # Continue if the inner loop wasn't broken.
                continue
            # Inner loop was broken, break the outer.
            break  
# print(new_elf_array[14])
print(count
print('The elf which has no overlap is elf, ', list(count.values())[0])