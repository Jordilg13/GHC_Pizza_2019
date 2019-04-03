from processing.classes import *

def parse_file(file):
    f = open(file, 'r')
    parsed_array = []

    for row in f.readlines():
        parsed_array.append(row.replace("\n", "").split(" "))
    f.close()

    # delete rules line
    parsed_array.pop(0)
    return parsed_array


def createRules(file):
    f = open(file, 'r')
    rules = Rules(f.readline())
    f.close()
    return rules


def calculateStandardSlices(max_cells):
    array_possible_slices = []

    for i in range(1, max_cells):
        for j in range(1, max_cells):
            if i*j <= max_cells:
                array_possible_slices.append([i, j])

    # delete [1,1]
    array_possible_slices.pop(0)
    return array_possible_slices


def createMap(pizza, rules):
    map = []
    for row in range(rules.rows):
        map.append([])
        for cell in range(rules.cols):
            map[row].append(pizza[row][0][cell])
    return map

def cutSlice(x, y, pos, mapp, rules):
    countT=0
    countM=0
    x2=0
    y2=0
    for i in range(pos[0]):
        for j in range(pos[1]):
            try:
                if mapp[x+i][y+j]=="T":
                    countT += 1
                elif mapp[x+i][y+j]=="M":
                    countM += 1
                x2=x+i
                y2=y+j
            except:
                pass    
    if countT >= rules.min_ingredients and countM >= rules.min_ingredients:
        return [x,y,x2,y2]
    else:
        return False
    

def saveAllPossibleSlices(rules, mapp, pos_slices):
    possibleSlices = []
    for row in range(rules.rows):
        for col in range(rules.cols):
            for pos in range(len(pos_slices)):
                newSlice = cutSlice(row, col, pos_slices[pos], mapp,rules)
                if newSlice:
                    possibleSlices.append(newSlice)

    return possibleSlices 

def printPizza(pizza):
    print()
    for i in pizza:
        print(" "+i[0])
    print()

def createSliceMap(possibleSliceMap, bitmap):
    pizzaSliceMap = []
    countSlice=0
    for thisSlice in possibleSliceMap:
        if bitmap[thisSlice[0]][thisSlice[1]] == False:
            addedSlice=addSliceToPizza(thisSlice,bitmap)
            bitmap=addedSlice[0]
            sliceAdded=addedSlice[1]
            if sliceAdded:
                pizzaSliceMap.append(thisSlice)

    return [bitmap,pizzaSliceMap]

def addSliceToPizza(sliceA,pizza):
    success=False
    mapA=[]
    for row in range(sliceA[0],sliceA[2]+1):
        for col in range(sliceA[1],sliceA[3]+1):
            mapA.append([row,col])
            
    for cell in mapA:
        try:
            if pizza[cell[0]][cell[1]] == False:
                success=True
            else:
                success=False 
                break             
        except:
            success=False
            break
    if success:
        for cell in mapA:
            pizza[cell[0]][cell[1]] = True
    return [pizza,success]


def bitmapp(rules): # esto tarda menos de 0.1s en el de 1000x1000
    bitmap = []
    for i in range(rules.rows):
        bitmap.append([])
        for j in range(rules.cols):
            bitmap[i].append(False)
    return bitmap