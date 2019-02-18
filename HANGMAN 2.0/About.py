#About file contains the details of the program developers,resources used in development of the game which are displayed after the  

import pygame
 
import time

pygame.init()

#The function AboutM() displays a new screen with the following mentioned content.

def AboutM():

	screenA=pygame.display.set_mode([800,600])                #screen being setup
 	screenA.fill((0,0,0))                                     #filling the screen background.

	font=pygame.font.SysFont(None,30)                         #initializong fonts being used
	font1=pygame.font.SysFont(None,40)      
                                                                               
	s_t1=font1.render("ABOUT HANGMAN 2.0",True,(0,255,0))                       # text to be displayed on the screen
	s_t2=font.render("<o> Developed by - 2pcoderStudios",True,(255,255,0))      # are being rendered with the fonts.
	s_t3=font.render("<o> Developers -K.Sailesh and prakash" ,True,(255,255,0))
	s_t4=font1.render("CREDITS",True,(0,255,0))

	s_t5=font.render(">> Images -Google",True,(255,255,0))
	s_t6=font.render(">> Sounds -Freesounds.org",True,(255,255,0))

	s_t7=font1.render("THANK YOU ENJOY HANGING",True,(255,0,0))

	screenA.blit(s_t1,(30,30))
	screenA.blit(s_t2,(30,130))                               #bliting the text on the screen at the required location.
	screenA.blit(s_t3,(30,200))
	screenA.blit(s_t4,(30,300))
	screenA.blit(s_t5,(30,350))
	screenA.blit(s_t6,(30,400))
	screenA.blit(s_t7,(100,500))
	    
	pygame.display.update()                                   #updating the display of the screen with the new insertions on it.

AboutM()
time.sleep(5)                                                     #program sleeps for 5 seconds and then closes.
quit()


