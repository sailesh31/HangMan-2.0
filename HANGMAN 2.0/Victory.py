#Victory is the follow up of the program displaying the new screen on player1's success which also allows the users to quit the game.

import pygame

import time

pygame.init()

#VictoryM() function display's a screen which contains the text regarding player1's win and also has a button which allows the player#to quit the game.

def VictoryM():
        pygame.mixer.music.load('SOUNDS/scary.wav')              #Playing background music as long as the function is running.       
        pygame.mixer.music.play(-1)

        screenV=pygame.display.set_mode([1000,700])              #Setting up a screen.
        screenV.fill((0,0,0))

        image_scary=pygame.image.load('IMAGES/i6.png')           #displaying image on the screen.
        screenV.blit(image_scary,(30,300))

	font =pygame.font.SysFont(None,40)                       #initializing fonts.
	font1 =pygame.font.SysFont(None,30)
	
        winner=font.render("WINNER IS : PLAYER1",True,(255,0,0))        #rendering fonts to texts

	text1_V=font.render("PLAYER 1,",True,(255,250,0))
	text2_V=font.render("PLAYER 2 WISHES YOU A",True,(255,250,0))
	text3_V=font.render("VERY HAPPY HALLOWEEEN",True,(255,250,0))

	screenV.blit(winner,(300,30))                            #dislaying text on the screen.
	screenV.blit(text1_V,(400,300))
	screenV.blit(text2_V,(400,400))
	screenV.blit(text3_V,(400,500))
	pygame.display.update()

	#button1 = pygame.Rect(300, 600, 100, 50)                #initializing a button in rectangular shape of required dimensions 
	button2 = pygame.Rect(550, 600, 100, 50)                 #at the required location.

	#texti=font1.render("RESTART",True,(0,0,0))              #text to be displayed on the button.
	textj=font1.render("QUIT",True,(0,0,0))

	#pygame.draw.rect(screenV, (0,255, 0), button1)          #displaying the button.
	pygame.draw.rect(screenV, (255,0,0), button2)

	#screenV.blit(texti,(304,620))                           #displaying text on the button.
	screenV.blit(textj,(570,620))

	pygame.display.update()

run_V=True
VictoryM()
while run_V:
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
       run_V=False

    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()                         #getting the position of mouse on the screen.
      #if ((300<mouse_pos[0]<400 and 600<mouse_pos[1]<650) ):
       #   run_V=False   
        #  import Hangman1 

      if ((550<mouse_pos[0]<650 and 600<mouse_pos[1]<650)):      #if mouse is clicked in this region on the screen 
           run_V=False                                           #Previous screen is closed.
           import About                                          #then About is imported.
