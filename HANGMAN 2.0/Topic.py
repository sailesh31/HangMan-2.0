#Topic is used to take input from player1 and show the topic related to the word, player2 is suppoused to guess given by player1.

import pygame

pygame.init()

screen_T=pygame.display.set_mode((1000,500))                     #setting up the screen.
screen_T.fill((0,0,0)) 

font=pygame.font.SysFont(None,50)                                #initializing the fonts.
font1=pygame.font.SysFont(None,60)
font2=pygame.font.SysFont(None,30)

s_text1=font.render("PLAYER1",True,(123,213,0))                          #rendering fonts to text.
s_text2=font.render("PLEASE SPECIFY THE TOPIC:",True,(123,213,201))
s_text3=font2.render("close the tab to continue",True,(90,90,90))

screen_T.blit(s_text1,(50,100))
screen_T.blit(s_text2,(50,300))                                  #displaying text on screen.
screen_T.blit(s_text3,(30,470))


topic=""                                                         #initializing an empty string 
running_T=True
while running_T:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key!=pygame.K_TAB and event.key!= pygame.K_BACKSPACE:
          topic+=(chr(event.key))             #taking word input from the user by adding the letters typed at the end of the string.
 
        t=font1.render(topic,True,(255,0,0))                     #displaying the letters typed on the screen
        t1=font1.render(topic,True,(0,0,0))
        screen_T.blit(t,(570,295))
        pygame.display.update()

        if event.type ==pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            topic=topic[:-1:]                            #using back space feature by displaying the word excluding the last letter. 
            t=font1.render(topic,True,(255,0,0))
            screen_T.blit(t1,(570,295))                          #covering the previous word.
            pygame.display.update()
            screen_T.blit(t,(570,295))
            pygame.display.update()                              #displaying the new word. 
        
        if event.type == pygame.QUIT:
           running_T=False

        if event.type ==pygame.KEYDOWN and event.key ==pygame.K_TAB:
            running_T=False
