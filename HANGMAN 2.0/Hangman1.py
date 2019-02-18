import pygame

import time

pygame.init()

word1=""                                                      #initializing an empty string.

screen0=pygame.display.set_mode((1000,700))                   #setting up a screen and filling the background.
screen0.fill((0,0,0))

pygame.mixer.music.load('SOUNDS/intro.wav')                   #playing background music
pygame.mixer.music.play(-1)

font=pygame.font.SysFont(None,40)                             #initializing a font.

s0_text1=font.render("PLAYER 1",True,(0,250,0))               #rendering font to text.
s0_text2=font.render("Please enter the word of desire:",True,(0,250,0))

screen0.blit(s0_text1,(100,50))                               #blitting text on the screen.
screen0.blit(s0_text2,(100,300))

pygame.display.update()

font1=pygame.font.SysFont(None,30)

s0_text3=font1.render("press tab to continue",True,(135,206,250))
screen0.blit(s0_text3,(100,650))
pygame.display.update()                                       #updating the screen with new insertions.


running0=True

while running0:
   for event in pygame.event.get():
      if event.type==pygame.QUIT:                             #exiting from the screen.
          running0=False
      if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
          running0=False
      if event.type == pygame.KEYDOWN:                      #taking input from the player1 by adding the new letter typed at the end. 
               #runningi =False
                if event.key == pygame.K_a:
                    word1+=(chr(event.key))
                if event.key == pygame.K_b:
                    word1+=(chr(event.key))
                if event.key == pygame.K_c:
                    word1+=(chr(event.key))
                if event.key == pygame.K_d:
                    word1+=(chr(event.key))
                if event.key == pygame.K_e:
                    word1+=(chr(event.key))
                if event.key == pygame.K_f:
                    word1+=(chr(event.key))
                if event.key == pygame.K_g:
                    word1+=(chr(event.key))
                if event.key == pygame.K_h:
                    word1+=(chr(event.key))
                if event.key == pygame.K_i:
                    word1+=chr(event.key)
                if event.key == pygame.K_j:
                    word1+=chr(event.key)
                if event.key == pygame.K_k:
                    word1+=chr(event.key)
                if event.key == pygame.K_l:
                    word1+=chr(event.key)
                if event.key == pygame.K_m:
                    word1+=chr(event.key)
                if event.key == pygame.K_n:
                    word1+=chr(event.key)
                if event.key == pygame.K_o:
                    word1+=chr(event.key)
                if event.key == pygame.K_p:
                    word1+=chr(event.key)
                if event.key == pygame.K_q:
                    word1+=chr(event.key)
                if event.key == pygame.K_r:
                    word1+=chr(event.key)
                if event.key == pygame.K_s:
                    word1+=chr(event.key)
                if event.key == pygame.K_t:
                    word1+=chr(event.key)
                if event.key == pygame.K_u:
                    word1+=chr(event.key)
                if event.key == pygame.K_v:
                    word1+=chr(event.key)
                if event.key == pygame.K_w:
                    word1+=chr(event.key)
                if event.key == pygame.K_x:
                    word1+=chr(event.key)
                if event.key == pygame.K_y:
                    word1+=chr(event.key)
                if event.key == pygame.K_z:
                    word1+=chr(event.key)
                if event.key == pygame.K_BACKSPACE:  #duplicating backspace feature by displaying replacing th eoriginal word
                     word1=(word1[:-1:])             #with the last letter removed.
      #text=font.render(word1,True,(255,255,255)) 
      #screen.blit(text,(600,300))                  #these lines are commented so as to prevent the display of the    
      #pygame.display.update()                      #word to player2
                                           
      if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:  
                                                    #closing the previous screen and displaying a new one.
        running0=False

        #screen0=pygame.display.set_mode((1000,700))
        #screen0.fill((0,0,0))
        #font=pygame.font.SysFont(None,40)
        #t=font.render("PLEASE SPECIFY THE TOPIC OF THE WORD",True,(0,200,0))

        screen1=pygame.display.set_mode((1000,700))
        screen1.fill((0,0,0))

        font=pygame.font.SysFont(None,100)
        font1=pygame.font.SysFont(None,30)

        s1_text1=font.render("LETS <HANG>",True,(0,255,0))
        s1_text2=font.render("MAN",True,(0,255,0))
        
        screen1.blit(s1_text1,(100,250))
        
        s1_i1=pygame.image.load('IMAGES/i4.png')
        screen1.blit(s1_i1,(600,150))
        screen1.blit(s1_text2,(800,250))

        s1_text3=font1.render("press tab to continue",True,(135,206,250))
        screen1.blit(s1_text3,(50,650))

        pygame.display.update()

        running1=True

        while running1:
          for event in pygame.event.get():
            if event.type==pygame.QUIT:
              running1=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
              running1=False                 
            if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
              running1=False
        
              import Topic       #importing the contents in topic file.

              screen2= pygame.display.set_mode((1000,700))
              l=[]              #an empty list
              l=list(word1)     #list containing all the letters in the given word
              n=len(l)          #length of the list l
              m=[]              #a list containing unique elements of the list l
              for x in l:
                if  x not in m:
                  m.append(x)
              n1=len(m)         #length of list m

              screen2.fill((0,0,0))
              
              pygame.draw.rect(screen2, (255,255,0),[30,30,400,500])
              pygame.draw.rect(screen2, (255,255,255),[35,35,390,490]) 
              pygame.display.update()

              font=pygame.font.SysFont(None,50)
              font1=pygame.font.SysFont(None,30)
              
              s2_text1 = font.render("_",True,(255,255,0))
              s2_text2 = font1.render("Guess a letter:",True,(255,255,0))
              
              lx=[]   #an empty list to store the x-coordinates of the dashes 
              ly=[]   #an empty list to store the y-coordinates of the dashes

              #a function used to print the blancks on screen equal to the number of letters in the word.
              def print_dashes():
                               
                a=n/13
                w=n%13
                if(a<1):                 #if less than 13 letters are there they are printed on the screen continuously
                  y=0
                  while(y<w):                  
                     screen2.blit(s2_text1,(450+(40*y),300))
                     lx.append(450+(40*y))
                     ly.append(300)
                     y+=1
                   
                if(a>=1):               #else 13 per line ar eprinted and the extra ones are printed on the next line.
                   q=0
                   while(q<=a-1):
                     y=0
                     while(y<13):
                       screen2.blit(s2_text1,(450+(40*y),300+(80*q)))
                       lx.append(450+(40*y))
                       ly.append(300+(80*q))
                       y+=1
                     q+=1
                   
                   h=0
                   while(h<w):
                    screen2.blit(s2_text1,(450+(40*h),300+(80*q+1)))
                    h+=1   

                screen2.blit(s2_text2,(100,600))
                pygame.display.update()

              image1=pygame.image.load('IMAGES/h1.png')        #loading image
              image1=pygame.transform.scale(image1,(360,460))  #adjusting the size of the image to the size we require
              image2=pygame.image.load('IMAGES/h2.png')
              image2=pygame.transform.scale(image2,(360,460))
              image3=pygame.image.load('IMAGES/h3.png')
              image3=pygame.transform.scale(image3,(360,460))
              image4=pygame.image.load('IMAGES/h4.png')
              image4=pygame.transform.scale(image4,(360,460))
              image5=pygame.image.load('IMAGES/h5.png')
              image5=pygame.transform.scale(image5,(360,460))

              l1=[image1,image2,image3,image4,image5]          #A list containg the five images.
               

              #a function to take input from player2 who is guessing the word.
              #and to show whether the guess is correct or wrong and does little insertiond=s on the screen. 
              #also checks if the word is guessed entirely.
              def input_Guess():
                  lunique=[]                   #To prevent repetition of printing of correct letter
                  lguess=[]                    #To ckeck if the whole word is guessed
                  lunique1=[]                  #To prevent repetetion of wrong letters
                  i=0                          #To print the guessed letters
                  j=0                          #To give five chances to player2
                  while(j<5):
                      for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            exit()
                        if event.type==pygame.KEYDOWN:
                              a=True
                              d=(chr(event.key))
                              p=font1.render(d,True,(255,255,0)) 
                              player2=font1.render("Player 2",True,(0,255,0))
                              screen2.blit(player2,(30,10))
                              screen2.blit(p,(250+20*i,600))
                              pygame.display.update()
                              k=0
                              while(k<n): 
                                  if(l[k]==d):                                  #if guessed letter is there in the word.
                                      screen2.blit(p,(lx[k],ly[k]))             #displaying correct letter at the corresponding space 
                                      pygame.mixer.music.load('SOUNDS/yes.mp3') #sound to be played when a correct letter is guessed.
                                      pygame.mixer.music.play(0)
                                      pygame.display.update()
                                      lguess.append(d)
                                      if d  not in lunique:
                                        lunique.append(d) 
                                        i+=1 
                                      a=False
                                      k+=1
                                  
                                  else: 
                                      k+=1
                                  if(len(lunique)==n1 and len(lguess)==n):    #player 2 wins the game by guessing the entire word.
                                      word=font.render(word1,True,(255,255,0))
                                      player2=font1.render("Player 2",True,(0,0,0))
                                      screen2.blit(player2,(30,10))
                                      pygame.display.update()
                                      player1=font1.render("Player 1",True,(255,255,0)) #player 1 is hanged.
                                      screen2.blit(player1,(30,10))
                                      pygame.display.update()
                                      screen2.blit(l1[4],(30,30))
                                      pygame.display.update()
                                      #screen2.fill((255,255,255))
                                      
                                      #pygame.display.update()
                                      screen2.blit(word,(600,200)) #displaying the complete word.
                                      pygame.display.update()
                                      time.sleep(4)
                                      
                                      import Loss   #player 2 wins the game.
                                      
                                  if(a==True and  k==n-1 and d!=l[k]):
                                    if(d not in lunique1):    
                                      lunique1.append(d)                                 #not having the guessed letter in the word.
                                      screen2.blit(l1[j],(30,30))      #a picture analogous to showing that the player2 lost a chance.
                                      #screen2.blit(p,(700+20*i,600))
                                      pygame.mixer.music.load('SOUNDS/no.wav') #sound to be played when a wrong letter is guessed
                                      pygame.mixer.music.play(0)
                                      pygame.display.update()
                                      i+=1
                                      j+=1
                                    else:
                                      i+=1
                                 
                                 # if(a==True and  k==n-1 and d==l[k]):
                                   #  screen2.blit(p,lx[k],ly[k])
                                    # pygame.display.update()


                      if(j==5):                                      #player2 is out of chances.
                        word=font.render(word1,True,(255,0,0))
                        screen2.blit(word,(700,200))                 #displaying the complete word at end of the game.
                        pygame.display.update()
                        time.sleep(4)
                
                        import Victory                               #if player1 wins the game Victory is imported.
                
                        
              running3=True
              print_dashes( )                                        #calling the functions.
              input_Guess()
              
              while running3: 
            
                for event in pygame.event.get():
                   if event.type==pygame.QUIT:
                       running3=False
