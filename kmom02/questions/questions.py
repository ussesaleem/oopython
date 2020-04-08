"""
Contains all classes for the different types of questions
"""

class Question():
    """
    Manages the text questions.
    """
    type = "text"

    def __init__(self, text, answer):
        """
        Initiates the text option and the correct answer.
        """
        self._text = text
        self._answer = answer

    @classmethod
    def get_type(cls):
        """
        Returns the question type.
        """
        return Question.type

    def get_text(self):
        """
        Returns the text.
        """
        return self._text

    def check_answer(self, respons):
        """
        Checks if the player's answer matches the correct answer.
        """
        return self._answer.lower() == respons.lower()

class RadiobuttonQuestion(Question):
    """
    Manages the Radiobutton questions.
    """
    type = "radiobutton"

    def __init__(self, text, answer, alternatives):
        """
        Initiates through inheriting from Question class.
        """
        super().__init__(text, answer)
        self.alternatives = alternatives

    @classmethod
    def get_type(cls):
        """
        Returns the question type.
        """
        return RadiobuttonQuestion.type

    def get_alternatives(self):
        """
        Returns the alternatives.
        """
        return self.alternatives

    def check_answer(self, respons):
        """
        Checks if the player's answer matches the correct answer.
        """
        return bool(respons == self._answer)


class CheckboxQuestion(Question):
    """
    Manager the Checkbox questions.
    """
    type = "checkbox"

    def __init__(self, text, answer, alternatives):
        """
        Initiates through inheriting from Question class.
        """
        super().__init__(text, answer)
        self.alternatives = alternatives

    @classmethod
    def get_type(cls):
        """
        Returns the question type.
        """
        return CheckboxQuestion.type

    def get_alternatives(self):
        """
        Returns the alternatives.
        """
        return self.alternatives

    def check_answer(self, respons):
        """
        Checks if the player's answers matches the correct answers.
        """
        points = 0
        for a in respons:
            if a in self._answer:
                points += 1
        return points
