#the beggining of the hangman2.0  game.

import pygame
import time

pygame.init()
pygame.mixer.init(48000, -16, 1, 1024)
pygame.display.set_caption('Hang Man 2.0')     #pygame.display.set_caption to set the caption to the windows
screen0=pygame.display.set_mode((1000,700))    #pygame.display.set_mode to initialize a screen with the given size.

clock=pygame.time.Clock()

screen0.fill((0,0,0))                          #.fiil to fill the backgound with the given colour.
pygame.mixer.music.load('SOUNDS/intro.wav')    #pygame.mixer.music.load to load the music
pygame.mixer.music.play(-1)                    #pygame.mixer.music.play to play the music as long as the condition holds good.
                                               #Here continuously.


def message():
 font0=pygame.font.SysFont(None,100)           #initializing fonts using pygame.font.SysFont() with the font type and font size.
 font1=pygame.font.SysFont(None,200)
 font2=pygame.font.SysFont(None,30)

 screen0_text1=font1.render("2.0",True,(255,0,0))                           #font.render renders the font to the selected text.
 screen0_text2=font2.render("press tab to continue",True,(135,206,250))     #initializing text.

 screen0.blit(screen0_text1,[550,50])

 image1=pygame.image.load('IMAGES/i3.png')     #pygame.image.load to load an image.
 screen0.blit(image1,(200,50))                 #screen.blit to display on the screen.

 pygame.display.flip()

 image2=pygame.image.load('IMAGES/i2.png')
 screen0.blit(image2,(350,300))

 pygame.display.flip()

 screen0.blit(screen0_text2,(50,650))


running=True
message()
pygame.display.update()                        #pygame.display.update() to update the insertions on the screen.
time.sleep(1)                                  #the program sleeps for the mentioned amount of time becoming inactive.

while running:
 for event in pygame.event.get():   #pygame.event.get() to get the events correspondingly done on the screen using mouse,keyboard...
    if event.type==pygame.QUIT:     #to quit the program screen.
        running =False
    if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
        running =False
    if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:       #here we move to the next screen when we press tab.
       running =False                                                #this is done by closing the previous one and opening a new one
                                                                     #without time gap.

       screen1=pygame.display.set_mode((1000,700))
       screen1.fill((0,0,0))
       pygame.display.update()

       def message1():
        font1=pygame.font.SysFont(None,50)
        font2=pygame.font.SysFont(None,30)

        s1_text=font1.render("This is hangman 2.0!...",True,(255,255,0))
        s1_text1=font1.render("The rules are simple...",True,(255,255,0))
        s1_text2=font1.render("There are two players...",True,(255,255,0))
        s1_text3=font1.render("One player gives a word",True,(255,255,0))
        s1_text4=font1.render("...and the other guesses",True,(255,255,0))

        screen1.blit(s1_text,(50,50))
        time.sleep(1)
        pygame.display.update()

        screen1.blit(s1_text1,(50,150))
        time.sleep(1)
        pygame.display.update()

        screen1.blit(s1_text2,(50,250))
        time.sleep(1)
        pygame.display.update()

        screen1.blit(s1_text3,(50,450))
        time.sleep(1)
        pygame.display.update()

        screen1.blit(s1_text4,(380,570))
        screen_text5=font2.render("press tab to continue",True,(135,206,250))
        screen1.blit(screen_text5,(50,650))
        time.sleep(1)
        pygame.display.update()

       running1=True
       message1()
       while running1:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running1=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                running1=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                running1=False

                screen2=pygame.display.set_mode((1000,700))
                screen2.fill((0,0,0))
                pygame.display.update()

                def message2():
                 font1=pygame.font.SysFont(None,30)

                 s2_text=font1.render("Winnner hangs the loser!!!!..",True,(255,0,0))

                 s2_i1=pygame.image.load('IMAGES/i1.png')
                 s2_i2=pygame.image.load('IMAGES/i5.png')

                 s2_text1=font1.render("Winner takes",True,(255,255,0))
                 s2_text2=font1.render("Loser takes",True,(255,255,0))

                 screen2.blit(s2_text,(50,50))
                 time.sleep(1)                  #time.sleep() to make the program inactive for the mentioned no.of seconds.
                 pygame.display.update()

                 screen2.blit(s2_text1,(50,250))
                 screen2.blit(s2_i2,(400,150))
                 time.sleep(1)
                 pygame.display.update()

                 screen2.blit(s2_text2,(50,550))
                 screen2.blit(s2_i1,(400,450))

                 s2_text3=font1.render("press tab to continue",True,(135,206,250))
                 screen2.blit(s2_text3,(50,650))
                 pygame.display.update()


                running2=True
                message2()
                while running2:
                  for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                      running2=False
                    if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                      runnig2=False
                    if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                        running2=False
                        import WarningMessage  #import to import the contents of the mentioned file to this file
