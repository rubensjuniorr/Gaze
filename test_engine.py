import unittest

from engine import split_text, forward, backward, current_block


class TestEngine(unittest.TestCase):
    def test_split_text_into_blocks(self):
        result = split_text("One two three four five", 4)

        self.assertEqual(result, ["One two three four", "five"])


    def test_empty_text_returns_no_blocks(self):
        result = split_text("")
        self.assertEqual(result, [])

    def test_zero_block_size_raises_error(self):
        with self.assertRaises(ValueError):
            split_text("One two three", 0)

    def test_with_negative_number_raises_error(self):
        with self.assertRaises(ValueError):
            split_text("One two three", -1)

    def test_forward_moves_to_next_block(self):
        blocks = ["First block", "Second block"]

        result = forward(0, blocks)

        self.assertEqual(result, 1)

    def test_forward_stays_at_last_block(self):
        blocks = ["First block", "Second block"]

        result = forward(1, blocks)

        self.assertEqual(result, 1)

    def test_backward_moves_to_previous_block(self):
        blocks = ["First block", "Second block"]

        result = backward(1, blocks)

        self.assertEqual(result, 0)

    def test_backward_stays_at_first_block(self):
        blocks = ["First block", "Second block"]

        result = backward(0, blocks)

        self.assertEqual(result, 0)

    def test_current_block_returns_selected_block(self):
        blocks = ["First block", "Second block"]

        result = current_block(1, blocks)

        self.assertEqual(result, "Second block")

    def test_current_block_returns_empty_string_for_no_blocks(self):
        result = current_block(0, [])

        self.assertEqual(result, "")