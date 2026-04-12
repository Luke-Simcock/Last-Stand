enemy_bullet_size_w=0
enemy_bullet_size_h=0

enemy1_bullet1_shot=0
enemy1_bullet2_shot=0


class Enemy1(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                (enemy_size_w, enemy_size_h))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h/2 + enemy1_gap_to_border)

        def update(self):
            
            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame2.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame3.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame4.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)

            

            #Enemy Movement
            if enemy_time1 > 0:
                enemy_time1 -= 1

                #timer runs out
                if LorR_Enemy1 >= LorR_Calc1:  
                    self.rect.move_ip(-enemy_speed, 0)   #left
                elif LorR_Enemy1 < LorR_Calc1: 
                    self.rect.move_ip(enemy_speed, 0)   #right

            else:
                #Reset
                enemy_time1 = random.randint(45, 50)
                LorR_Enemy1 = enemy1.rect.x / 1543 * 100
                LorR_Calc1 = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT


        def __init__(self):
            super(Enemy3, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                (enemy_size_w, enemy_size_h))
            self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH/2, enemy_size_h/2 + enemy3_gap_to_border)

        def update(self):
            
            global enemy_time, LorR_Enemy, LorR_Calc, sprite_timer

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame1.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 75:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame2.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 50:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame3.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)
            
            if sprite_timer == 25:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Level 1/1/Frame4.png").convert(),
                    (enemy_size_w, enemy_size_h))
                self.surf.set_colorkey((255, 0, 255), RLEACCEL)

            

            #Enemy Movement
            if enemy_time3 > 0:
                enemy_time3 -= 1

                #timer runs out
                if LorR_Enemy3 >= LorR_Calc3:  
                    self.rect.move_ip(-enemy_speed, 0)   #left
                elif LorR_Enemy3 < LorR_Calc3: 
                    self.rect.move_ip(enemy_speed, 0)   #right

            else:
                #Reset
                enemy_time3 = random.randint(45, 50)
                LorR_Enemy3 = enemy1.rect.x / 1543 * 100
                LorR_Calc3 = random.randint(0, 100) 
                
            # Keep enemy on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

enemy1 = Enemy1()

class Enemy_Bullet1(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Bullet1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (enemy_bullet_size_w, enemy_bullet_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.x = (enemy1.rect.x+23)
            self.rect.y = (enemy1.rect.y)

        def update(self):
            
            global sprite_timer, enemy1_bullet1_shot, enemy1_bullet2_shot

            if sprite_timer == 100:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame1.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 80:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame2.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 60:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame3.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 40:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame4.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if sprite_timer == 20:
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Enemies/Weapons/Bullet/Frame5.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy1_bullet1_shot == True:
                enemy1_bullet1.rect.move_ip(0, +enemy_bullet_speed)
            if enemy1_bullet1_shot == False:
                enemy1_bullet1.rect.x = (enemy1.rect.x+23)
                enemy1_bullet1.rect.y = (enemy1.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy1_bullet1.rect.bottom >= SCREEN_HEIGHT:
                enemy1_bullet1_shot = False

            if enemy1_bullet2_shot == True:
                enemy1_bullet2.rect.move_ip(0, +enemy_bullet_speed)
            if enemy1_bullet2_shot == False:
                enemy1_bullet2.rect.x = (enemy1.rect.x+23)
                enemy1_bullet2.rect.y = (enemy1.rect.y)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_bullet_size_w, enemy_bullet_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy1_bullet2.rect.bottom >= SCREEN_HEIGHT:
                enemy1_bullet2_shot = False

class Enemy_Missile1(pygame.sprite.Sprite):

        def __init__(self):
            super(Enemy_Missile1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (enemy_missile_size_w, enemy_missile_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy1.rect.x  + enemy_size_h/2, enemy1.rect.y + enemy_missile_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy1_missile_shot

            if enemy1_missile_shot == True:
                enemy1_missile1.rect.move_ip(0, +enemy_missile_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame1.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame2.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame3.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame4.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Missiles/Frame5.png").convert(),
                        (enemy_missile_size_w, enemy_missile_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy1_missile_shot == False:
                enemy1_missile1.rect.x = (enemy1.rect.x + 30)
                enemy1_missile1.rect.bottom = (enemy1.rect.top)
                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_missile_size_w, enemy_missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
                
            if enemy1_missile1.rect.top >= SCREEN_HEIGHT:
                enemy1_missile_shot = False

class Enemy_Bomb1(pygame.sprite.Sprite):
        
        def __init__(self):
            super(Enemy_Bomb1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (enemy_bomb_size_w, enemy_bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy1.rect.x  - enemy_size_h/2, enemy1.rect.y - enemy_bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy1_bomb_shot

            if enemy1_bomb_shot == True:
                enemy1_bomb1.rect.move_ip(0, +enemy_bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame2.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame3.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame4.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame5.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy1_bomb_shot == False:
                enemy1_bomb1.rect.x = (enemy1.rect.x + 17)
                enemy1_bomb1.rect.bottom = (enemy1.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_missile_size_w, enemy_missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy1_bomb1.rect.bottom >= SCREEN_HEIGHT:
                enemy1_bomb_shot = False


        
        def __init__(self):
            super(Enemy_Bomb1, self).__init__()
            self.surf = pygame.transform.scale(
                pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                (enemy_bomb_size_w, enemy_bomb_size_h))
            self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.center = (enemy1.rect.x  - enemy_size_h/2, enemy1.rect.y - enemy_bomb_size_h/2)   

        def update(self):
            
            global sprite_timer, enemy_bomb_shot

            if enemy_bomb_shot == True:
                enemy_bomb1.rect.move_ip(0, +enemy_bomb_speed)

                if sprite_timer == 100:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame1.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 80:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame2.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 60:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame3.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 40:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame4.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

                if sprite_timer == 20:
                    self.surf = pygame.transform.scale(
                        pygame.image.load("C:/Sprites/Enemies/Weapons/Bombs/Frame5.png").convert(),
                        (enemy_bomb_size_w, enemy_bomb_size_h))
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if enemy_bomb_shot == False:
                enemy_bomb1.rect.x = (enemy1.rect.x + 17)
                enemy_bomb1.rect.bottom = (enemy1.rect.top)

                self.surf = pygame.transform.scale(
                    pygame.image.load("C:/Sprites/Player/Weapons/SetAs'00FFFF'.png").convert(),
                    (enemy_missile_size_w, enemy_missile_size_h))
                self.surf.set_colorkey((0, 255, 255), RLEACCEL)
            if enemy_bomb1.rect.bottom >= SCREEN_HEIGHT:
                enemy_bomb_shot = False
    
    
enemy1_bullet1 = Enemy_Bullet1()
enemy1_bullet2 = Enemy_Bullet1()
enemy1_missile1 = Enemy_Missile1()
enemy1_bomb1 = Enemy_Bomb1()
