import pygame
import random

pygame.init()
WIDTH, HEIGHT= 900, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, paper, scissors, Smash")

#Load Image

bg = pygame.image.load("background.jpg")

buttons = {
    "rock" : pygame.image.load("r_button.png").convert_alpha(),
    "paper" : pygame.image.load("p_button.png").convert_alpha(),
    "scissors" : pygame.image.load("s_button.png").convert_alpha(),
}

choices_img = {
    "rock": pygame.image.load("rock (2).png").convert_alpha(),
    "paper": pygame.image.load("paper (2).png").convert_alpha(),
    "scissors": pygame.image.load("scissors (2).png").convert_alpha()
}

# Button positions
btn_pos = {
    "rock": pygame.Rect(30, 520, 300, 140),
    "paper": pygame.Rect(340, 520, 300, 140),
    "scissors": pygame.Rect(650, 520, 300, 140)
}

font = pygame.font.Font("Splatch.ttf", 90)

pl_score = 0
pc_score = 0


def draw_screen(text=""):
    screen.blit(bg, (0, 0))
    screen.blit(buttons["rock"], (20, 500))
    screen.blit(buttons["paper"], (330, 500))
    screen.blit(buttons["scissors"], (640, 500))

    if text:
        score_text = font.render(text, True, (255, 255, 255))
        screen.blit(score_text, (330, 0))


def get_winner(player, computer):
    if player == computer:
        return "draw"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"


run = True
clock = pygame.time.Clock()

while run:
    draw_screen(f"{pl_score} : {pc_score}")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for choice in btn_pos:
                if btn_pos[choice].collidepoint(mouse_pos):

                    player_choice = choice
                    computer_choice = random.choice(list(btn_pos.keys()))

                    # Draw choices
                    draw_screen()
                    screen.blit(choices_img[player_choice], (120, 200))
                    screen.blit(choices_img[computer_choice], (600, 200))
                    pygame.display.update()

                    pygame.time.delay(2000)  # ⏳ stay for 2 seconds

                    # Update score AFTER showing result
                    winner = get_winner(player_choice, computer_choice)
                    if winner == "player":
                        pl_score += 1
                    elif winner == "computer":
                        pc_score += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()