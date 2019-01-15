#import libraries
import pygame
import random
import os

pygame.init()

pygame.mixer.init()


#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,200)
green=(0,255,0)

#creating window
width=900
height=600

window=pygame.display.set_mode((width,height))
#for BG Image
bgimage = pygame.image.load("bg1.jpg")
bgimage = pygame.transform.scale(bgimage, (width, height)).convert_alpha()

#set display title
pygame.display.set_caption("Snake")
pygame.display.update() #it updates the display

clock=pygame.time.Clock()
font=pygame.font.SysFont("comicsansms", 43)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    window.blit(screen_text,[x,y])

def plt_snake(window,color,snake_list,snake_size):
    for x,y in snake_list: 
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

#home screen
def home_screen():
    exit_game = False
    while not exit_game:
        window.fill((233,210,229))
        
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('theme.mp3')
                    pygame.mixer.music.play()
                    gameLoop()

        pygame.display.update()
        clock.tick(30)


#game Loop
def gameLoop():

    #Game specific Var(s)
    exit_game=False
    game_over=False
    pos_x=35
    pos_y=40
    snake_size=20
    apple_size=20

    fps=30
    velo_x=0
    velo_y=0
    snake_list=[]
    snake_length=1
    #check the txt file exist or not
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")
            
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()


    score=0

    apple_x=random.randint(15,width/1.5)
    apple_y=random.randint(15,height/1.5)
    

    while not exit_game:

        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            window.fill(white)
            
            text_screen("Game Over! Enter to Continue",red,190,250)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('theme.mp3')
                        pygame.mixer.music.play()
                        gameLoop()

        else:
            
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:

                    if event.key==pygame.K_RIGHT:  #for right direction
                        velo_x=8
                        velo_y=0
                        
                    if event.key==pygame.K_LEFT: #for left direction
                        velo_x=-8
                        velo_y=0
                        
                    if event.key==pygame.K_UP: #for upward directon
                        
                        velo_y=-8
                        velo_x=0
                        
                    if event.key==pygame.K_DOWN: #for downward direction
                        
                        velo_y=8
                        velo_x=0

            if abs(pos_x-apple_x)<22 and abs(pos_y-apple_y)<22:
                score=score+10
                             
                apple_x=random.randint(10,width/1.25)
                apple_y=random.randint(10,height/1.25)

                snake_length+=5
                if score>int(hiscore):
                    hiscore = score

            pos_x=pos_x+velo_x
            pos_y=pos_y+velo_y
            
            window.fill(white)
            window.blit(bgimage,(0,0))
            #displaying highscore 
            text_screen("Score: "+str(score) + "  High Score: "+str(hiscore),green,5,5) #it makes score screen
            

            head=[]
            head.append(pos_x)
            head.append(pos_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()

            if pos_x<0 or pos_x>width or pos_y<0 or pos_y>height:
                game_over=True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
            
            pygame.draw.rect(window,red,[apple_x,apple_y,apple_size,apple_size])

            plt_snake(window,black,snake_list,snake_size)
        
        pygame.display.update()
        clock.tick(fps)

                    
    #quit game
    pygame.quit()
    quit()

#call the main function
home_screen()











