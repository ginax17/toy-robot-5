import robot
import unittest
import sys
#from world import obstacles as obstacles
import world.obstacles as obstacles
from unittest.mock import patch
from io import StringIO


class TestObstacles(unittest.TestCase):
    
    def test_path_blocked(self):
        self.assertFalse(obstacles.is_path_blocked(-2,10,34,19),False)
    
    def test_position_blocked(self):
        self.assertFalse(obstacles.is_position_blocked(22,45),False)

    