import robot
import unittest
import sys
import maze.mazerunner as mazerunner
import maze.obstacles as obstacles

from unittest.mock import patch
from io import StringIO

class TestMazerunner(unittest.TestCase):
    def test_path_blocked(self):
        self.assertFalse(mazerunner.is_path_blocked(-2,15,3,4),False)

    def test_position_blocked(self):
        self.assertFalse(mazerunner.is_position_blocked(10,33),False)

    def test_maze_exit_directions(self):
        self.assertEqual(mazerunner.open_exit('top'),'top')

    