#5323 pre game code
#████████ ████████ ████████ ████████
#██             ██ ██    ██       ██
#████████   ██████     ██     ██████
#      ██       ██   ██           ██
#████████ ████████ ████████ ████████

#████████ ████████ ██    ██ ██████   ████████ ████████ ████████
#██          ██    ██    ██ ██    ██    ██    ██    ██ ██
#████████    ██    ██    ██ ██    ██    ██    ██    ██ ████████
#      ██    ██    ██    ██ ██    ██    ██    ██    ██       ██
#████████    ██    ████████ ██████   ████████ ████████ ████████


#Importations
import os
import pygame 
import random
import sys
import time
import threading
from ctypes import windll
from tkinter import *
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_a,
    K_s,
    K_d,
    K_SPACE,
    K_m,
    K_b,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#5323 Alpha 3.1

#variables
hz = 60
placeholder = "" #can be changed with no effect
stop_music = False
menu_choice = ""
settings_choice = ""

#Title
def start_title():
    print("===============================================================================")
    time.sleep(0.5)
    print("      :::            :::      :::::::: :::::::::::          ")
    print("     :+:          :+: :+:   :+:    :+:    :+:               ")
    print("    +:+         +:+   +:+  +:+           +:+                ")
    print("   +#+        +#++:++#++: +#++:++#++    +#+                 ")
    print("  +#+        +#+     +#+        +#+    +#+                  ")
    print(" #+#        #+#     #+# #+#    #+#    #+#                   ")
    print("########## ###     ###  ########     ###                    ")
    print("                                                            ")
    print("          :::::::: ::::::::::: :::     ::::    ::: :::::::::")
    print("        :+:    :+:    :+:   :+: :+:   :+:+:   :+: :+:    :+:")
    print("       +:+           +:+  +:+   +:+  :+:+:+  +:+ +:+    +:+ ")
    print("      +#++:++#++    +#+ +#++:++#++: +#+ +:+ +#+ +#+    +:+  ")
    print("            +#+    +#+ +#+     +#+ +#+  +#+#+# +#+    +#+   ")
    print("    #+#    #+#    #+# #+#     #+# #+#   #+#+# #+#    #+#    ") 
    print("    ########     ### ###     ### ###    #### #########      ")
    time.sleep(0.5)
    print("===============================================================================")
    print("===============================================================================")
    time.sleep(0.5)
    print("      ██            ███████████   ██████████████  ██████████████          ")
    print("     ██            ██        ██  ██                     ██     ")
    print("    ██            ██        ██  ██                     ██      ")
    print("   ██            ████████████  ██████████████         ██       ")
    print("  ██            ██        ██              ██         ██        ")
    print(" ██            ██        ██  ██          ██         ██         ")
    print("████████████  ██        ██  ██████████████         ██          ")
    print("                                                            ")
    print("      ██████████████  ██████████████  ███████████   ██        ██  ██████████    ")
    print("     ██                     ██       ██        ██  ████      ██  ██        ██" \
    "")
    print("    ██                     ██       ██        ██  ██  ██    ██  ██         ██  ")
    print("   ██████████████         ██       ████████████  ██   ██   ██  ██         ██    ")
    print("              ██         ██       ██        ██  ██    ██  ██  ██         ██    ")
    print(" ██          ██         ██       ██        ██  ██      ████  ██        ███      ")
    print("██████████████         ██       ██        ██  ██        ██  ████████████                ")
    time.sleep(0.5)
    print("===============================================================================")


