import logging
import unittest

import pygame

from lib.sprite import Bullet


RED = (255, 0, 0)


class TestBullet(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((600,380))

        Bullet.groups = pygame.sprite.Group()
        self.bullet = Bullet(RED, 5)

    def test_constructor_without_defined_groups(self):
        """
        Use the Bullet constructor with a 'groups' attribute that
        contains a non-Group.

        Should raise a TypeError.
        """
        Bullet.groups = None
        self.assertRaises(TypeError, Bullet, RED, 5)

    def test_constructor_with_defined_groups(self):
        """
        Use the Bullet constructor with a 'groups' attribute that
        contains only Groups.

        Should add the Bullet instance to the Groups in the 'groups'
        attribute.
        """
        a = pygame.sprite.Group()
        b = pygame.sprite.Group()
        c = pygame.sprite.Group()

        Bullet.groups = (a, b, c)
        bullet = Bullet(RED, 5)
        self.assertEqual(len(bullet.groups), len(Bullet.groups))
        for i in Bullet.groups:
            with self.subTest(group=i):
                self.assertIn(i, bullet.groups)

    # ---
    # Should this just be merged with the other two methods to create
    # a test_constructor() method? 
    #
    # def test_constructor_with_offset(self):
    #     pass
    # ---

    def test_update(self):
        """
        Use the update() method.

        Should move the bullet left by (the value of) its 'speed'
        attribute.
        """
        expected_rect = self.bullet.rect
        expected_rect.left -= self.bullet.speed

        self.bullet.update()
        self.assertEqual(expected_rect, self.bullet.rect)

    def test_set_radius(self):
        """
        Use the set_radius() method.

        Should update the 'radius' attribute to the given value, then
        update the visible attributes to reflect this change. Should
        preserve the topleft position of the 'rect' attribute.
        """
        radius = 10
        x = 100
        y = 100

        bullet = Bullet(RED, 5, x, y)
        bullet.set_radius(radius)
        self.assertEqual(radius, bullet.radius)
        self.assertEqual((x,y), bullet.rect.topleft)


if (__name__ == "__main__"): unittest.main()
