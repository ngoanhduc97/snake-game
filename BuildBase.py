import pygame
from time import sleep
from random import randint 

pygame.init()
screen = pygame.display.set_mode((601, 600))            # Set the window size
pygame.display.set_caption('Snake')                     # Set the window title
running = True
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()                             # Control the frame rate
                         
pausing = False

# Snake position
# tail - head
snakes = [[5,10]]
direction = "right" 
score = 0

apple = [randint(0,19), randint(0,19)]                 # Random apple position
font_small = pygame.font.SysFont("sans", 20)            # Small font for score display
font_big = pygame.font.SysFont("sans", 50)              # Big font for game over display

while running:
    clock.tick(60)
    screen.fill(BLACK)
    
    # Get the tail position (create new independent variables, then dont use tail = snakes[])
    tail_x = snakes[0][0]
    tail_y = snakes[0][1]

    # Draw the grid
    # for i in range(21):                     
    #  pygame.draw.line(screen, WHITE, (0,i*30),(600,i*30))  # Draw a white line across the top
    #  pygame.draw.line(screen, WHITE, (i*30,0),(i*30,600))  # Draw a white line down the side
    
    # Draw the snake
    for snake in snakes: 
            pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))  
    
    # Draw the apple
            pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

    # point
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0, [tail_x, tail_y])  
        score += 1              # count the score

        # Generate new apple position (have to make sure it doesn't spawn on the snake)
        for snake in snakes:
            while (apple == snake):
                apple = [randint(0,19), randint(0,19)]

    # Check crash with edges
    if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
        pausing = True

   
    
    # Draw score
    score_txt = font_small.render("Score: " + str(score), True, WHITE)                      # Render score text
    screen.blit(score_txt, (5, 5))                                                          # Display score

    # Snake movement
    if pausing == False:
        if direction == "right":
            snakes.append([snakes[-1][0]+1, snakes[-1][1]])
            snakes.pop(0)
        if direction == "left":
            snakes.append([snakes[-1][0]-1, snakes[-1][1]])
            snakes.pop(0)
        if direction == "up":
            snakes.append([snakes[-1][0], snakes[-1][1]-1])
            snakes.pop(0)
        if direction == "down":
            snakes.append([snakes[-1][0], snakes[-1][1]+1])
            snakes.pop(0)
    
    # Check crash with body 
    for i in range(len(snakes)-1):
        if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
              pausing = True

    # Draw game over 
    if pausing: 
        game_over_txt = font_big.render("GAME OVER, score: " + str(score), True, WHITE)         # Render game over text + score
        press_space_txt = font_big.render("Press SPACE to continue", True, WHITE)
        screen.blit(game_over_txt, (50, 200))                                                      # Display game over text
        screen.blit(press_space_txt, (50, 300))

    sleep(0.07)                                                         # Control the speed of the snake (0.05 is the most difficult, 0.1 is the easiest)

    for event in pygame.event.get():   
        if event.type == pygame.QUIT:               
            running = False
        
        # Handle key presses for snake movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_SPACE and pausing == True:        # Restart the game (add 'and pausing ...' for any unintentional pauses by pressing space during gameplay)
                pausing = False
                snakes = [[5,10]]
                apple = [randint(0,19), randint(0,19)]
                score = 0

    pygame.display.flip()                   # Update the display

pygame.quit()