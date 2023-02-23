import unittest
from game import Game, Move

class TestGame(unittest.TestCase):
    def test_default_game(self):
        # test a default game with no moves
        game = Game()
        self.assertEqual(game.board_size, 3)
        self.assertEqual(game.current_player.label, "X")
        self.assertEqual(game.is_tied(), False)
        self.assertEqual(game.has_winner(), False)

    def test_out_of_bounds(self):
        # Test a move that is out of bounds
        game = Game()
        move = Move(3, 0, "X")
        # test IndexError
        with self.assertRaises(IndexError):
            game.is_valid_move(move)
        
        with self.assertRaises(IndexError):
            game.process_move(move)

    def test_move(self):
        # test a move
        game = Game()
        move = Move(0, 0, "X")
        self.assertEqual(game.current_player.label, "X")
        game.process_move(move)
        game.toggle_player()
        self.assertEqual(game.current_player.label, "O")
        self.assertEqual(game.is_valid_move(move), False)
        self.assertEqual(game.is_valid_move(Move(0, 1, "O")), True)
        self.assertEqual(game.is_tied(), False)
        self.assertEqual(game.has_winner(), False)
    
    def test_end_game(self):
        # Test a game that ends with X winning
        game = Game()
        game.process_move(Move(0, 0, "X"))
        game.toggle_player()
        game.process_move(Move(0, 1, "O"))
        game.toggle_player()
        game.process_move(Move(1, 0, "X"))
        game.toggle_player()
        game.process_move(Move(0, 2, "O"))
        game.toggle_player()
        game.process_move(Move(2, 0, "X"))
        self.assertEqual(game.is_tied(), False)
        self.assertEqual(game.has_winner(), True)
        self.assertEqual(game.current_player.label, "X")

if __name__ == '__main__':
    unittest.main()