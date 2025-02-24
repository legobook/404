import pygame, datetime

class desktop:
    def __init__(self, screen, images):
        # Initialize the desktop
        self.screen = screen

        # Load the desktop logo
        self.logo = images["logo"]
        self.logo = pygame.transform.scale(self.logo, (700, 700))
        self.logo_rect = self.logo.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        # Load fonts
        self.font = pygame.font.Font("fonts/DejaVuSans.ttf", 14)
    
    def draw(self):
        # Draw the background
        self.screen.fill((32, 69, 90))

        # Draw the logo
        self.screen.blit(self.logo, self.logo_rect.topleft)

        # Draw the top bar
        pygame.draw.rect(self.screen, (54, 63, 65), (0, 0, self.screen.get_width(), 28))

        # Get current date and time
        date_time_surface = self.font.render(datetime.datetime.now().strftime("%a %d %b, %H:%M"), True, (255, 255, 255))
        date_time_rect = date_time_surface.get_rect(center=(self.screen.get_width() // 2, 14))

        # Draw the date and time
        self.screen.blit(date_time_surface, date_time_rect.topleft)