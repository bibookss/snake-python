import pygame
import random

WIDTH = 1280
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def snake(blocksize, snakeCoordinates):
    for coord in snakeCoordinates:
        pygame.draw.rect(gameDisplay, RED, [coord[0], coord[1], blocksize, blocksize])

def food(blocksize, foodX, foodY):
    pygame.draw.rect(gameDisplay, GREEN, [foodX, foodY, blocksize, blocksize])

def displayScore(score):
    message = pygame.font.SysFont("arial", 35).render("Score: " + str(score), True, YELLOW)
    gameDisplay.blit(message, [600,0])

def displayEnd(score):
    message1 = pygame.font.SysFont("arial", 35).render("Game Over!", True, BLACK)
    message2 = pygame.font.SysFont("arial", 35).render("Score: " + str(score), True, BLACK)
    gameDisplay.blit(message1, [600, HEIGHT/3])
    gameDisplay.blit(message2, [600, HEIGHT/2.5])

def main():
    global gameDisplay

    pygame.init()
    gameDisplay = pygame.display.set_mode([WIDTH, HEIGHT])
    gameClock = pygame.time.Clock()
    pygame.display.set_caption("Snake Game")

    blockSize = 20
    score = 0

    # Snake attributes
    snakeX = 0
    snakeY = 0
    snakeXChange = 0
    snakeYChange = 0
    snakeCoordinates = []
    snakeLength = 1

    # Food attributes
    foodX = round(random.randrange(blockSize, WIDTH - blockSize) / 20.0) * 20.0
    foodY = round(random.randrange(blockSize, HEIGHT - blockSize) / 20.0) * 20.0

    gameOver = False
    gameEnd = False 

    drawBorder(blockSize)

    while not gameOver:
        gameDisplay.fill(BLACK)
        drawBorder(blockSize)
        while gameEnd:
            gameDisplay.fill(WHITE)
            displayEnd(score)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameEnd = False
                    if event.key == pygame.K_c:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
                gameEnd = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snakeXChange = 0
                    snakeYChange = 20
                if event.key == pygame.K_UP:
                    snakeXChange = 0
                    snakeYChange = -20
                if event.key == pygame.K_RIGHT:
                    snakeXChange = 20
                    snakeYChange = 0
                if event.key == pygame.K_LEFT:
                    snakeXChange = -20
                    snakeYChange = 0

        # Update coorindates of snake
        snakeX += snakeXChange
        snakeY += snakeYChange
        snakeHead = []
        snakeHead.append(snakeX)
        snakeHead.append(snakeY)
        snakeCoordinates.append(snakeHead)

        # Make sure that the length of the snake is accurate
        if len(snakeCoordinates) > snakeLength:
            del snakeCoordinates[0]

        # Draw snake
        snake(blockSize, snakeCoordinates)

        # Draw food
        food(blockSize, foodX, foodY)

        # Check if snake eats food
        if snakeX == foodX and snakeY == foodY:
            snakeLength += 1
            score += 1
            foodX = round(random.randrange(blockSize, WIDTH - blockSize) / 20.0) * 20.0
            foodY = round(random.randrange(blockSize, HEIGHT - blockSize) / 20.0) * 20.0
        
        # Check if snake goes out of bounds
        if (snakeX >= WIDTH or snakeX < 0 or snakeY >= HEIGHT or snakeY < 0):
            gameEnd = True

        # Check if snake eats self
        for coord in snakeCoordinates[:-1]:
            if coord == snakeHead:
                print("Hit")
                gameEnd = True

        displayScore(score)
        pygame.display.flip()
        gameClock.tick(20)

    pygame.quit()
    quit()

main()