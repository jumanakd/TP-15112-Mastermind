import pygame
# from BasicGame import *
from helperFunctions import *

class interface():

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
        self.won = pygame.image.load('win.png')
        self.lost = pygame.image.load('loss.png')
        self.colors = [self.redPeg, self.greenPeg, self.bluePeg,
                       self.yellowPeg, self.purplePeg, self.orangePeg]
        self.red = False
        self.green = False
        self.blue = False
        self.yellow = False
        self.purple = False
        self.orange = False
        self.drag = False
        self.check = False
        self.selectedPeg = self.redPeg
        self.imagesToDisplay = list()
        self.rowCount = 0
        self.guess = [0, 0, 0, 0]
        self.guessCode = [None, None, None, None]
        self.score = [0 , 0]
        self.hiddenCode = generateRandomBoard()


    def uploadBoard(self):
        window.blit(self.board, (0, 0))

        # update placed pegs
        for peg in self.imagesToDisplay:
            window.blit(peg[0], (peg[1], peg[2]))

    def startScreen(self):
        start = True
        while start == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
            window.fill((255, 255, 255))
            title = pygame.image.load('title.png')
            window.blit(title, (20, 100))
            pygame.display.update()

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
                elif x > 262 and x < 318 and y > 612 and y < 669:
                    self.check = True
                    self.getCode()
                    self.score = self.getScore()
                    self.rowCount += 1

            # place peg when mouse released
            elif event.type == pygame.MOUSEBUTTONUP:
                self.red = False
                self.green = False
                self.blue = False
                self.yellow = False
                self.purple = False
                self.orange = False
                if x > 32 and x < 180 and y > 545 - (50 * self.rowCount ) and y < 581 - (50 * self.rowCount):
                    if self.drag == True:
                        if x > 32 and x < 66:
                            self.guess[0] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 30, 542 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 70 and x < 104:
                            self.guess[1] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 68, 542 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 109 and x < 143:
                            self.guess[2] = self.selectedPeg
                            self.imagesToDisplay.append([self.selectedPeg, 106, 542 - (50 * self.rowCount)])
                            self.drag = False
                        elif x > 148 and x < 180:
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
            if self.score[0] > 0:
                for i in range(self.score[0]):
                    self.imagesToDisplay.append([self.blackPeg, (i * 28) + 195, 548 - (50 * (self.rowCount - 1))])
            if self.score[1] > 0:
                for i in range(self.score[1]):
                    self.imagesToDisplay.append([self.whitePeg, (i * 28) + 195 + (self.score[0] * 28), 548 - (50 * (self.rowCount - 1))])
            if self.score[0] != 4:
                self.score[0], self.score[1] = 0, 0
                self.guessCode = [0, 0, 0, 0]

    # check win or loss condition
    def checkWinOrLoss(self):
        if self.score[0] == 4:
            self.imagesToDisplay.append([self.won, 30, 300])
            for i in range(4):
                self.imagesToDisplay.append([self.colors[self.hiddenCode[i] - 1], (40 * i) + 30, 30])
        if self.rowCount == 10:
            self.imagesToDisplay.append([self.lost, 10, 300])
            for i in range(4):
                self.imagesToDisplay.append([self.colors[self.hiddenCode[i] - 1], (40 * i) + 30, 30])










pg = interface()
pygame.init() # initializing game

window = pygame.display.set_mode((338, 700)) # game dimensions

pygame.display.set_caption('Mastermind')

print(pg.hiddenCode)
run = True
while run: # main loop
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # condition to end
            run = False

    pg.uploadBoard()
    pg.movePegs(x, y)
    pg.placeScorePegs()
    pg.checkWinOrLoss()
    # pg.getCode()
    pygame.display.update()

# pg.startScreen()
pygame.quit()