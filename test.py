import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Epic Genetic Simulation")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60


gens_colecction = "start_gen_1start_gen_1end" \
"move_leftstep_leftend" \
"move_rightstep_rightend"

class Cell:
    def __init__(self, gens, color, number, x, y):
        self.color = color
        self.number = number
        self.x = x
        self.y = y
        self.gens = gens
        self.morph_gen_list = []

    def gen_expresion(self):
        output_marphogen = []
        for morph in self.morph_gen_list:

            start_marker = morph
            start_index = self.gens.find(start_marker)
            if start_index == -1:
                continue

            read_start = start_index + len(start_marker)
            end_index = self.gens.find("end", read_start)
            if end_index == -1:
                continue

            gene_product = self.gens[read_start:end_index]
            if gene_product == '':
                gene_product = morph

            output_marphogen.append(gene_product)
        self.morph_gen_list = output_marphogen

    def cell_functions_realisation(self):
        working_morph_gen_list = self.morph_gen_list.copy()
        for morph in working_morph_gen_list:
            if morph == "step_left":
                self.x -= 5
                self.morph_gen_list.remove(morph)
                return
            if morph == "step_right":
                self.x += 5
                self.morph_gen_list.remove(morph)
                return
        

    def cell_draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 30, width=0)


cell = Cell(gens_colecction, "red", 1, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
cell.morph_gen_list = ["move_left","move_left","move_left","move_left","move_left","move_left","move_left"]


bakteria = Cell(gens_colecction, "green", 1, SCREEN_WIDTH//3, SCREEN_HEIGHT//3)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((225, 225, 225))
     

    cell.gen_expresion()
    cell.cell_functions_realisation()
    cell.cell_draw()
    pygame.time.delay(50)

    pygame.display.flip()

   
    clock.tick(FPS)

pygame.quit()
sys.exit()