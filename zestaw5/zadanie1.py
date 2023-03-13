import pygame, sys 
pygame.init() 

def main():
    
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    positionx = width
    positiony = height
    
    clock = pygame.time.Clock()
    
    pygame.display.set_caption('Tytul naszego okienka')
    icon = pygame.image.load(r'C:\Users\jasie\Desktop\Python\zestaw5\moon.jpg')
    pygame.display.set_icon(icon)
    
    pygame.mixer.music.load(r'C:\Users\jasie\Desktop\Python\zestaw5\music.mp3')
    pygame.mixer.music.play(-1)
    
    speed = [0, 0]
    accel = [0.1, 0.1]
    
    image = pygame.image.load(r'C:\Users\jasie\Desktop\Python\zestaw5\moon.jpg')
    image = pygame.transform.scale(image, size)
    
    surf_center = ( 
        (width-image.get_width())/2, 
        (height-image.get_height())/2
    )
    
    screen.blit(image, surf_center)
    pygame.display.flip()
    
    ball = pygame.image.load(r'C:\Users\jasie\Desktop\Python\zestaw5\ball.gif') 
    screen.blit(ball, (width/2, height/2))
    ballrect = ball.get_rect(center=(positionx / 2, positiony / 2))
    pygame.display.flip()
    a = 1
    b = 1
    keyList = [1]
    step = 10
       
    while True:
        clock.tick(60)
        pygame.time.delay(50)
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit() 
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: sys.exit()
        
        if keys[pygame.K_UP]:
            if(keyList[-1] != 1):
                speed = [0, 0]
                accel = [0.1, 0.1]
            else:
                speed[0] = speed[0] + accel[0]
                speed[1] = speed[1] + accel[1]
                
            if ballrect.top > 0:
                positiony -= step
            ballrect = ball.get_rect(center=(positionx / 2, positiony / 2))
            keyList.append(1)
            accel[1] = accel[1] - 1.5
        elif keys[pygame.K_DOWN]:
            if(keyList[-1] != 2):
                speed = [0, 0]
                accel = [0.1, 0.1]
            else:
                speed[0] = speed[0] + accel[0]
                speed[1] = speed[1] + accel[1]

            if ballrect.bottom < height: 
                positiony += step
            ballrect = ball.get_rect(center=(positionx / 2, positiony / 2))
            keyList.append(2)
            accel[1] = accel[1] + 1.5
            
        elif keys[pygame.K_RIGHT]:
            if(keyList[-1] != 3):
                speed = [0, 0]
                accel = [0.1, 0.1]
            else:
                speed[0] = speed[0] + accel[0]
                speed[1] = speed[1] + accel[1]
            
            if ballrect.right < width:
                positionx += step         
            ballrect = ball.get_rect(center=(positionx / 2, positiony / 2))
            keyList.append(3)
            accel[0] = accel[0] + 1.5
            
        elif keys[pygame.K_LEFT]:
            if(keyList[-1] != 4):
                speed = [0, 0]
                accel = [0.1, 0.1]
            else:
                speed[0] = speed[0] + accel[0]
                speed[1] = speed[1] + accel[1] 
                
            if ballrect.left > 0:
                positionx -= step
            ballrect = ball.get_rect(center=(positionx / 2, positiony / 2))
            keyList.append(4)
            accel[0] = accel[0] - 1.5
        
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        
  
        screen.blit(image,surf_center)
        screen.blit(ball,ballrect)
        pygame.display.flip()
            
if __name__ == '__main__': 
    main() 
    pygame.quit() 
    sys.exit()