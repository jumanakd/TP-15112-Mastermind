import pygame
from game import *
from helperFunctions import *

from tkinter import *
from tkinter import messagebox

class interface():
    # initialize everything
    def __init__(self):
        self.board = pygame.image.load('Board.png')
        self.redPeg = pygame.image.load('redPeg.png')
        self.greenPeg = pygame.image.load('greenPeg.png')
        self.bluePeg = pygame.image.load('bluePeg.png')
        self.yellowPeg = pygame.image.load('yellowPeg.png')
        self.purplePeg = pygame.image.load('purplePeg.png')
        self.orangePeg = pygame.image.load('orangePeg.png')
        self.blackPeg = pygame.image.load('blackPeg.png')
        self.whitePeg = pygame.image.load('whitePeg.png')
        self.redBorder = pygame.image.load('redBorder.png')
        self.won = pygame.image.load('win.png')
        self.lost = pygame.image.load('loss.png')
        self.menu = pygame.image.load('mainmenu.png')
        self.scoringBoard = pygame.image.load('AIboard.png')
        self.wonAI = pygame.image.load('winAI.png')
        self.lostAI = pygame.image.load('lossAI.png')
        self.info = pygame.image.load('info.png')
        self.inputBoard = pygame.image.load('inputBoard.png')
        self.colors = [self.redPeg, self.greenPeg, self.bluePeg,
                       self.yellowPeg, self.purplePeg, self.orangePeg]
        self.red = False
        self.green = False
        self.blue = False
        self.yellow = False
        self.purple = False
        self.orange = False
        self.white = False
        self.black = False
        self.drag = False
        self.check = False
        self.openmenu = True
        self.infoMenu = False
        self.codeBreakerPressed = False
        self.codeSetterPressed = False
        self.codeSet = False
        self.selectedPeg = self.redPeg
        self.imagesToDisplay = list()
        self.rowCount = 0
        self.blackCount, self.whiteCount = 0, 0
        self.guess = [0, 0, 0, 0]
        self.guessCode = [0, 0, 0, 0]
        self.score = [0, 0]
        self.setCode = [0, 0, 0, 0]
        self.playersCode = [0, 0, 0, 0]
        self.hiddenCode = generateRandomBoard()
        self.nextBoard = []
        self.seenBefore = []
        self.blackWhite = []
        self.guessGame = Game()

    def uploadBoard(self):
        window.blit(self.board, (0, 0))
        # track row pos
        if self.score[0] != 4 and self.rowCount != 10:
            window.blit(self.redBorder, (25, 537 - (self.rowCount * 50)))

        # update placed pegs
        for peg in self.imagesToDisplay:
            window.blit(peg[0], (peg[1], peg[2]))

    # drag and drop pegs
    def movePegs(self, x, y):
        offset = 20
        for event in pygame.event.get():
            # check if player pressed on peg
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # red
                if x > 17 and x < 53 and y > 620 and y < 660:
                    self.red = True
                    self.drag = True
                    self.selectedPeg = self.redPeg
                # green
                elif x > 58 and x < 93 and y > 620 and y < 660:
                    self.green = True
                    self.drag = True
                    self.selectedPeg = self.greenPeg
                # blue
                elif x > 97 and x < 132 and y > 620 and y < 660:
                    self.blue = True
                    self.drag = True
                    self.selectedPeg = self.bluePeg
                # yellow
                elif x > 137 and x < 171 and y > 620 and y < 660:
                    self.yellow = True
                    self.drag = True
                    self.selectedPeg = self.yellowPeg
                # purple
                elif x > 177 and x < 212 and y > 620 and y < 660:
                    self.purple = True
                    self.drag = True
                    self.selectedPeg = self.purplePeg
                # orange
                elif x > 215 and x < 250 and y > 620 and y < 660:
                    self.orange = True
                    self.drag = True
                    self.selectedPeg = self.orangePeg
                # check score
                elif x > 262 and x < 318 and y > 612 and y < 669 and self.checkIfRowFilled() == True:
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    self.check = True
                    self.getCode()
                    self.score = self.getScore()
                    self.rowCount += 1
                    self.guess = [0, 0, 0, 0]
                    self.placeScorePegs()
                    self.checkWinOrLoss()

            # place peg when mouse released
            elif event.type == pygame.MOUSEBUTTONUP:
                self.red = False
                self.green = False
                self.blue = False
                self.yellow = False
                self.purple = False
                self.orange = False

                # center the pegs
                if x > 32 and x < 180 and y > 545 - (50 * self.rowCount ) and y < 581 - (50 * self.rowCount):
                    if self.drag == True:
                        if x > 32 and x < 66:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.guess[0] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 30, 542 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 70 and x < 104:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.guess[1] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 68, 542 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 109 and x < 143:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.guess[2] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 106, 542 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 148 and x < 180:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.guess[3] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 144, 542 - (50 * self.rowCount)])
                            self.drag = False

        # move peg around when clicked
        if self.red:
            window.blit(self.redPeg, (x - offset, y - offset))
        elif self.green:
            window.blit(self.greenPeg, (x - offset, y - offset))
        elif self.blue:
            window.blit(self.bluePeg, (x - offset, y - offset))
        elif self.yellow:
            window.blit(self.yellowPeg, (x - offset, y - offset))
        elif self.purple:
            window.blit(self.purplePeg, (x - offset, y - offset))
        elif self.orange:
            window.blit(self.orangePeg, (x - offset, y - offset))

    # translate pegs
    def getCode(self):
        for i in range(4):
            self.guessCode[i] = self.colors.index(self.guess[i]) + 1

    # get score of guess
    def getScore(self):
        return scoreBoard(self.hiddenCode, self.guessCode)

    # add the score pegs
    def placeScorePegs(self):
        if self.check == True:

            # add black pegs
            if self.score[0] > 0:
                for i in range(self.score[0]):
                    self.imagesToDisplay.append([self.blackPeg, (i * 28) + 195, 548 - (50 * (self.rowCount - 1))])

            # add white pegs
            if self.score[1] > 0:
                for i in range(self.score[1]):
                    self.imagesToDisplay.append(
                        [self.whitePeg, (i * 28) + 195 + (self.score[0] * 28), 548 - (50 * (self.rowCount - 1))])

            if self.score[0] != 4:
                self.score[0], self.score[1] = 0, 0
                self.guessCode = [0, 0, 0, 0]

    # check if row if full
    def checkIfRowFilled(self):

        # if row not full output an error
        if 0 in self.guess:
            pygame.mixer.music.load('oops.wav')
            pygame.mixer.music.play()
            Tk().wm_withdraw()
            messagebox.showinfo('Oops!', 'Please enter a full guess')
            return False
        else:
            return True

    # check win or loss condition
    def checkWinOrLoss(self):

        # winning condition
        if self.score[0] == 4:
            pygame.mixer.music.load('tada.wav')
            pygame.mixer.music.play()
            self.imagesToDisplay.append([self.won, 23, 230])
            for i in range(4):
                self.imagesToDisplay.append([self.colors[self.hiddenCode[i] - 1], (40 * i) + 30, 30])

        # losing condition
        if self.rowCount == 10 and self.score[0] != 4:
            pygame.mixer.music.load('lose.wav')
            pygame.mixer.music.play()
            self.imagesToDisplay.append([self.lost, 20, 230])
            for i in range(4):
                self.imagesToDisplay.append([self.colors[self.hiddenCode[i] - 1], (40 * i) + 30, 30])

    def mainMenu(self, x, y):
        # keep menu open
        window.blit(self.menu, (0, 0))
        while self.openmenu:
            x, y = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    #  if code breaker is clicked
                    if x > 105 and x < 230 and y > 380 and y < 505:
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        self.codeBreakerPressed = True
                        self.openmenu = False

                    # if code setter is clicked
                    elif x > 105 and x < 230 and y > 520 and y < 645:
                        pygame.mixer.music.load('click.wav')
                        pygame.mixer.music.play()
                        self.codeSetterPressed = True
                        self.openmenu = False

                    # if info button is clicked
                    elif x > 19 and x < 58 and y > 640 and y < 680:
                        self.infoMenu = not self.infoMenu
                        if self.infoMenu:
                            window.blit(self.info, (3, 100))
                        elif not self.infoMenu:
                            window.blit(self.menu, (0, 0))
            pygame.display.update()

    # code breaker mode
    def codeBreaker(self, x, y):
        self.uploadBoard()
        if self.score[0] != 4:
            self.movePegs(x, y)

    # let user enter his code
    def setCodeAI(self, x, y):

        window.blit(self.inputBoard, (0, 0))

        for peg in self.imagesToDisplay:
            window.blit(peg[0], (peg[1], peg[2]))

        offset = 20
        for event in pygame.event.get():
            # check if player pressed on peg
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # red
                if x > 17 and x < 53 and y > 620 and y < 660:
                    self.red = True
                    self.drag = True
                    self.selectedPeg = self.redPeg
                # green
                elif x > 58 and x < 93 and y > 620 and y < 660:
                    self.green = True
                    self.drag = True
                    self.selectedPeg = self.greenPeg
                # blue
                elif x > 97 and x < 132 and y > 620 and y < 660:
                    self.blue = True
                    self.drag = True
                    self.selectedPeg = self.bluePeg
                # yellow
                elif x > 137 and x < 171 and y > 620 and y < 660:
                    self.yellow = True
                    self.drag = True
                    self.selectedPeg = self.yellowPeg
                # purple
                elif x > 177 and x < 212 and y > 620 and y < 660:
                    self.purple = True
                    self.drag = True
                    self.selectedPeg = self.purplePeg
                # orange
                elif x > 215 and x < 250 and y > 620 and y < 660:
                    self.orange = True
                    self.drag = True
                    self.selectedPeg = self.orangePeg
                # check score
                elif x > 262 and x < 318 and y > 612 and y < 669 and self.validateInput() == True:
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    self.check = True
                    self.codeSet = True
                    self.addGuesses()
                    self.getPlayersCode()

            # place peg when mouse released
            elif event.type == pygame.MOUSEBUTTONUP:
                self.red = False
                self.green = False
                self.blue = False
                self.yellow = False
                self.purple = False
                self.orange = False

                # center pegs
                if x > 32 and x < 180 and y > 34 and y < 67:
                    if self.drag == True:
                        if x > 32 and x < 66:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.setCode[0] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 30, 32])
                            self.drag = False
                        elif x > 70 and x < 104:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.setCode[1] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 68, 32])
                            self.drag = False
                        elif x > 109 and x < 143:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.setCode[2] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 106, 32])
                            self.drag = False
                        elif x > 148 and x < 180:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            self.setCode[3] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 144, 32])
                            self.drag = False

        # move peg around when clicked
        if self.red:
            window.blit(self.redPeg, (x - offset, y - offset))
        elif self.green:
            window.blit(self.greenPeg, (x - offset, y - offset))
        elif self.blue:
            window.blit(self.bluePeg, (x - offset, y - offset))
        elif self.yellow:
            window.blit(self.yellowPeg, (x - offset, y - offset))
        elif self.purple:
            window.blit(self.purplePeg, (x - offset, y - offset))
        elif self.orange:
            window.blit(self.orangePeg, (x - offset, y - offset))

    # open scoring bord
    def openScoringBoard(self):
        if self.codeSet == True:
            window.blit(self.scoringBoard, (0, 0))


    # convert players input code
    def getPlayersCode(self):
        for i in range(4):
            self.playersCode[i] = self.colors.index(self.setCode[i]) + 1

    # predict the next guess
    def getNextGuess(self):
        self.nextBoard = self.guessGame.predictNextGuess(self.seenBefore, self.blackWhite)
        self.nextBoard = self.guessGame.convertOneHotToNums(self.nextBoard)
        self.seenBefore.append(self.nextBoard)

    # display predicted guess
    def addGuesses(self):
        self.getNextGuess()
        for i in range(4):
            self.imagesToDisplay.append([self.colors[self.nextBoard[i] - 1], (38 * i) + 30, 542 - (50 * self.rowCount)])

        # reset score
        self.blackCount = 0
        self.whiteCount = 0

    # add scoring pegs
    def placeScorePegsAI(self):
        offset = 10
        for event in pygame.event.get():
            # check if player pressed on peg
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # black
                if x > 133 and x < 155 and y > 630 and y < 650:
                    self.black = True
                    self.drag = True
                    self.selectedPeg = self.blackPeg
                # white
                elif x > 169 and x < 191 and y > 630 and y < 650:
                    self.white = True
                    self.drag = True
                    self.selectedPeg = self.whitePeg
                # display next guess
                elif x > 262 and x < 318 and y > 612 and y < 669 and self.verifyUserScoring() == True:
                    pygame.mixer.music.load('click.wav')
                    pygame.mixer.music.play()
                    self.checkLoss()
                    self.checkWin()
                    self.check = True
                    self.rowCount += 1
                    if self.blackCount != 4:
                        self.blackWhite.append([self.blackCount, self.whiteCount])
                        self.addGuesses()

            # place peg when mouse released
            elif event.type == pygame.MOUSEBUTTONUP:
                self.black = False
                self.white = False

                # center pegs and count black and white
                if x > 199 and x < 305 and y > 552 - (50 * self.rowCount) and y < 574 - (50 * self.rowCount):
                    if self.drag == True:
                        if x > 199 and x < 221:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            if self.selectedPeg == self.blackPeg:
                                self.blackCount += 1
                            elif self.selectedPeg == self.whitePeg:
                                self.whiteCount += 1
                            self.imagesToDisplay.append([self.selectedPeg, 197, 548 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 227 and x < 249:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            if self.selectedPeg == self.blackPeg:
                                self.blackCount += 1
                            elif self.selectedPeg == self.whitePeg:
                                self.whiteCount += 1
                            self.imagesToDisplay.append([self.selectedPeg, 225, 548 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 255 and x < 277:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            if self.selectedPeg == self.blackPeg:
                                self.blackCount += 1
                            elif self.selectedPeg == self.whitePeg:
                                self.whiteCount += 1
                            self.imagesToDisplay.append([self.selectedPeg, 253, 548 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 283 and x < 305:
                            pygame.mixer.music.load('Pop.wav')
                            pygame.mixer.music.play()
                            if self.selectedPeg == self.blackPeg:
                                self.blackCount += 1
                            elif self.selectedPeg == self.whitePeg:
                                self.whiteCount += 1
                            self.imagesToDisplay.append([self.selectedPeg, 280, 548 - (50 * self.rowCount)])
                            self.drag = False

        # move peg around with mouse when clicked
        if self.black:
            window.blit(self.blackPeg, (x - offset, y - offset))
        elif self.white:
            window.blit(self.whitePeg, (x - offset, y - offset))

    # verify the player entered correct score
    def verifyUserScoring(self):
        if scoreBoard(self.playersCode, self.nextBoard) != [self.blackCount, self.whiteCount]:
            pygame.mixer.music.load('oops.wav')
            pygame.mixer.music.play()
            Tk().wm_withdraw()
            messagebox.showinfo('Caught!', 'Make sure you enter the correct score')
            
            # remove wrong score pegs
            sum = self.blackCount + self.whiteCount
            self.imagesToDisplay = self.imagesToDisplay[0:len(self.imagesToDisplay) - sum]
            self.blackCount = 0
            self.whiteCount = 0
            return False
        else:
            return True

    # ensure player entered full code
    def validateInput(self):
        if 0 in self.setCode:
            pygame.mixer.music.load('oops.wav')
            pygame.mixer.music.play()
            Tk().wm_withdraw()
            messagebox.showinfo('Oops!','Please enter a full code')
            return False
        else:
            return True

    # win or loss conditions
    def checkWin(self):
        # if won
        if self.blackCount == 4:
            pygame.mixer.music.load('tada.wav')
            pygame.mixer.music.play(0)
            self.imagesToDisplay.append([self.wonAI, 30, 250])

    def checkLoss(self):
        # if lost
        if self.rowCount == 9:
            pygame.mixer.music.load('lose.wav')
            pygame.mixer.music.play(0)
            self.imagesToDisplay.append([self.lostAI, 20, 220])

    # code setter function
    def codeSetter(self, x, y):
        if self.codeSet == False:
            self.setCodeAI(x, y)
        self.openScoringBoard()
        # display all
        for peg in self.imagesToDisplay:
            window.blit(peg[0], (peg[1], peg[2]))
        if self.rowCount != 10:
            self.placeScorePegsAI()

    # reset game
    def resetGame(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.red = False
            self.green = False
            self.blue = False
            self.yellow = False
            self.purple = False
            self.orange = False
            self.white = False
            self.black = False
            self.drag = False
            self.check = False
            self.openmenu = True
            self.codeBreakerPressed = False
            self.codeSetterPressed = False
            self.codeSet = False
            self.selectedPeg = self.redPeg
            self.imagesToDisplay = list()
            self.rowCount = 0
            self.blackCount, self.whiteCount = 0, 0
            self.guess = [0, 0, 0, 0]
            self.guessCode = [0, 0, 0, 0]
            self.score = [0, 0]
            self.setCode = [0, 0, 0, 0]
            self.playersCode = [0, 0, 0, 0]
            self.hiddenCode = generateRandomBoard()+
            self.nextBoard = []
            self.seenBefore = []
            self.blackWhite = []





pg = interface()
pygame.init() # initializing game

window = pygame.display.set_mode((338, 700)) # game dimensions
pygame.display.set_caption('Mastermind')


run = True
while run: # main loop
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # condition to end
            run = False

    pg.mainMenu(x, y)

    if pg.codeSetterPressed == True:
        pg.codeSetter(x, y)

    if pg.codeBreakerPressed == True:
        pg.codeBreaker(x, y)

    pg.resetGame()
    pygame.display.update()


pygame.quit()