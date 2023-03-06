import pygame

pygame.init()

X = 1850
Y = 1000
scrn = pygame.display.set_mode((X, Y))

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 128,   0)
PURPLE = (134, 19, 144)
YELLOW = (212, 195, 27)

size = (1850, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess 2")

DEFAULT_IMAGE_SIZE = (80, 80)

PawnDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\pawn.png").convert()
PawnDispl = pygame.transform.scale(PawnDisp, DEFAULT_IMAGE_SIZE)

Pawn1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\pawn1.png").convert()
Pawn1Displ = pygame.transform.scale(Pawn1Disp, DEFAULT_IMAGE_SIZE)

KnightDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\knight.png").convert()
KnightDispl = pygame.transform.scale(KnightDisp, DEFAULT_IMAGE_SIZE)

Knight1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\knight1.png").convert()
Knight1Displ = pygame.transform.scale(Knight1Disp, DEFAULT_IMAGE_SIZE)

BishopDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\bishop.png").convert()
BishopDispl = pygame.transform.scale(BishopDisp, DEFAULT_IMAGE_SIZE)

Bishop1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\bishop1.png").convert()
Bishop1Displ = pygame.transform.scale(Bishop1Disp, DEFAULT_IMAGE_SIZE)

RookDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\rook.png").convert()
RookDispl = pygame.transform.scale(RookDisp, DEFAULT_IMAGE_SIZE)

Rook1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\rook1.png").convert()
Rook1Displ = pygame.transform.scale(Rook1Disp, DEFAULT_IMAGE_SIZE)

KingDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\king.png").convert()
KingDispl = pygame.transform.scale(KingDisp, DEFAULT_IMAGE_SIZE)

King1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\king1.png").convert()
King1Displ = pygame.transform.scale(King1Disp, DEFAULT_IMAGE_SIZE)

QueenDisp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\queen.png").convert()
QueenDispl = pygame.transform.scale(QueenDisp, DEFAULT_IMAGE_SIZE)

Queen1Disp = pygame.image.load("C:\\Users\\fmend\Documents\\Gaspar\\Python Projects\\Chess Images\\queen1.png").convert()
Queen1Displ = pygame.transform.scale(Queen1Disp, DEFAULT_IMAGE_SIZE)

def Board():
    InitBoardX = 475
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 50, 100, 100)) #a8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 150, 100, 100)) #a7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 250, 100, 100)) #a6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 350, 100, 100)) #a5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 450, 100, 100)) #a4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 550, 100, 100)) #a3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX, 650, 100, 100)) #a2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX, 750, 100, 100)) #a1

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 50, 100, 100)) #b8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 150, 100, 100)) #b7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 250, 100, 100)) #b6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 350, 100, 100)) #b5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 450, 100, 100)) #b4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 550, 100, 100)) #b3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 100, 650, 100, 100)) #b2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 100, 750, 100, 100)) #b1

    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 50, 100, 100)) #c8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 150, 100, 100)) #c7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 250, 100, 100)) #c6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 350, 100, 100)) #c5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 450, 100, 100)) #c4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 550, 100, 100)) #c3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 200, 650, 100, 100)) #c2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 200, 750, 100, 100)) #c1

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 50, 100, 100)) #d8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 150, 100, 100)) #d7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 250, 100, 100)) #d6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 350, 100, 100)) #d5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 450, 100, 100)) #d4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 550, 100, 100)) #d3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 300, 650, 100, 100)) #d2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 300, 750, 100, 100)) #d1

    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 50, 100, 100)) #e8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 150, 100, 100)) #e7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 250, 100, 100)) #e6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 350, 100, 100)) #e5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 450, 100, 100)) #e4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 550, 100, 100)) #e3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 400, 650, 100, 100)) #e2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 400, 750, 100, 100)) #e1    

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 50, 100, 100)) #f8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 150, 100, 100)) #f7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 250, 100, 100)) #f6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 350, 100, 100)) #f5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 450, 100, 100)) #f4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 550, 100, 100)) #f3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 500, 650, 100, 100)) #f2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 500, 750, 100, 100)) #f1

    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 50, 100, 100)) #g8
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 150, 100, 100)) #g7
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 250, 100, 100)) #g6
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 350, 100, 100)) #g5
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 450, 100, 100)) #g4
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 550, 100, 100)) #g3
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 600, 650, 100, 100)) #g2
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 600, 750, 100, 100)) #g1

    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 50, 100, 100)) #h8
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 150, 100, 100)) #h7
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 250, 100, 100)) #h6
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 350, 100, 100)) #h5
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 450, 100, 100)) #h4
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 550, 100, 100)) #h3
    pygame.draw.rect(scrn, BLACK, pygame.Rect(InitBoardX + 700, 650, 100, 100)) #h2
    pygame.draw.rect(scrn, WHITE, pygame.Rect(InitBoardX + 700, 750, 100, 100)) #h1

    pygame.display.flip()

