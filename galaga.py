import pygame

WIDTH=600
HEIGHT=600
TITLE="GALAGA GAME"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

score=0
bugs_left=[]
bullet_amount=10
bullets=[]
level=1
go=False

bg1=pygame.image.load("space bg.png")
bg2=pygame.image.load("bullet.png")
bg3=pygame.image.load("galagabug.png")
bg4=pygame.image.load("galagaship.png")

class Ship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=bg4
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def move(self,keys):
        if keys[pygame.K_a]:
            self.rect.x=self.rect.x-2
        if keys[pygame.K_d]:
            self.rect.x=self.rect.x+2
s1=Ship(250,500)
ships=pygame.sprite.Group()
ships.add(s1)


while go==False:
    screen.blit(bg1,(0,0))
    ships.draw(screen)
    bullets.draw(screen)
    keys_pressed=pygame.key.get_pressed()
    s1.move(keys_pressed)
    for event in pygame.event.get(): 
      if event.type==pygame.QUIT:
        go=True
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            bullet=Bullets(s1.rect.x+100,s1.rect.y) 
            bullets.add(bullet)
    if len(bullets)>0:
        for bullet in bullets:
            bullet.move()
    pygame.display.update()
    