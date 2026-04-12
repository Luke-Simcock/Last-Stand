#5323 pre game code

#Importations
import os
import pygame 
import random
import sys
import time


#variables
hz = 144
placeholder = "" #can be changed with no effect
stop_music = False
menu_choice = ""
settings_choice = ""

#Title
def start_title():
    print("===============================================================================")
    time.sleep(0.5)
    print("           :::::::::::::    :::::::::::     ::::::::        ::::::::::: ")
    time.sleep(0.5)
    print("          :+:       :+:   :+:       :+:   :+:       :+:   :+:      :+: ")
    time.sleep(0.5)
    print("         +:+                       +:+          +:+               +:+  ")
    time.sleep(0.5)
    print("        +#++:++:++#+        +#++:++:         +#+           +#++:++:    ")
    time.sleep(0.5)
    print("                 +#+              +#+     +#+                    +#+    ")
    time.sleep(0.5)
    print("      #+#       #+#   #+#       #+#    #+#           #+#       #+#     ")
    time.sleep(0.5)
    print("      ###########     ###########    #############   ###########       ")      
    time.sleep(0.5)
    print("===============================================================================")
    time.sleep(1.5)

def game():
    #Game Settings
    hz = 144

    #Enemy Intilisation
    enemy_time = random.randint(45, 50)  # Pause duration in frames (3–5 seconds at 60 FPS)
    LorR_Enemy = random.choice([1, 100])     # Random left (-1) or right (+1)
    LorR_Calc = random.randint(0, 100)

    #ESSENTIAL CODE DO NOT TOUCH
    pygame.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()

    #Setting Up Window
    WIDTH = 1543
    HEIGHT = 864

    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN) 
    pygame.display.set_caption("5323")

    #Player Colour
    WHITE = (255, 255, 255)
    player_size = 70
    player_speed = 7
    enemy_speed = 5

    #Players Assignment
    enemy_rect = pygame.Rect(WIDTH//2-40, 10, player_size, player_size)
    player_rect = pygame.Rect(WIDTH//2-40, HEIGHT-80, player_size, player_size)
    running = True

    #GAME LOOP ITSELF
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        #Players Movement
        keys = pygame.key.get_pressed()

        #Joystick Stuff
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            
            # Axis 0: Left/Right movement
            left_x = joystick.get_axis(0)

            #Player Movement
            if left_x <= 0.1: player_rect.x -= player_speed*abs(left_x)
            if left_x >= -0.1: player_rect.x += player_speed*abs(left_x)

        if keys[pygame.K_a]: player_rect.x -= player_speed
        if keys[pygame.K_d]: player_rect.x += player_speed
        
        player_rect.x = max(0, min(WIDTH - player_size, player_rect.x))
        player_rect.y = max(0, min(HEIGHT - player_size, player_rect.y))


        #Enemy Movement
        if enemy_time > 0:
            enemy_time -= 1

            #timer runs out
            if LorR_Enemy >= LorR_Calc:  
                enemy_rect.x -= enemy_speed   #left
            elif LorR_Enemy < LorR_Calc: 
                enemy_rect.x += enemy_speed   #right

        else:
            #Reset
            enemy_time = random.randint(45, 50)  # Pause duration in frames (3–5 seconds at 60 FPS)
            LorR_Enemy = enemy_rect.x / 1543 * 100
            LorR_Calc = random.randint(0, 100) 
            
        enemy_rect.x = max(0, min(WIDTH - player_size, enemy_rect.x))
        enemy_rect.y = max(0, min(HEIGHT - player_size, enemy_rect.y))

        #Drawing Characters
        pygame.draw.rect(screen, WHITE, player_rect)
        pygame.draw.rect(screen, WHITE, enemy_rect)

        #Kills Game
        if keys[pygame.K_ESCAPE]: sys.exit()

        #Cirtical Screen Stuff
        pygame.display.flip()
        screen.fill("black")
        clock.tick(hz)

    pygame.quit()
    sys.exit()


#Menu
def menu():
    global placeholder
    global stop_music
    global menu_choice
    global settings_choice

    print("")
    print("===================================== Menu ====================================")
    time.sleep(0.5)
    print("Press 1 to Start")
    time.sleep(0.5)
    print("Press 2 to open settings")
    time.sleep(0.5)
    print("Press 3 to open tutorial")
    time.sleep(0.5)
    print("Press 4 to open leaderboard")
    time.sleep(0.5)
    print("Press 5 to open accounts")
    time.sleep(0.5)
    print("Press 6 to open credits")
    time.sleep(0.5)
    print("Press Esc to quit")
    time.sleep(0.5)
    menu_choice = input("Enter choice: ")
    print("===============================================================================")
    print("")
    
    #The Game
    if menu_choice == "1":
        game()


    #Settings
    if menu_choice == "2":
        print("")
        print("=================================== Settings ==================================")
        time.sleep(0.5)
        print("Press 1 to open game Hz")
        time.sleep(0.5)
        print("Press 2 to open audio")
        time.sleep(0.5)
        print("Press 3 to open music")
        time.sleep(0.5)
        print("Press 4 to open difficulty")
        time.sleep(0.5)
        print("Press 5 to open menu")
        time.sleep(0.5)
        print("Press Esc to quit")
        time.sleep(0.5)
        settings_choice = input("Enter choice: ")
        print("===============================================================================")
        print("")

        #Hz
        if settings_choice == "1":
            print("-------------------------------------- Hz -------------------------------------")
            print("Lower will put less strain on your computer but may make the game less smooth")
            time.sleep(1)
            print("Higher will make the game more smooth but may put less strain on your computer")
            time.sleep(1)
            print("This will also effct how many ")
            time.sleep(1)
            print("It is recommended to match your in game Hz to your monitors Hz")
            time.sleep(1)
            print("Hz must be 24, 30, 60, 75, 100, 120, 144, 165, 180 or 240")
            time.sleep(1)
            print("Default is 60")
            time.sleep(1)
            hz = int(input("Enter Hz: "))
            print("===============================================================================")
            time.sleep(2)
            return hz

        #Audio
        if settings_choice == "2":
            print("------------------------------------- Audio  -----------------------------------")
            print("This Audio took too long to make so deal with it")
            time.sleep(1)
            placeholder = input("")
            print("===============================================================================")
            print("")
            menu()

        #Music settings
        if settings_choice == "3":
            print("------------------------------------ Music  -----------------------------------")
            print("Press 1 to turn on music")
            time.sleep(1)
            print("Press 2 to turn off music")
            time.sleep(1)
            print("Press Esc to quit")
            time.sleep(1)
            music_choice = int(input("Enter choice: "))
            print("===============================================================================")
            if music_choice == 1:
                stop_music = False
                music()
                menu()
            if music_choice == 2:
                stop_music = True
                menu()

        #Difficulty
        if settings_choice == "4":
            print("---------------------------------- Difficulty ---------------------------------")
            print("Difficulty settings coming soon!")
            time.sleep(1)
            placeholder = input("")
            menu()

        #Menu
        if settings_choice == "5":
            menu()

        #Tutorial
    
    #Tutorial
    if menu_choice == "3":
        print("")
        print("=================================== Tutorial ==================================")
        time.sleep(0.5)
        print("5323 is a single player space shooter game where the goal is to get 5323 points.")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("You move left using the        A key")
        print("You move right using the       D key")
        print("You shoot bullets using the    Space bar")
        print("You shoot missiles using the   M key")
        print("You shoot bombs using the      B key")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Player types and stats:")
        print("colour          bullet         missile         bomb        health       level")
        print("Base            1x bullet      1x missile      1x bomb     15 health    level 4.5")
        print("Rifle           1.3x bullet    1x missile      1x bomb     15 health    level 5")
        print("ICBM            1x bullet      1.2x missile    1x bomb     15 health    level 5")
        print("Bomber          1x bullet      1x missile      1.25x bomb  15 health    level 5")
        print("Tank            1x bullet      1x missile      1x bomb     25 health    level 5")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Armour          1.5x bullet    1.4x missile    1.2x bomb   +80 health   level 6.5")
        print("coin            1, 2, 5, 10, 25, 50, 100, 200, 1000")
        print("dice            [2-5 nothing] [1 player to 1hp] [6 removes 50% of all enemies total hp] ")
        print("hammer          puts health back to 100%")
        print("sands of time   gives player an extra life")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Enemy types and stats:")
        print("colour          bullet         missile         bomb        health       level")
        print("black           0.2x bullet                                1 health     level 1")
        print("orange          0.5x bullet                                3 health     level 2")
        print("yellow          0.75x bullet   0.5x missile                5 health     level 3")
        print("blue            1x bullet      1x missile                  10 health    level 4")
        print("red             1.25x bullet   1.25x missile   1x bomb     25 health    level 5")
        print("purple          1.5x bullet    1.4x missile    1.2x bomb   50 health    level 6")
        print("pink            2x bullet      1.75x missile   1.5x bomb   100 health   level 7")
        print("white           3x bullet      2x missile      1.8x bomb   200 health   level 8")
        print("gold            5x bullet      3x missile      3x bomb     1000 health  level 9")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Upgrades:")
        print("damage          +1 bullet      +2 missile      +5 bomb")
        print("speed           -7% bullet     -5% missile     -10% bomb")
        print("delay           -5% bullet     -7% missile     -10% bomb")
        print("health          +5 health")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Level ups:")
        print("damage          +2 bullet      +5 missile      +10 bomb")
        print("speed           -15% bullet   -10% missile     -25% bomb")
        print("delay           -10% bullet   -15% missile     -25% bomb")
        print("health          +20 health")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Avoid enemy fire and destroy enemies to gain points.")
        print("Enemies come in waves, with 8 waves per level")
        print("At the start you are the strongest character by a bit")
        print("By the end, you are the weakest character by a LOT")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Bullets, missiles and bombs are the weapons.")
        print("Each weapon has different damage, duration and delay stats.")
        print("These are the default weapon stats:")
        print("weapon     damage         map travel      delay")
        print("bullets    1 damage       3 sec           1s")
        print("missiles   5 damage       1 sec           3s")
        print("bombs      25 damage      10 sec          30s")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("5323          The games name")
        print("Menu          Main section where all sections branch off from")
        print("Settings      Goes to the settings")
        print("Start         Begins the games selection")
        print("Tutorial      Explains the games premise and functions (hopefully)")
        print("Account       Brings up sign up/in")
        print("Sign up       Allows account creation")
        print("Sign in       Allows account log in")
        print("Leaderboard   Shows leaderboard of users who have the biggest high score")
        print("Customise     Allows a user to change their username/password for an account")
        print("Credits       Says who worked on every part")
        print("Settings      Opens the settings menu")
        print("Hz            Sets the refresh rate of the game")
        print("Sound         Effects can be toggled on and off (coming soon)")
        print("Music         Can be toggled on and off")
        print("Difficulty    Easy, normal, hard and impossible")
        print("Restart       Goes back to the start of the level")
        print("")
        placeholder = input("Menu: ")
        print("===============================================================================")
        print("")
        menu()

    #Leaderboard
    if menu_choice == "4":
        #top players scores
        print("")
        menu()

    #Accounts
    if menu_choice == "5":
        #accoount stuff
        print("")
        menu()

    #Credits
    if menu_choice == "6":
        print("")
        print("=================================== Credits ===================================")
        time.sleep(0.5)
        print("Producer       Luke Simcock")
        time.sleep(0.5)
        print("Directors      Luke Simcock")
        time.sleep(0.5)
        print("Designers      Luke Simcock")
        time.sleep(0.5)
        print("Level          Luke Simcock")
        time.sleep(0.5)
        print("UI             Luke Simcock")
        time.sleep(0.5)
        print("Artists        Luke Simcock")
        time.sleep(0.5)
        print("Concept        Luke Simcock")
        time.sleep(0.5)
        print("3D             Luke Simcock")
        time.sleep(0.5)
        print("Texture        Luke Simcock")
        time.sleep(0.5)
        print("Animation      Luke Simcock")
        time.sleep(0.5)
        print("VFX            Luke Simcock")
        time.sleep(0.5)
        print("Audio          Luke Simcock")
        time.sleep(0.5)
        print("Music          Luke Simcock")
        time.sleep(0.5)
        print("Sound          Luke Simcock")
        time.sleep(0.5)
        print("Composers      Luke Simcock")
        time.sleep(0.5)
        print("Voice Actors   Luke Simcock")
        time.sleep(0.5)
        print("Programmers    Luke Simcock")
        time.sleep(0.5)
        print("Engine         Luke Simcock")
        time.sleep(0.5)
        print("AI             Luke Simcock")
        time.sleep(0.5)
        print("Tools          Luke Simcock")
        time.sleep(0.5)
        print("Licensing      Luke Simcock")
        time.sleep(0.5)
        print("Publishers     Luke Simcock")
        placeholder = input("Continue: ")
        time.sleep(0.5)
        print("===============================================================================")
        print("")
        menu()



#Music
def music():
    #Music on or off
    global stop_music

    #Function to play a random song
    def play_random_song():
        song = random.choice(mp3_files)
        #print(f"Playing: {song}")
        pygame.mixer.music.load(os.path.join(music_folder, song))
        pygame.mixer.music.play()

    #Folder where your MP3s are
    music_folder = r"C:\Users\luke\Music\Majority And Minority"

    #Get a list of all MP3 files in that folder
    mp3_files = [f for f in os.listdir(music_folder) if f.lower().endswith(".mp3")]

    if not mp3_files:
        exit()

    #Initialize mixer
    pygame.mixer.init()

    #First song
    play_random_song()

    #Plays song
    while not stop_music:
        play_random_song()
        while not stop_music:
            time.sleep(0.001)
            if not pygame.mixer.music.get_busy() and not stop_music:
                play_random_song()
    return stop_music





start_title()
menu()