def AllPieces():
    PawnA2(PawnA2x)
    PawnB2(PawnB2x)
    PawnC2(PawnC2x)
    PawnD2(PawnD2x)
    PawnE2(PawnE2x)
    PawnF2(PawnF2x)
    PawnG2(PawnG2x)
    PawnH2(PawnH2x)
    Pawn1A7(Pawn1A7x)
    Pawn1B7(Pawn1B7x)
    Pawn1C7(Pawn1C7x)
    Pawn1D7(Pawn1D7x)
    Pawn1E7(Pawn1E7x)
    Pawn1F7(Pawn1F7x)
    Pawn1G7(Pawn1G7x)
    Pawn1H7(Pawn1H7x)
    KnightB1(KnightB1x)
    KnightG1(KnightG1x)
    Knight1B8(Knight1B8x)
    Knight1G8(Knight1G8x)
    BishopC1(BishopC1x)
    BishopF1(BishopF1x)
    Bishop1C8(Bishop1C8x)
    Bishop1F8(Bishop1F8x)
    RookA1(RookA1x)
    RookH1(RookH1x)
    Rook1A8(Rook1A8x)
    Rook1H8(Rook1H8x)
    King(Kingx)
    King1(King1x)
    Queen(Queenx)
    Queen1(Queen1x)

def PawnA2(PawnA2x):
    scrn.blit(PawnDispl, (PawnA2x, 650))
    pygame.display.flip()

def PawnB2(PawnB2x):
    scrn.blit(PawnDispl, (PawnB2x, 650))
    pygame.display.flip()

def PawnC2(PawnC2x):
    scrn.blit(PawnDispl, (PawnC2x, 650))
    pygame.display.flip()

def PawnD2(PawnD2x):
    scrn.blit(PawnDispl, (PawnD2x, 650))
    pygame.display.flip()

def PawnE2(PawnE2x):
    scrn.blit(PawnDispl, (PawnE2x, 650))
    pygame.display.flip()

def PawnF2(PawnF2x):
    scrn.blit(PawnDispl, (PawnF2x, 650))
    pygame.display.flip()

def PawnG2(PawnG2x):
    scrn.blit(PawnDispl, (PawnG2x, 650))
    pygame.display.flip()

def PawnH2(PawnH2x):
    scrn.blit(PawnDispl, (PawnH2x, 650))
    pygame.display.flip()

def Pawn1A7(Pawn1A7x):
    scrn.blit(Pawn1Displ, (Pawn1A7x, 150))
    pygame.display.flip()

def Pawn1B7(Pawn1B7x):
    scrn.blit(Pawn1Displ, (Pawn1B7x, 150))
    pygame.display.flip()

def Pawn1C7(Pawn1C7x):
    scrn.blit(Pawn1Displ, (Pawn1C7x, 150))
    pygame.display.flip()

def Pawn1D7(Pawn1D7x):
    scrn.blit(Pawn1Displ, (Pawn1D7x, 150))
    pygame.display.flip()

def Pawn1E7(Pawn1E7x):
    scrn.blit(Pawn1Displ, (Pawn1E7x, 150))
    pygame.display.flip()

