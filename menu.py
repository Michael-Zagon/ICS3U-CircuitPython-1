#/usr/bin/env python3

# Created by: Michael Zagon
# Created on: October 2021
# This is the space alians game

import ugame
import stage

import constants

def menu_scene():
    # This function is the menu_scene

    # Image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)

    # Create stage and set fps to 60
    game = stage.Stage(ugame.display, constants.FPS)
    # Set layers of all sprites, items show up in order
    game.layers = [text] + [background]
    # Render sprites and background
    game.render_block()

    # infinite loop
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()
        

        # Update game Logic
        game.tick() # wait until refresh rates finishes


def game_scene():
    # This function is the main game game_scene

    # Image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # Buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    
    # Get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # Set image and set size
    background = stage.Grid(image_bank_background, 10, 8)

    # A sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    alien = stage.Sprite(image_bank_sprites, 9,
                     int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                     16)

    # Create stage and set fps to 60
    game = stage.Stage(ugame.display, 60)
    # Set layers of all sprites, items show up in order
    game.layers = [ship] + [alien] + [background]
    # Render sprites and background
    game.render_block()

    # infinite loop
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # Update game Logic
        # Play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw Sprite
        game.render_sprites([ship] + [alien])
        game.tick() # Wait until refresh rate finishes

if __name__ == "__main__":
    menu_scene()
