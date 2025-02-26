import pygame, os
from desktop import desktop
from utilities import *

class game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.font.init()

        # Get the resolution of the user's monitor
        screen_info = pygame.display.Info()
        window_resolution = (screen_info.current_w, screen_info.current_h)

        # Start the screen and clock
        self.screen = pygame.display.set_mode(window_resolution, pygame.FULLSCREEN | pygame.NOFRAME)
        #self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Set the name of the window
        pygame.display.set_caption("MangOS")

        # Load all images from the images directory
        images = self.load_images()

        # Create the desktop
        self.desktop = desktop(self.screen, images)
    
    def load_images(self):
        images = {}

        # Loop through all the files in the directory and load the images
        for root, _, files in os.walk("images"):
            for i in files:
                image = pygame.image.load(os.path.join(root, i))
                images[os.path.splitext(i)[0]] = image

        return images

    def run(self):
        while True:
            # Calculate delta time
            delta_time = self.clock.tick(72) / 1000

            for i in pygame.event.get():
                self.desktop.handle_event(i)

                if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
                    quit_program()

            # Draw the desktop
            self.desktop.draw()

            # Update the screen
            pygame.display.flip()

if __name__ == "__main__":
    game().run()