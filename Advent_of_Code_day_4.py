import numpy as np
import os
import collections
def EditGuardData():

    with open('Advent_of_Code_day_4_data.txt') as f:
        with open('Advent_of_Code_day_4_data_edited.txt', "w+") as f2:
            for line in f:
                new_line1 = line.partition('[')[0]
                new_line2 = line.partition('[')[2]
                new_new_line1 = new_line1  + new_line2
                # print(new_new_line1)
                new_line3 = new_new_line1.partition(']')[0]
                new_line4 = new_new_line1.partition(']')[2]
                new_new_line2 = new_line3 + new_line4
                # print(new_new_line2)
                new_line5 = new_new_line2.partition('-')[0]
                new_line6 = new_new_line2.partition('-')[2]
                new_new_line3 = new_line5 + ' '+ new_line6
                # print(new_new_line3)
                new_line7 = new_new_line3.partition(':')[0]
                new_line8 = new_new_line3.partition(':')[2]
                new_new_line4 = new_line7 + ' ' +new_line8
                # print(new_new_line4)
                new_line9 = new_new_line4.partition(']')[0]
                new_line10 = new_new_line4.partition(']')[2]
                new_new_line5 = new_line9 + new_line10
                new_line11 = new_new_line5.partition('-')[0]
                new_line12 = new_new_line5.partition('-')[2]
                new_new_line6 = new_line11 + ' '+ new_line12
                # print(new_new_line6)
                new_line13 = new_new_line6.partition('#')[0]
                new_line14 = new_new_line6.partition('#')[2]
                new_new_line7 = new_line13 +  new_line14
                # print(new_new_line7)
                if 'Guard' in new_new_line7:
                    new_linea = new_new_line7.partition('Guard')[0]
                    new_lineb = new_new_line7.partition('Guard')[2]
                    new_new_lineA = new_linea + new_lineb
                    new_linec = new_new_lineA.partition('shift')[0]
                    new_lined = new_new_lineA.partition('shift')[2]
                    new_new_lineB = new_linec + new_lined
                    f2.write(new_new_lineB)
                else:
                    f2.write(new_new_line7)


    return

EditGuardData()
def ReadGuardData():
    guard_data = np.loadtxt('Advent_of_Code_day_4_data_edited.txt', dtype = str)

    return guard_data

guard_data = ReadGuardData()
# print(guard_data)
new_gd = guard_data[:,1:]
# print(new_gd)
new_gd.view('i8,i8,i8').sort(order=['f0', 'f1', 'f2'], axis=0)
print(new_gd)
# for guard_data[:, ]