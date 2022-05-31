import pygame
import sys
import copy
import random
import time
import psycopg2

if __name__ == "__main__":
    playerName = input("Enter your name:")

config = psycopg2.connect(**params)
current = config.cursor()


pygame.init()


scale = 10
score = 0
level = 0
SPEED = 10

food_x = 10
food_y = 10
food_w = 0

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

background = (0, 0, 0)
snake_colour = (236, 240, 241)
food_colour = (148, 49, 38)
snake_head = (255, 0, 0)




class Food:
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, 500/scale-1)*scale
        food_y = random.randrange(1, 500/scale-1)*scale

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))
    
    def food_weight(self):
        global food_w
        food_w = random.randint(1, 2)
        return food_w


    

def show_score():
    font = pygame.font.SysFont("Copperplate Gothic Bold", 20)
    text = font.render("Score: " + str(score), True, snake_colour)
    display.blit(text, (scale, scale))

def show_level():
    font = pygame.font.SysFont("Copperplate Gothic Bold", 20)
    text = font.render("Level: " + str(level), True, snake_colour)
    display.blit(text, (90 - scale, scale))

class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def reset(self):
        self.x = 500/2-scale
        self.y = 500/2-scale
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    def level(self):
        global level
        if self.length % 6 == 0:
            return True
            
            

    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length-2])

    
    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i-1])
            i -= 1
        self.history[0][0] += self.x_dir*scale
        self.history[0][1] += self.y_dir*scale




def gameLoop():

    global score
    global level
    global SPEED

    snake = Snake(500/2, 500/2)
    food = Food()
    food.new_location()

    time_delay = 5000 # 5 seconds
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, time_delay)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1

                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0

        display.fill(background)

        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()
        
          
        if snake.check_eaten():
            food.new_location()
            score += food.food_weight()
            snake.grow()

        if snake.level():
            food.new_location()
            level += 1
            SPEED += 2.5
            snake.grow()
        
        #position update of food each 5 seconds
        if event.type == timer_event:
            food.new_location()
        
            
            

        if snake.death():
            score = 0
            level = 0
            font = pygame.font.SysFont("Copperplate Gothic Bold", 50)
            text = font.render("Game Over!", True, snake_colour)
            display.blit(text, (500/2-50, 500/2))
            insert_into = '''
            INSERT INTO records VALUES (%s, %s);
            '''
            try:
                get = f'''
                    SELECT record FROM records WHERE name = '{playerName}';
                '''
                current.execute(get)
                output = current.fetchone()
                high_score = output[0]
                exist = True
            except:
                pass
            if exist:
                if score > high_score:
                    update = '''
                        UPDATE records SET record = %s WHERE name = %s;
                    '''
                    current.execute(update,(score,playerName))
            else:
                current.execute(insert_into, (f'{playerName}', f'{score}'))
            current.close()
            config.commit()
            config.close()
            
            pygame.display.update()
            time.sleep(3)
            snake.reset()

        if snake.history[0][0] > 500:
            snake.history[0][0] = 0
        if snake.history[0][0] < 0:
            snake.history[0][0] = 500

        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        pygame.display.update()
        clock.tick(SPEED)

gameLoop()



