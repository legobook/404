import pygame, datetime
from utilities import *

class desktop:
    def __init__(self, screen, images):
        # Initialize the desktop
        self.screen = screen
        self.topbar_states = {"volume": 100, "wifi": 4}

        # Scaled properties
        self.topbar_size = 28
        self.topbar_icon_size = (self.topbar_size - 12, self.topbar_size - 12)
        self.topbar_icon_padding = 14

        # Load the desktop logo
        self.logo_image = scale_image(images["logo"], (600, 600))
        self.logo_rect = self.logo_image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        # Load the topbar icons
        self.power_image = scale_image(images["power"], self.topbar_icon_size) # Power
        self.power_rect = self.power_image.get_rect(topright=(self.screen.get_width() - self.topbar_icon_padding, 6))
        self.volume_image = scale_image(images["volume_3"], self.topbar_icon_size) # Volume
        self.volume_rect = self.volume_image.get_rect(topright=(self.screen.get_width() - (self.topbar_icon_padding + self.topbar_size), 6))
        self.wifi_image = scale_image(images["wifi_3"], self.topbar_icon_size) # Wifi
        self.wifi_rect = self.wifi_image.get_rect(topright=(self.screen.get_width() - (self.topbar_icon_padding + (self.topbar_size * 2)), 6))

        # Load fonts
        self.font = pygame.font.Font("fonts/dejavu_sans_bold.ttf", 14)
    
    def handle_event(self, event):
        # Check the event type
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check to see if the user clicked on the power button
            if self.power_rect.collidepoint(event.pos):
                quit_program()
    
    def draw_icon(self, image, rect):
        # Check to see if the mouse is hovering over the icon
        if rect.collidepoint(pygame.mouse.get_pos()):
            # Make the image slightly brighter
            brighter_image = image.copy()
            brighter_image.fill((30, 30, 30, 0), special_flags=pygame.BLEND_RGBA_ADD)

            # Apply the brightness
            image = brighter_image

        # Draw the icon
        self.screen.blit(image, rect)
    
    def draw(self):
        # Get current date and time
        date_time_surface = self.font.render("Thu 20 Jan, 21:34", True, (203, 203, 203))
        date_time_rect = date_time_surface.get_rect(center=(self.screen.get_width() // 2, self.topbar_size // 2))

        # Draw the background
        self.screen.fill((32, 69, 90))
        self.screen.blit(self.logo_image, self.logo_rect.topleft) # Logo

        # Draw the top bar
        pygame.draw.rect(self.screen, (54, 63, 65), (0, 0, self.screen.get_width(), self.topbar_size))
        self.screen.blit(date_time_surface, date_time_rect.topleft) # Date and time
        
        # Draw the top bar icons
        self.draw_icon(self.power_image, self.power_rect) # Power
        self.draw_icon(self.volume_image, self.volume_rect) # Volume
        self.draw_icon(self.wifi_image, self.wifi_rect) # Wifi