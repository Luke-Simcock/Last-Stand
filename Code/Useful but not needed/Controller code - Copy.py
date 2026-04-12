import pygame

pygame.init()
pygame.joystick.init()

# Check if joystick is connected
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print("No controller detected!")




while True:  # Main game loop
    for event in pygame.event.get():

        #A and B button press detection
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:  # A button
                print("A pressed")
            if event.button == 5:  # B button
                print("B pressed")
        
        #Movement detection
        if event.type == pygame.JOYAXISMOTION:
            # Axis 0: Left/Right movement
            left_x = joystick.get_axis(0)  # -1 to 1
            
            # Only process if stick is moved beyond dead zone (e.g., >0.1)
            if abs(left_x) > 0.1:
                print(f"Left Stick: X={left_x:.2f}")
        
        #Trigger detection
        if event.type == pygame.JOYAXISMOTION:
            # Axis 5: Right trigger
            trigger = joystick.get_axis(5)  # -1 to 1
            if abs(trigger) > 0.1:
                if trigger > 0:
                    print("Trigger")
        

            # Axis 1: Up/Down movement
            #left_y = joystick.get_axis(1)  # -1 to 1