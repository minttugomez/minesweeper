import unittest
import pygame
from src.main.minesweeper.minesweeper import Minesweeper, Stopwatch, Button

class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.minesweeper = Minesweeper()

    def test_initialization(self):
        self.assertEqual(self.minesweeper.game_status, 0)
        self.assertEqual(self.minesweeper.mines_left, 0)
        self.assertIsInstance(self.minesweeper.stopwatch, Stopwatch)
        self.assertIsInstance(self.minesweeper.screen, pygame.Surface)

    def test_draw_buttons(self):
        pass

    def test_draw_info(self):
        pass