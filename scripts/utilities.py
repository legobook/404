import pygame, sys

def scale_image(image, size):
    # Return a scaled version of the provided image
    return pygame.transform.smoothscale(image, size)

def quit_program():
    sys.exit()
    pygame.quit()