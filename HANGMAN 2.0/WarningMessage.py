#WarningMesssage contains a warning message regarding the contents of the game which might seem disturbing to some people.The playersare allowed to move further in the game only on clicking the 'yes' button.


import pygame
import time

pygame.init()

#WarningM() functions displays a small box with a warning message and asks user to accept few conditions.It also displays two buttons 'yes' and 'no' which can be accessed through mouse click.

def WarningM():

        screen = pygame.display.set_mode((500,300))
        screen.fill((0,0,0))
        pygame.display.update()

	button1 = pygame.Rect(150, 200, 100, 50)        #pygame.Rect is used for creating rectangles at the given coordinates
	button2 = pygame.Rect(300, 200, 100, 50)        #with the given dimensions.
	    
	font=pygame.font.SysFont(None,30)               #initializing fonts
	font1=pygame.font.SysFont(None,30)

	text1=font1.render("WARNING!!!!!!",True,(255,255,0))                            #rendering fonts to text to be displayed 
	text2=font1.render("This game is just for fun",True,(255,255,0))                #on the screen.
	text3=font1.render("please donot try to imitate any of this",True,(255,255,0))
	text4=font1.render("Clicking yes would mean your agreement",True,(255,255,0))  

	texti=font.render("YES",True,(0,0,0))
	textj=font.render("NO",True,(0,0,0))
	     


	pygame.draw.rect(screen, (0,255, 0), button1)#pygame.draw.rectangle is used to draw the rectangle of desired colour on screen.
	pygame.draw.rect(screen, (255,0,0), button2)

	screen.blit(text1,(250,0))
	screen.blit(text2,(10,50))
	screen.blit(text3,(10,100))                     #displaying text on screen.
	screen.blit(text4,(10,150))

	screen.blit(texti,(170,210))                    #displaying text on the buttons
	screen.blit(textj,(320,210))

	pygame.display.update()                         #updating the screen with new insertions.
 
running_M=True
WarningM()
while running_M:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_M=False
                                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()          #getting the coordinates of the mouse pointer on the screen.
            if ((150<mouse_pos[0]<250 and 200<mouse_pos[1]<250) ):         #if the mouseclick is made on button1
                        running_M=False

                        pygame.mixer.music.load('SOUNDS/click.wav')        #sound plays on clicking in the area under button1
                        pygame.mixer.music.play(0)
                        time.sleep(1)

                        import Hangman1  
                                           # one can proceed further into the game only when one clicks on the 'yes' 
                                           #button and accepts not to imitate any of the content related to the game outside the game.

            if ((300<mouse_pos[0]<450 and 200<mouse_pos[1]<250) ):         #if the mouseclick is made on button2
                        running_M=False
      





