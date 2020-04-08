#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""
from questions import Question, RadiobuttonQuestion, CheckboxQuestion

class QuestionManager():
    """
    Manages all questions
    """

    def __init__(self):
        """
        Initiates a new questionmanager session.
        """
        self._points = 0
        self._quest_count = 0
        self.questions = []
        self.answers = []
        self.add_default_questions()

    def get_score(self):
        """
        Returns the player's actual points.
        """
        return self._points

    def get_max_score(self):
        """
        Returns the max points.
        """
        max_score = (len(self.questions) + len(self.answers[0]) +
                     len(self.answers[1]) + len(self.answers[2]) - 3)
        return max_score

    def has_next(self):
        """
        Checks if there are any more questions.
        """
        if self._quest_count < 9:
            return True

    def get_next(self):
        """
        Returns the next question.
        """
        question = self.questions[self._quest_count]
        return question

    def get_quest_count(self):
        """
        Returns the question number.
        """
        return self._quest_count

    def correct_answer(self, form):
        """
        Checks if the answer is correct and adds points.
        """
        question = self.questions[self._quest_count]
        check_respons = question.check_answer(form.get("answer"))
        if question.type == "text" or question.type == "radiobutton":
            if check_respons is True:
                self._points += 1
        elif question.type == "checkbox":
            self._points += question.check_answer(form.getlist("answer"))
        self._quest_count += 1

    def add_default_questions(self):
        """
        Adds questions to the question list and handles the answers
        and alternatives.
        """
        question_one = Question(("Vad heter landet med röd flagga med ett " +
                                 "vitt kryss i mitten?"), "Schweiz")
        self.questions.append(question_one)
        question_two = Question(("Hur gammal måste man vara för att få ta " +
                                 "B-körkort i Sverige (i siffror)?"), str(18))
        self.questions.append(question_two)
        question_three = Question(("Vad är efternamnet på författaren av " +
                                   "Romeo & Juliet?"), "Shakespeare")
        self.questions.append(question_three)

        question_four = RadiobuttonQuestion(("Vilket av följande alternativ " +
                                             "har högst siffra när man " +
                                             "mäter 1 meter?"),
                                            "Inches",
                                            [
                                                "Foot",
                                                "Inches",
                                                "Yards"
                                            ])
        self.questions.append(question_four)
        question_five = RadiobuttonQuestion(("Vem av följande är inte en av " +
                                             "huvudkaraktärerna i TV-serien " +
                                             "Friends?"),
                                            "John",
                                            [
                                                "John",
                                                "Ross",
                                                "Phoebe"
                                            ])
        self.questions.append(question_five)
        question_six = RadiobuttonQuestion(("Vad av följande är inte ett " +
                                            "datortillbehör?"),
                                           "Golv",
                                           [
                                               "Mus",
                                               "Tangentbord",
                                               "Golv"
                                           ])
        self.questions.append(question_six)

        seven_correct_list = ["Hund", "Giraff"]
        self.answers.append(seven_correct_list)
        question_seven = CheckboxQuestion(("Vilket/Vilka av följande djur " +
                                           "går på 4 ben?"),
                                          [
                                              "Hund",
                                              "Giraff"
                                          ],
                                          [
                                              "Snigel",
                                              "Hund",
                                              "Apa",
                                              "Orm",
                                              "Giraff"
                                          ])
        self.questions.append(question_seven)
        eight_correct_list = ["Bord", "Stolar", "Byrå"]
        self.answers.append(eight_correct_list)
        question_eight = CheckboxQuestion(("Vilket/Vilka av följande " +
                                           "alternativ hittar man i en " +
                                           "lägenhet?"),
                                          [
                                              "Bord",
                                              "Stolar",
                                              "Byrå"
                                          ],
                                          [
                                              "Bord",
                                              "Stolar",
                                              "Grus",
                                              "Gräs",
                                              "Byrå"
                                          ])
        self.questions.append(question_eight)
        nine_correct_list = ["1an", "2an", "4an", "6an"]
        self.answers.append(nine_correct_list)
        question_nine = CheckboxQuestion(("Vilka kanaler ingår vanligtvis " +
                                          "i ett grund TV-utbud?"),
                                         [
                                             "1an",
                                             "2an",
                                             "4an",
                                             "6an"
                                         ],
                                         [
                                             "1an",
                                             "2an",
                                             "4an",
                                             "5an",
                                             "6an"
                                         ])
        self.questions.append(question_nine)

    def read_session(self, session):
        """
        Read current score and current quest number from session
        """
        self._points = session.get("points", 0)
        self._quest_count = session.get("quest_count", 0)

    def write_session(self, session):
        """
        Write current score and quest number to session
        """
        session["points"] = self._points
        session["quest_count"] = self._quest_count

    def reset(self):
        """
        Reset score and quest number to 0
        """
        self._quest_count = 0
        self._points = 0
