import pygame

class ThirdMenu:
    def __init__(self):
        self.font = pygame.font.Font('fonts/Alien.ttf', 80)
        self.title = self.font.render("This is Third!", True, (255, 255, 255))
        self.title_position = (10, 10)
        self.main_menu = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return self.main_menu
        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_position)