def game():
    #Game Settings
    print("+")


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
        
        print("===============================================================================")
        print("===============================================================================")
        time.sleep(0.5)
        print("[You]")
        print("*Where am i?*")
        placeholder = input("")
        time.sleep(0.5)
        print("[You]")
        print("*Who am i?*")
        placeholder = input("")
        time.sleep(0.5)
        print("[Man]")
        print("You are a civilain in the Terran Galactic Empire.")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("I am General Nishikado of the Unified Armed Forces of the Sagittarius Arm.")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("There has been a brutal war against our people.")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("Casualties across the empire are at 34%")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("Casualties across the most effected regions are at 89%")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("The enemy has captured the Perseus Arm of the milky way.")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("This leaves only the Sagittarius Arm region to defend us.")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("If we fail to hold this point then the Orion Arm will fall and with it, our empire.")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("You have been conscripted into the General Defencive Force of the Sagittarius Arm")
        placeholder = input("")
        time.sleep(0.5)        
        print("[General Nishikado]")
        print("This regiment is a level 2 importance meaning only the force more valuable is the Final Defencive Force of the Orion Arm.")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("Your only objective is to inflict as much harm to the enemy forces as possible")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("We have ranked all enemy forces at levels 1-10")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("You Appear to be a level 4.5, with a class selected you can go up to a level 5")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("You can reach up to a level 6.5 with armour")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("You better come back a hero or not at all")
        placeholder = input("")
        time.sleep(0.5)
        print("[General Nishikado]")
        print("Good luck soldier")
        placeholder = input("")
        print("")
        game()


    #Settings
    if menu_choice == "2":
        print("")
        print("=================================== Settings ==================================")
        time.sleep(0.5)
        print("Press 1 to open audio")
        time.sleep(0.5)
        print("Press 2 to open music")
        time.sleep(0.5)
        print("Press 3 to open difficulty")
        time.sleep(0.5)
        print("Press 4 to open menu")
        time.sleep(0.5)
        print("Press Esc to quit")
        time.sleep(0.5)
        settings_choice = input("Enter choice: ")
        print("===============================================================================")
        print("")

        #Hz
        if settings_choice == "1":
            print("------------------------------------- Audio  -----------------------------------")
            print("This Audio took too long to make so deal with it")
            time.sleep(1)
            placeholder = input("")
            print("===============================================================================")
            print("")
            menu()

        #Music settings
        if settings_choice == "2":
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
        if settings_choice == "3":
            print("---------------------------------- Difficulty ---------------------------------")
            print("Difficulty settings coming soon!")
            time.sleep(1)
            placeholder = input("")
            menu()

        #Menu
        if settings_choice == "4":
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
        print("You move left using the        A key       Right D-PAD")
        print("You move right using the       D key       Left D-PAD")
        print("You shoot bullets using the    Space bar   R2")
        print("You shoot missiles using the   M key       X ")
        print("You shoot bombs using the      B key       O ")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Player types and stats:")
        print("colour     bullet         missile         bomb        health       level")
        print("Base       5  bullet      7  missile      25 bomb     15 health    level 4.5")
        print("Rifle      7  bullet      7  missile      25 bomb     15 health    level 5")
        print("ICBM       5  bullet      15 missile      25 bomb     15 health    level 5")
        print("Bomber     5  bullet      7  missile      35 bomb     15 health    level 5")
        print("Tank       5  bullet      7  missile      25 bomb     35 health    level 5")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Armour     10 bullet      15 missile      30 bomb     +80 health   level 6.5")
        print("Coin            1, 2, 5, 10, 25, 50, 100, 200, 1000")
        print("Sands of Time   gives player an extra life")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Enemy types and stats:")
        print("colour      bullet      missile      bomb        health        level")
        print("Turquoise   1  bullet                            1    health   level 1")
        print("green       2  bullet                            3    health   level 2")
        print("yellow      3  bullet   5  missile               5    health   level 3")
        print("blue        5  bullet   7  missile               10   health   level 4")
        print("red         7  bullet   10 missile   25 bomb     25   health   level 5")
        print("purple      10 bullet   15 missile   30 bomb     50   health   level 6")
        print("pink        12 bullet   20 missile   35 bomb     100  health   level 7")
        print("gold        15 bullet   25 missile   50 bomb     200  health   level 8")
        print("darkness    20 bullet   35 missile   75 bomb     1000 health   level 9")
        placeholder = input("Continue: ")
        print("-------------------------------------------------------------------------------")
        time.sleep(0.5)
        print("Upgrades    +1 bullet   +2 missile   +5 bomb     +5   health")
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