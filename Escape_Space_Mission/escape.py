# A Python game in space where you need to escape and survive

import pgzrun

# Screen size opening
WIDTH = 800
HEIGHT = 600

# Player position at the start of the game
player_x = 600
player_y = 350

# Function to draw screen display whenever the screen changes
def draw():
    
    # Importing and positioning background image
    screen.blit(images.backdrop,(0,0))
    
    # Importing and positioning planet, player and ship images
    screen.blit(images.mars, (50,50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550,300))

#
def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5

clock.schedule_interval(game_loop, 0.03)
    
pgzrun.go()

