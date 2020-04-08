"""
Contains code for unittesting of the Questions class.
"""

import unittest
from questions import Question

class QuestionTest(unittest.TestCase):
    """
    Tests the Question class.
    """
    def test_create_question(self):
        """
        Test to create a new question and answer.
        """
        quest = Question("Vad heter jag?", "Usama")
        self.assertEqual(quest._text, "Vad heter jag?")
        self.assertEqual(quest._answer, "Usama")

if __name__ == "__main__":
    unittest.main(verbosity=3)
