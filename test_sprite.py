import logging
import unittest

import pygame

from lib.sprite import Bullet


class TestBullet(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((600,380))
        self.bullet = Bullet((100,100), (255,0,0), 6)

    def test_update(self):
        """
        The update() method must move the bullet to the left by the
        magnitude of its speed.
        """
        expected_rect = self.bullet.rect
        expected_rect.left -= self.bullet.speed

        self.bullet.update()
        self.assertEqual(expected_rect, self.bullet.rect)


if (__name__ == "__main__"): unittest.main()
