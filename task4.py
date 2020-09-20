import numpy as np
import random
import os


def readFile(fileName):
    filehandle = open(fileName)
    file = filehandle.read()
    mass = file.split("\n")
    twoDimMass = []
    for i in range(0, len(mass)):
        temp = mass[i].split(" ")
        temp1 = []
        for j in range(0, len(temp)):
            temp1.append(int(temp[j]))
        twoDimMass.append(temp1)
    filehandle.close()
    return twoDimMass


def task3():
    twoDimensionalArray = readFile('input1.txt')
    sum = twoDimensionalArray[0][0]
    step = Step(0, 0)
    move = Move
    array = []
    while len(twoDimensionalArray) != step.x + 1 or len(twoDimensionalArray[0]) != step.y + 1:
        step = move.doStep(twoDimensionalArray, step)
        array.append(step)
    for item in array:
        sum += twoDimensionalArray[item.x][item.y]
    print("Sum: " + str(sum))


class Move:
    def doStep(twoDimensionalArray, step):
        sumDown = goDown(twoDimensionalArray, step)
        sumRight = goRight(twoDimensionalArray, step)
        if sumDown > sumRight:
            return Step(step.x + 1, step.y)
        elif sumDown < sumRight:
            return Step(step.x, step.y + 1)
        elif sumRight == sumRight and sumRight > 0:
            return Step(step.x, step.y + 1)
        else:
            return Step(step.x, step.y)


def goDown(twoDimensionalArray, step):
    if len(twoDimensionalArray) > step.x + 1:
        return twoDimensionalArray[step.x + 1][step.y]
    else:
        return 0


def goRight(twoDimensionalArray, step):
    if len(twoDimensionalArray[step.x]) > step.y + 1:
        return twoDimensionalArray[step.x][step.y + 1]
    else:
        return 0


class Step:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getXposition(self):
        return self.x

    def getYposition(self):
        return self.y

    def setXposition(self, x):
        self.x = x

    def setYposition(self, y):
        self.y = y


if __name__ == '__main__':
    task3()
