import pygame, random

pygame.init()


FPS = 30
SPEED = 15
SPEED=FPS/SPEED
screen_width = 800
screen_height = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
SCORE1, SCORE2 = 0, 0
BALL_SIZE = 1000 / 20  # change the number after 1000/

LINE = ((screen_width // 2, 0), (screen_width // 2, screen_height))

# Set up the font
font = pygame.font.Font(None, 50)

class Element:
    def __init__(self, position, element):
        if element == "player":
            self.width = screen_width // 50
            self.height = screen_height // 5
            self.center = (screen_width / 2, screen_height / 2)
            self.score = 0
            if position == "left":
                self.x = 0
                self.y = (screen_height // 2)
            elif position == "right":
                self.x = screen_width - self.width
                self.y = screen_height // 2
        elif element == "ball":
            self.width = screen_width / BALL_SIZE
            self.height = self.width
            self.x = 0
            self.y = 0
            self.center = (screen_width / 2, screen_height / 2)
            self.x_speed, self.y_speed = 1, 1

    def randomize(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.x_speed = random.choice([-1, 1])
        self.y_speed = random.choice([-1, 1])

player1 = Element("left", "player")
player2 = Element("right", "player")
ball = Element("ball", "ball")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w]:
        if player1.y > 0:
            player1.y -= FPS/SPEED**2
    if keys_pressed[pygame.K_s]:
        if player1.y < screen_height - player1.height:
            player1.y += FPS/SPEED**2
    if keys_pressed[pygame.K_UP]:
        if player2.y > 0:
            player2.y -= FPS/SPEED**2
    if keys_pressed[pygame.K_DOWN]:
        if player2.y < screen_height - player2.height:
            player2.y += FPS/SPEED**2

    if ball.y <= 0:  # Touches the top of the screen
        ball.y = 0  # Reset position to avoid going off-screen
        ball.y_speed = -ball.y_speed  # Reverse the vertical velocity

    if ball.y >= screen_height:  # Touches the bottom of the screen
        ball.y = screen_height  # Reset position to avoid going off-screen
        ball.y_speed = -ball.y_speed  # Reverse the vertical velocity
    text=font.render(f"Ball out of the court",True,"white")
    # text_width, text_height = text.get_size()    
    if ball.x <= 0:
        player2.score += 1
        screen.fill("black")
        # screen.blit(font.render(f"Ball out of the court", True, "white"), (screen_width//2-text_width//2, screen_height//2))
        pygame.display.flip()
        pygame.time.delay(500)
        ball.randomize()
        continue
    if ball.x >= screen_width:
        player1.score += 1
        screen.fill("black")
        # screen.blit(font.render(f"Ball out of the court", True, "white"), (screen_width//2-text_width//2, screen_height//2))
        pygame.display.flip()
        pygame.time.delay(500)
        ball.randomize()
        continue
    ball.x += ball.x_speed * FPS/SPEED**2
    ball.y += ball.y_speed * FPS/SPEED**2

    player1.rect = pygame.Rect(player1.x, player1.y, player1.width, player1.height)
    player2.rect = pygame.Rect(player2.x, player2.y, player2.width, player2.height)
    ball.rect = pygame.Rect(ball.x, ball.y, ball.width, ball.height)

    if player1.rect.colliderect(ball.rect):
        ball.x_speed = 1
    if player2.rect.colliderect(ball.rect):
        ball.x_speed = -1

    screen.fill("black")
    score_text = font.render(f"Player1: {player1.score}        Player2: {player2.score}", True, "white")
    text_width, text_height = score_text.get_size()
    screen.blit(score_text, ((screen_width - text_width) // 2, 10))

    pygame.draw.ellipse(screen, "white", ball.rect, int(BALL_SIZE))
    pygame.draw.line(screen, "white", LINE[0], LINE[1], 5)
    pygame.draw.rect(screen, "white", player1.rect)
    pygame.draw.rect(screen, "white", player2.rect)

    pygame.display.flip()
    clock.tick(FPS)
