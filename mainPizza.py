import sys, os
from processing.classes import *
from processing.functions import *
import random

# VARIABLES
file = sys.argv[1]
rules = createRules(file)

# MAIN
cont = 0
if __name__ == "__main__":
    countMaxCell=0
    pizza = parse_file(file)
    printPizza(pizza)
    possible_slices = calculateStandardSlices(rules.max_cells)
    divisors = createMap(pizza,rules)
    possibleSliceMap = saveAllPossibleSlices(rules,divisors,possible_slices) 
    totalCells=(rules.rows * rules.cols)

    while countMaxCell < totalCells:
        bitmap = bitmapp(rules)
        random.shuffle(possibleSliceMap)
        possibleSliceMap = sorted(possibleSliceMap, key=lambda x: (x[0], x[1]))
        pizzaMap = createSliceMap(possibleSliceMap,bitmap)
        countCell=0
        for x in pizzaMap[0]:
            for y in x:
                if y == True:
                    countCell += 1
        
        if countCell>countMaxCell:
            print(str(countCell)+"/"+str(totalCells))
            countMaxCell=countCell
            print("output"+os.sep+file.split(os.sep)[2].split('.')[0]+".out")
            text_file = open("output"+os.sep+file.split(os.sep)[2].split('.')[0]+".out", "w")
            text_file.write(str(len(pizzaMap[1]))+"\n")
            for x in pizzaMap[1]:
                text_file.write(str(x[0])+' '+str(x[1])+' '+str(x[2])+' '+str(x[3])+"\n")
            text_file.close()
