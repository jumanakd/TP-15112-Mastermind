import pygame

class interface():

    def __init__(self):
        self.num = [1, 2, 3, 4, 5, 6]
        self.board = pygame.image.load('Board.png')
        self.redPeg = pygame.image.load('redPeg.png')
        self.greenPeg = pygame.image.load('greenPeg.png')
        self.bluePeg = pygame.image.load('bluePeg.png')
        self.yellowPeg = pygame.image.load('yellowPeg.png')
        self.purplePeg = pygame.image.load('purplePeg.png')
        self.orangePeg = pygame.image.load('orangePeg.png')
        self.blackPeg = pygame.image.load('blackPeg.png')
        self.whitePeg = pygame.image.load('whitePeg.png')

    def uploadBoard(self):
        window.blit(self.board, (0, 0))

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

    def movePegs(self):
        x, y = pygame.mouse.get_pos()
        offset = 30
        drag = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x > 17 and x < 53 and y > 620 and y < 660:
                    drag = True
                    window.blit(self.redPeg, (x - offset, y - offset))

            elif event.type == pygame.MOUSEBUTTONUP:
                drag = False

            elif event.type == pygame.MOUSEMOTION:
                if drag:
                    window.blit(self.redPeg, (x - offset, y - offset))

        # red
        # if x > 17 and x < 53 and y > 620 and y < 660:
        #     window.blit(self.redPeg, (x - offset, y - offset))
        # green
        if x > 58 and x < 93 and y > 620 and y < 660:
            window.blit(self.greenPeg, (x - offset, y - offset))
        # blue
        if x > 97 and x < 132 and y > 620 and y < 660:
            window.blit(self.bluePeg, (x - offset, y - offset))
        # yellow
        if x > 137 and x < 171 and y > 620 and y < 660:
            window.blit(self.yellowPeg, (x - 20, y - 20))
        # purple
        if x > 177 and x < 212 and y > 620 and y < 660:
            window.blit(self.purplePeg, (x - offset, y - offset))
        # orange
        if x > 215 and x < 250 and y > 620 and y < 660:
            window.blit(self.orangePeg, (x - offset, y - offset))






pg = interface()
pygame.init() # initializing game

window = pygame.display.set_mode((338, 700)) # game dimensions

pygame.display.set_caption('Mastermind')

run = True
while run: # main loop
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # condition to end
            run = False
        pg.movePegs()

    window.fill((255, 255, 255))

    pg.uploadBoard()
    pg.movePegs()
    pygame.display.update()

# pg.startScreen()
pygame.quit()