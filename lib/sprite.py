import logging

import pygame
import pygame.gfxdraw


class Bullet(pygame.sprite.Sprite):

    """
    Base class for simple bullets.

    Each bullet is a coloured circle that moves from right to left
    across the screen. It has a black border.

    Extends pygame.sprite.Sprite.
    """

    speed = 5

    def __init__(self, colour, radius, x=0, y=0):
        """
        Create a new bullet using the given parameters. The bullet is
        added to any Groups in the groups attribute on creation.
        """
        try:
            super().__init__(self.groups)
        except TypeError:
            logging.exception((
                "Attribute 'groups' of class Bullet contains a non-Group or",
                "is undefined."
            ))
            raise

        self.colour = colour

        self.rect = pygame.Rect(x, y, 0, 0)
        self.set_radius(radius)

    def update(self):
        """ Move from right-to-left. """
        self.rect.move_ip(-self.speed, 0)

    def set_radius(self, radius):
        """
        Update the bullet radius then update the visible attributes to
        reflect the change.

        The topleft position of the 'rect' attribute is preserved.
        """
        self.radius = radius

        # Redraw visible image; preserve position
        self.image = pygame.Surface((radius*2,radius*2), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(
            self.image, radius, radius, radius-1, self.colour)
        pygame.gfxdraw.filled_circle(
            self.image, radius, radius, radius-1, self.colour)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
