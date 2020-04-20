# Mastermind

# AndrewId: jkdarwis

import random
from pandas.core.common import flatten

from numpy import loadtxt
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import keras.callbacks

class Game():
    allModels = []

    def __init__(self):
        self.white = 0
        self.black = 0
        self.colors = [1, 2, 3, 4, 5, 6]
        for i in range(1, 5):
            self.allModels.append(load_model('model.' + str(i) + '.hdf5'))
            # print(self.allModels[i - 1].summary())

    # generating a random code
    def generateRandomBoard(self):
        code = list()
        for i in range(4):
            code.append(random.choice(self.colors))
        return code

    # calculate the score of the guess
    def scoreBoard(self, referenceBoard, guessBoard):
        rb = referenceBoard[:]
        gb = guessBoard[:]
        self.black = 0
        self.white = 0

        # calculate black
        for i in range(4):
            if rb[i] == gb[i]:
                self.black += 1
                rb[i] = 0
                gb[i] = 0

        # calculate white
        for i in range(4):
            if gb[i] != 0 and gb[i] in rb:
                self.white += 1
                index = rb.index(gb[i])
                rb[index] = 0
        return self.black, self.white

    # convert numerical code to one hot code
    def convertToOneHot(self, list):
        outputCode = []

        # check each num
        for num in list:
            if num == 1:
                outputCode.append([1, 0, 0, 0, 0, 0])
            elif num == 2:
                outputCode.append([0, 1, 0, 0, 0, 0])
            elif num == 3:
                outputCode.append([0, 0, 1, 0, 0, 0])
            elif num == 4:
                outputCode.append([0, 0, 0, 1, 0, 0])
            elif num == 5:
                outputCode.append([0, 0, 0, 0, 1, 0])
            elif num == 6:
                outputCode.append([0, 0, 0, 0, 0, 1])
        return outputCode

    # decode one hot to numbers
    def convertOneHotToNums(self, list):
        outputList = []
        # convert each list of codes
        for num in list:
            if num == [1, 0, 0, 0, 0, 0]:
                outputList.append(1)
            elif num == [0, 1, 0, 0, 0, 0]:
                outputList.append(2)
            elif num == [0, 0, 1, 0, 0, 0]:
                outputList.append(3)
            elif num == [0, 0, 0, 1, 0, 0]:
                outputList.append(4)
            elif num == [0, 0, 0, 0, 1, 0]:
                outputList.append(5)
            elif num == [0, 0, 0, 0, 0, 1]:
                outputList.append(6)
        return outputList

    # play in code breaker mode
    def codeBreaker(self):
        turns = 0
        referenceBoard = self.generateRandomBoard()
        while turns != 9: # max 8 attempts

            # enter new guess
            guess = list()
            for i in range(4):
                guess.append(str(input("enter your guess")))

            # win condition
            if referenceBoard == guess:
                print('You Win :)')
                break
            else:
                score = self.scoreBoard(referenceBoard, guess)
                print('You have ' + str(score[0]) + ' right guesses in the correct position')
                print('You have ' + str(score[1]) + ' right guesses in an incorrect position')
                turns += 1
        print('you exceeded number of tries')

    def predictNextGuess(self, currentGuess, blackWhite):
        if len(currentGuess) == 0:
            return [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
        ModelID = len(currentGuess) - 1
        x = []
        startingPoint = 0
        if len(currentGuess) > 4:
            startingPoint = len(currentGuess) - 4
            ModelID = 3
        baseItems = []
        for i in range(startingPoint, len(currentGuess)):
            baseItems.append(list(flatten(self.convertToOneHot(currentGuess[i]))) + list(flatten(blackWhite[i])))
        x = list(flatten(baseItems))
        y = self.allModels[ModelID].predict(numpy.asarray([x]))
        output = numpy.array(y).tolist()
        newGuess = []
        for i in range(4):
            tmp = output[0][6 * i : 6 * i + 6]
            newTmp = []
            for t in tmp:
                if t < max(tmp):
                    newTmp.append(0)
                else:
                    newTmp.append(1)
            newGuess.append(newTmp)
        return newGuess


    def codeMaker(self):
        guess = [1, 1, 2, 2]
        seenBefore = []
        blackWhiteScores = []
        seenBefore.append(guess)
        playersCode = list()
        for i in range(4):
            playersCode.append(input('enter your code: '))

        print('my first guess is: ' + str(guess))
        while guess != playersCode:
            black = int(input('num of right colors in the correct position: '))
            white = int(input('num of right colors in the wrong position: '))
            blackWhiteScores.append([black, white])
            guess = self.predictNextGuess(seenBefore, blackWhiteScores)
            guess = self.convertOneHotToNums(guess)
            seenBefore.append(guess)
            print('my next guess is: ' + str(guess))




# def genAllPossibleCombinations():
#     output = list()
#     for i in range(1,7):
#         for j in range(1,7):
#             for k in range(1,7):
#                 for l in range(1,7):
#                     o = [i,j,k,l]
#                     output.append(o)
#     # return a list of all combinations
#     return output
# play = BasicGame()
# allCodes = genAllPossibleCombinations()
#
# correctlyFound = 0
# for code in allCodes:
#     print('==============================')
#     BlackWhite = []
#     seenBefore = []
#     guess = [1, 1, 2, 2]
#     black = 0
#     white = 0
#     for i in range(4):
#         seenBefore.append(guess)
#         (black, white) = play.scoreBoard(code, guess)
#         BlackWhite.append([black, white])
#
#         if black == 4:
#             correctlyFound += 1
#             print(guess, BlackWhite[i])
#             break
#         guess = play.convertOneHotToNums(play.predictNextGuess(seenBefore, BlackWhite))
#     if black != 4:
#         (black, white) = play.scoreBoard(code, guess)
#         if black == 4:
#             correctlyFound += 1
#             print(guess, [black, white])
#
# print(100 * correctlyFound/1296)


#
# play = Game()
# play.codeMaker()
# allModels = []
# guess = [1, 1, 2, 2]
# for i in range(1, 5):
#     p = ML()
#     p.loadModel('model.' + str(i) + '.hdf5')
#     allModels.append(p)
# play.codeMaker()
# play.codeBreaker()

class trainModel(Game):

    # convert numerical code to one hot code
    def convertToOneHot(self, list):
        outputCode = []

        # check each num
        for num in list:
            if num == 1:
                outputCode.append([1, 0, 0, 0, 0, 0])
            elif num == 2:
                outputCode.append([0, 1, 0, 0, 0, 0])
            elif num == 3:
                outputCode.append([0, 0, 1, 0, 0, 0])
            elif num == 4:
                outputCode.append([0, 0, 0, 1, 0, 0])
            elif num == 5:
                outputCode.append([0, 0, 0, 0, 1, 0])
            elif num == 6:
                outputCode.append([0, 0, 0, 0, 0, 1])
        return outputCode

    # decode one hot to numbers
    def convertOneHotToNums(self, list):
        outputList = list()

        # convert each list of codes
        for num in list:
            if num == [1, 0, 0, 0, 0, 0]:
                outputList.append(1)
            elif num == [0, 1, 0, 0, 0, 0]:
                outputList.append(2)
            elif num == [0, 0, 1, 0, 0, 0]:
                outputList.append(3)
            elif num == [0, 0, 0, 1, 0, 0]:
                outputList.append(4)
            elif num == [0, 0, 0, 0, 1, 0]:
                outputList.append(5)
            elif num == [0, 0, 0, 0, 0, 1]:
                outputList.append(6)
        return outputList

    # create training data
    def createTrainingData(self, inputFile):
        inputFile = open(inputFile, mode='r')
        outputFiles = []
        for i in range(4):
            outputFiles.append(open('trainingData' + str(i + 1) + '.csv', mode='w'))


        # go through each line of the file
        for line in inputFile:
            eachLine = line.split('\t')
            hiddenCode = eachLine[len(eachLine) - 1]
            hiddenCode = list(map(int, hiddenCode.strip().split(',')))

            # create files in order
            for i in range(len(eachLine) - 1):
                outputLine = ''
                for code in eachLine[0: i + 1]:
                    code = list(map(int, code.strip().split(',')))

                    # calculate score of guess
                    noBlack, noWhite = self.scoreBoard(hiddenCode, code)

                    # add to file as one hot
                    if len(outputLine) > 0:
                        outputLine += ','
                    temp = list(map(str, flatten(self.convertToOneHot(code))))
                    outputLine += ','.join(temp) + ',' + str(noBlack) + ',' + str(noWhite)
                n = list(map(int, eachLine[i + 1].strip().split(',')))
                new = list(map(str, flatten(self.convertToOneHot(n))))
                outputLine += ',' + ','.join(new)
                outputFiles[i].write(outputLine + '\n')

        inputFile.close()
        for file in outputFiles:
            file.close()


    # creates neural network according to inputs
    def createModel(self, filename, numOfEpochs):

        # load examples file
        dataset = loadtxt(filename, delimiter=',')

        # split into input(x) and output(y) variables
        vecLen = len(dataset[0]) - 24

        X = dataset[:, 0:vecLen]
        Y = dataset[:, vecLen:]

        # define the model
        model = Sequential()
        model.add(Dense(2 * vecLen, input_dim=vecLen, activation='relu'))
        model.add(Dense(vecLen, activation='relu'))
        model.add(Dense(96, activation='relu'))
        model.add(Dense(48, activation='relu'))
        model.add(Dense(48, activation='relu'))
        model.add(Dense(24, activation='softmax'))

        # compile the model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

        # fit the model on the examples
        model.fit(X, Y, epochs=numOfEpochs, batch_size=2, callbacks=[callback])

        # evaluate the model
        _, accuracy = model.evaluate(X, Y)
        print('Accuracy: %.2f' % (accuracy * 100))
        return model

    # save model
    def saveModel(self, filename, model):
        # creates a HDF5 file
        model.save(filename)



# gameModel = trainModel()
# # # gameModel.createTrainingData('all-possible-solutions.txt')
# for k in range(1,5):
#     m = gameModel.createModel('trainingData' + str(k) + '.csv', 100)
#     gameModel.saveModel('model.' + str(k) + '.hdf5' , m)


class ML(trainModel):
    model = Sequential()

    # load model
    def loadModel(self, filename):
        # returns a compiled model identical to previous one
        self.model = load_model(filename)

    # create new set to be used for predictions
    def predictScore(self, hiddenBoard, currentGuess, boardSeenBefore):
        bestBoard = list()
        highestScore = 0

        # base elements based on history
        startingPoint = 0
        if len(boardSeenBefore) > 5:
            startingPoint = len(boardSeenBefore) - 5
        baseitems = []
        for i in range(startingPoint, len(boardSeenBefore)):
            baseitems += boardSeenBefore[i] + list(self.scoreBoard(hiddenBoard, boardSeenBefore[i]))

        # guess score for all possible boards
        for board in self.genAllPossibleCombinations():
            if board not in boardSeenBefore:
                input = list()
                input = baseitems + board

                inputArray = [input]
                yOut = self.model.predict(numpy.asarray(inputArray))

                # find combination with highest score
                if highestScore < yOut.item(0) + 4 * yOut.item(1):
                    highestScore = yOut.item(0) + 4 * yOut.item(1)
                    bestBoard = board[:]
        return bestBoard

    # generates all possible code combinations
    def genAllPossibleCombinations(self):
        output = list()
        for i in range(3,9):
            for j in range(3,9):
                for k in range(3,9):
                    for l in range(3,9):
                        o = [i,j,k,l]
                        output.append(o)
        # return a list of all combinations
        return output















