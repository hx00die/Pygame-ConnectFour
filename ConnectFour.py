import pygame, sys
from math import inf

screen_width = 700
screen_height = 700

cel_size = 100
colums = 7
rows = 6
spacing = 50

player1 = (7, 177, 155)
player2 = (42, 61, 80)
player_colour = player1
player = 1

board = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

# code tacken from: https://www.pygame.org/project-AAfilledRoundedRect-2349-.html
def AAfilledRoundedRect(surface,rect,color,radius=0.1):
    rect         = pygame.Rect(rect)
    color        = pygame.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)

def draw_grid():
    for i in range(rows + 1):
        for j in range(1, colums):
            x = i * cel_size + spacing
            y = j * cel_size + spacing
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 25)

def show_piece(xpos):
    pygame.draw.circle(screen, player_colour, (xpos * cel_size + spacing, 70), 25)

def check_winner(board):

    for i in range(colums-3):
        for j in range(rows):
            if board[j][i] == board[j][i+1] and board[j][i+1] == board[j][i+2] and board[j][i+2] == board[j][i+3]  and board[j][i] != 0:
                return board[j][i]

    for i in range(colums):
        for j in range(rows-3):
            if board[j][i] == board[j+1][i] and board[j+1][i] == board[j+2][i] and board[j+2][i] == board[j+3][i]  and board[j][i] != 0:
                return board[j][i]

    for i in range(colums-3):
        for j in range(rows-3):
            if board[j][i] == board[j+1][i+1] and board[j+1][i+1] == board[j+2][i+2] and board[j+2][i+2] == board[j+3][i+3]  and board[j][i] != 0:
                return board[j][i]

    for i in range(colums-3):
        for j in range(3, rows):
            if board[j][i] == board[j-1][i+1] and board[j-1][i+1] == board[j-2][i+2] and board[j-2][i+2] == board[j-3][i+3]  and board[j][i] != 0:
                return board[j][i]

    for i in board:
        for j in i:
            if j == 0:
                return None

    return 0
    
def draw_board(board):
    for i in range(rows):
        for j in range(colums):
            x = i * cel_size + spacing * 3
            y = j * cel_size + spacing
            if board[i][j] == 1:
                pygame.draw.circle(screen, player1, (y, x), 25)
            elif board[i][j] == 2:
                pygame.draw.circle(screen, player2, (y, x), 25)
         
def drop_piece(xpos, board):
    for i in range(len(board) - 1, -1, -1):
        if board[i][xpos] == 0:
            return i


while True:
    screen.fill((255,255,255))

    pos = pygame.mouse.get_pos()
    xpos = pos[0] // cel_size

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and check_winner(board) == None:
            board[drop_piece(xpos, board)][xpos] = player
            if player == 1:
                player = 2
                player_colour = player2
            else:
                player = 1
                player_colour = player1
    
    show_piece(xpos)
    AAfilledRoundedRect(screen, (10, 100, screen_width - 20, screen_height - 110), (205,211,219))
    draw_grid()
    draw_board(board)
    pygame.display.flip()
    clock.tick(30)

