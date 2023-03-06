# file created by: Alec Borer

# import libraries

from time import sleep

from random import randint

import pygame as pg

import os

# setup asset folders - images and sounds as needed
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 1200
HEIGHT = 680
FPS = 30
GAMEOVER = False

# defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# for the while loop later
running = True

# init pygame and create a window
pg.init()
pg.mixer.init()
# allows us to define size of window
screen = pg.display. set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors")
clock = pg.time.Clock()
# creates a file path back to this one and opens an image
# all images were found on Google images
rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()
scissors_image = pg.image.load(os.path.join(game_folder, "scissors.jpg")).convert()
yes_image = pg.image.load(os.path.join(game_folder, "yes.png")).convert()
no_image = pg.image.load(os.path.join(game_folder, "no.jpg")).convert()
you_win_image = pg.image.load(os.path.join(game_folder, "you win.png")).convert()
I_won_image = pg.image.load(os.path.join(game_folder, "I_won.jpg")).convert()
tie_image = pg.image.load(os.path.join(game_folder, "tie.gif")).convert()
Again_image = pg.image.load(os.path.join(game_folder, "Again.png")).convert()

# creates a rectangle over each image
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
yes_rect = yes_image.get_rect()
no_rect = no_image.get_rect()
you_win_rect = you_win_image.get_rect()
I_won_rect = I_won_image.get_rect()
tie_rect = tie_image.get_rect()
Again_rect = Again_image.get_rect()


choices = ["rock", "paper", "scissors"]

# defines computer choice
def cpu_choice():
    return choices[randint(0,2)]

# what happens when the cpu wins
def end_screen_cpuwin():
    screen.fill(WHITE)
    screen.blit(I_won_image, I_won_rect)

# what happens when the player wins
def end_screen_playerwin():
    screen.fill(WHITE)
    screen.blit(you_win_image, you_win_rect)  

# what happens when it is a draw
def end_screen_tie():
    screen.fill(WHITE)
    screen.blit(tie_image, tie_rect)


# modified rps function from day 10
def rps():
    cpu = cpu_choice()
    user = user_choice
    # debugging tool
    print("I chose: "+ cpu)
    # if theres a tie
    if user == cpu:
        # creates the image for it there is a tie
        end_screen_tie()
        # updates screen and waits to make sure the user has time to see it
        pg.display.flip()
        pg.time.delay(1000)
    # if the user chose rock
    elif user == "rock":
        if cpu == "paper":
            # creates the image for if the computer wins
            end_screen_cpuwin()
            # updates screen and waits to make sure the user has time to see it
            pg.display.flip()
            pg.time.delay(1000)
        elif cpu == "scissors":
            # creates the image for if the player wins
            end_screen_playerwin()
            # updates screen and waits to make sure the user has time to see it
            pg.display.flip()
            pg.time.delay(1000)
    # if the user chose paper
    elif user == "paper":
        if cpu == "scissors":
            # creates the image for if the computer wins
            end_screen_cpuwin()
            # updates screen and waits to make sure the user has time to see it
            pg.display.flip()
            pg.time.delay(1000)
        elif cpu == "rock":
            # creates the image for if the player wins
            end_screen_playerwin()
            # updates screen and waits to make sure the user has time to see it
            pg.display.flip()
            pg.time.delay(1000)
    # if the user chose scissors
    elif user == "scissors":
        if cpu == "rock":
           # creates the image for if the computer wins
            end_screen_cpuwin()
            # updates screen and waits to make sure the user has time to see it
            pg.display.flip()
            pg.time.delay(1000)
        elif cpu == "paper":
            # creates the image for if the player wins 
            end_screen_playerwin()
            # updates screen and waits to make sure the user has time to see it
            pg.display.flip()
            pg.time.delay(1000)


while running:
    # how fast the loop updates
    clock.tick(FPS)
    # get input from player
    # events are actions
    for event in pg.event.get():
        # closes the window if you hit the close button
        if event.type == pg. QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            # gets mouse position when button is lifted up   
            mouse_coords = pg.mouse.get_pos()
            # checks if the mouse position is within boundaries and executes a function if true
            if rock_rect.collidepoint(mouse_coords):
                user_choice = "rock"
                # debugging tool
                print(user_choice)
                rps()
                # switches to the end screen once rps is done
                GAMEOVER = True
            elif paper_rect.collidepoint(mouse_coords):
                user_choice = "paper"
                # debugging tool
                print(user_choice)
                rps()
                # switches to the end screen once rps is done
                GAMEOVER = True
            elif scissors_rect.collidepoint(mouse_coords):
                user_choice = "scissors"
                # debugging tool
                print(user_choice)
                rps()
                # switches to the end screen once rps is done
                GAMEOVER = True
            # changes back to the normal screen if you hit the again button
            elif Again_rect.collidepoint(mouse_coords):
                GAMEOVER = False
            # unnecessary message in the terminal for if you don't click on a button
            else:
                print("you missed")

    # update
   
    
    # draw
    # normal screen
    if not GAMEOVER:
        # sets the background color and draws all the images and rectangles for the user to choose from
        screen.fill(WHITE)
        screen.blit(rock_image, rock_rect)
        screen.blit(paper_image, paper_rect)
        screen.blit(scissors_image, scissors_rect)
        # moves the images 
        rock_rect.x = 0
        paper_rect.y = 200
        scissors_rect.x = 300
    # end screen
    elif GAMEOVER:
        screen.fill(WHITE)
        screen.blit(Again_image, Again_rect)
        # moves the images and hitboxes offscreen so they aren't accidently pressed when they aren't supposed to be there
        rock_rect.x = 10000
        paper_rect.y = 2000
        scissors_rect.x = 3000
    # updates the screen
    pg.display.flip()
pg.quit()