import numpy as np
import collections
def LoadFrequencyChanges():
    frequency_changes = list(np.loadtxt('Advent_of_Code_day_1_data', dtype = int))

    return frequency_changes
    
def ComputeFreqChanges():

    frequency_changes = LoadFrequencyChanges()
    frequency = 0

    for new_freq in frequency_changes:
        frequency = frequency + new_freq

    return frequency


# frequency = ComputeFreqChanges()

# print('The new frequency is:', frequency)

def FindDuplicateFreq():
    frequency_changes = LoadFrequencyChanges()

    new_frequency_set= set()
    # new_frequency_set.append(0)

    running_frequency = 0
    repeated_value = None
    while repeated_value is None:
        for new_freq in frequency_changes:
            # print('The previous value in the list is:', new_frequency_set[-1])
            running_frequency = running_frequency + new_freq
            if running_frequency in new_frequency_set:
                repeated_value = running_frequency
                new_frequency_set.add(repeated_value)
                break
            new_frequency_set.add(running_frequency)
            # print(new_frequency_list)

            # print('The newest value in the list is:', new_frequency_list[-1] )
            # print(len(new_frequency_set))
    return repeated_value, new_frequency_set

repeated_value, new_frequency_set = FindDuplicateFreq()
print('The repeated frequency is:', repeated_value)
# print(collections.Counter(new_frequency_list))        
# print(sorted(new_frequency_set))        

# for new_freq in frequency_changes:
#     print('The previous value in the list is:', new_frequency_list[-1])
#     running_frequency = running_frequency + new_freq
#     if running_frequency in new_frequency_list:
#         repeated_value = running_frequency
#         break
#     new_frequency_list.append(new_frequency_list[-1] + new_freq)
# for new_freq in frequency_changes:
#     print('The previous value in the list is:', new_frequency_list[-1])
#     running_frequency = running_frequency + new_freq
#     if running_frequency in new_frequency_list:
#         repeated_value = running_frequency
#         break
#     new_frequency_list.append(new_frequency_list[-1] + new_freq)
# for new_freq in frequency_changes:
#     print('The previous value in the list is:', new_frequency_list[-1])
#     running_frequency = running_frequency + new_freq
#     if running_frequency in new_frequency_list:
#         repeated_value = running_frequency
#         break
#     new_frequency_list.append(new_frequency_list[-1] + new_freq)
#     # print(new_frequency_list)
# for new_freq in frequency_changes:
#     print('The previous value in the list is:', new_frequency_list[-1])
#     running_frequency = running_frequency + new_freq
#     if running_frequency in new_frequency_list:
#         repeated_value = running_frequency
#         break
#     new_frequency_list.append(new_frequency_list[-1] + new_freq)
# for new_freq in frequency_changes:
#     print('The previous value in the list is:', new_frequency_list[-1])
#     running_frequency = running_frequency + new_freq
#     if running_frequency in new_frequency_list:
#         repeated_value = running_frequency
#         break
#     new_frequency_list.append(running_frequency)