import pygame

pygame.init()

display = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

pygame.display.set_caption("Moving Ball")

x = 250
y = 250

width = 25
height = 25
vel = 10

run = True

while run:
	pygame.time.delay(10)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			
			run = False
	objective = pygame.key.get_pressed()
	
	if objective[pygame.K_LEFT] and x>0:
		x -= vel
		
	if objective[pygame.K_RIGHT] and x<500-width:
		x += vel
	
	if objective[pygame.K_UP] and y>0:
		y -= vel
		
	if objective[pygame.K_DOWN] and y<500-height:
		y += vel
		
	pygame.draw.circle(display, (255, 0, 0), (x, y), 25)
	pygame.display.update()
	clock.tick(60)
pygame.quit()   