def Pawn1F7(Pawn1F7x):
    scrn.blit(Pawn1Displ, (Pawn1F7x, 150))
    pygame.display.flip()

def Pawn1G7(Pawn1G7x):
    scrn.blit(Pawn1Displ, (Pawn1G7x, 150))
    pygame.display.flip()

def Pawn1H7(Pawn1H7x):
    scrn.blit(Pawn1Displ, (Pawn1H7x, 150))
    pygame.display.flip()

def KnightB1(KnightB1x):
    scrn.blit(KnightDispl, (KnightB1x, 750))
    pygame.display.flip()

def KnightG1(KnightG1x):
    scrn.blit(KnightDispl, (KnightG1x, 750))
    pygame.display.flip()

def Knight1B8(Knight1B8x):
    scrn.blit(Knight1Displ, (Knight1B8x, 50))
    pygame.display.flip()

def Knight1G8(Knight1G8x):
    scrn.blit(Knight1Displ, (Knight1G8x, 50))
    pygame.display.flip()

def BishopC1(BishopC1x):
    scrn.blit(BishopDispl, (BishopC1x, 750))
    pygame.display.flip()

def BishopF1(BishopF1x):
    scrn.blit(BishopDispl, (BishopF1x, 750))
    pygame.display.flip()

def Bishop1C8(Bishop1C8x):
    scrn.blit(Bishop1Displ, (Bishop1C8x, 50))
    pygame.display.flip()

def Bishop1F8(Bishop1F8x):
    scrn.blit(Bishop1Displ, (Bishop1F8x, 50))
    pygame.display.flip()

def RookA1(RookA1x):
    scrn.blit(RookDispl, (RookA1x, 750))
    pygame.display.flip()

def RookH1(RookH1x):
    scrn.blit(RookDispl, (RookH1x, 750))
    pygame.display.flip()

def Rook1A8(Rook1H8x):
    scrn.blit(Rook1Displ, (Rook1H8x, 50))
    pygame.display.flip()

def Rook1H8(Rook1H8x):
    scrn.blit(Rook1Displ, (Rook1H8x, 50))
    pygame.display.flip()

def King(Kingx):
    scrn.blit(KingDispl, (Kingx, 750))
    pygame.display.flip()

def King1(King1x):
    scrn.blit(King1Displ, (King1x, 50))
    pygame.display.flip()

def Queen(Queenx):
    scrn.blit(QueenDispl, (Queenx, 750))
    pygame.display.flip()    

def Queen1(Queen1x):
    scrn.blit(Queen1Displ, (Queen1x, 50))
    pygame.display.flip()   

done = False
clock = pygame.time.Clock()

PawnA2x = 490
PawnB2x = 590
PawnC2x = 690
PawnD2x = 790
PawnE2x = 890
PawnF2x = 990
PawnG2x = 1090
PawnH2x = 1190
Pawn1A7x = 490
Pawn1B7x = 590
Pawn1C7x = 690
Pawn1D7x = 790
Pawn1E7x = 890
Pawn1F7x = 990
Pawn1G7x = 1090
Pawn1H7x = 1190

KnightB1x = 590
KnightG1x = 1090
Knight1B8x = 590
Knight1G8x = 1090

BishopC1x = 690
BishopF1x = 990
Bishop1C8x = 690
Bishop1F8x = 990

RookA1x = 490
RookH1x = 1190
Rook1A8x = 490
Rook1H8x = 1190

Kingx = 890
King1x = 890

Queenx = 790
Queen1x = 790


screen.fill(GREEN)
Board()
AllPieces()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
            if ((x < 575) and (x > 475) and (y < 750) and (y > 650)):
                PieceDropped = False
                while PieceDropped == False:
                    for move in pygame.event.get():
                        if move.type == pygame.MOUSEBUTTONUP:
                            x, y = move.pos
                            print(x)
                            PawnA2(x)
                            PieceDropped = True
    clock.tick(10)
   
pygame.quit()
quit()