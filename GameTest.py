import pygame
from pygame.locals import(
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT
        )


pygame.init()


screenWidth = 800
screenHeight = 600


screen = pygame.display.set_mode((screenWidth, screenHeight))


def main():


    # Defining variables
    playerMovementX = 0
    playerMovementY = 0
    cubeMovementX = 0
    cubeMovementY = 0
    cubeRelationX = 0
    cubeRelationY = 0
    cubePositionX = 0
    cubePositionY = 0


    running = True
    while running:


        playerPositionX = 100 + playerMovementX
        playerPositionY = 50 + playerMovementY


        # Tell the cube which direction to be pushed depending on how the player approaches it
        if playerPositionX > cubePositionX:
            cubeRelationX = -50
            cubeRelationY = 0
        elif playerPositionX < cubePositionX:
            cubeRelationX = 50
            cubeRelationY = 0
        elif playerPositionY > cubePositionY:
            cubeRelationY = -50
            cubeRelationX = 0
        elif playerPositionY < cubePositionY:
            cubeRelationY = 50
            cubeRelationX = 0


        # If the cube reaches the edge of the screen then teleport it to the other side
        if cubePositionX < 0:
            cubeMovementX += screenWidth
        elif cubePositionX >= screenWidth:
            cubeMovementX -= screenWidth
        elif cubePositionY < 0:
            cubeMovementY += screenHeight
        elif cubePositionY >= screenHeight:
            cubeMovementY -= screenHeight


        # If the player reaches the edge of the screen then teleport it to the other side 
        # and orient cubeRelation so that it will push the cube in the correct direction
        if playerPositionX < 0:
            cubeRelationX = -50
            cubeRelationY = 0
            playerMovementX += screenWidth 
        if playerPositionX >= screenWidth:
            cubeRelationX = 50
            cubeRelationY = 0
            playerMovementX -= screenWidth
        if playerPositionY < 0:
            cubeRelationX = 0
            cubeRelationY = -50
            playerMovementY += screenHeight 
        if playerPositionY >= screenHeight:
            cubeRelationX = 0
            cubeRelationY = 50
            playerMovementY -= screenHeight
       

        # If the player overlaps the cube then push it to the side
        if playerPositionX == cubePositionX and playerPositionY == cubePositionY:
            cubeMovementX += cubeRelationX
            cubeMovementY += cubeRelationY


        cubePositionX = 600 + cubeMovementX
        cubePositionY = 400 + cubeMovementY

        
        # Tells the game what to do with each button press
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    playerMovementY += -50
                elif event.key == K_DOWN:
                    playerMovementY += 50
                elif event.key == K_RIGHT:
                    playerMovementX += 50
                elif event.key == K_LEFT:
                    playerMovementX += -50
                else:
                    playerMovementY += 0
                    playerMovementX += 0
            elif event.type == QUIT:
                running = False
        

        screen.fill((0, 0, 0))


        # Tells the game where to draw the player and cube and what color these should be
        player = pygame.draw.rect(screen, (255, 0, 0), (playerPositionX, playerPositionY, 50, 50))
        cube = pygame.draw.rect(screen, (0, 0, 255), (cubePositionX, cubePositionY, 50, 50))
    

        pygame.display.update()
    

        pygame.time.Clock().tick(60)


main()
