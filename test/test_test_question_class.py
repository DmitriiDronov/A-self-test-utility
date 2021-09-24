import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_question import TestQuestion

class TestQuestionTestCase(unittest.TestCase):


    def test__init__(self):
        testQuestion = TestQuestion("Question?", [{"answer_text": "Answer 1", "value": 1}, {"answer_text": "Answer 2", "value": 0}])
        
        self.assertEqual(testQuestion.question_text, "Question?", "TestQuestion class: __init__, Question texts aren't equal")
        self.assertEqual(testQuestion.answers, [{"answer_text": "Answer 1", "value": 1}, {"answer_text": "Answer 2", "value": 0}], "TestQuestion class: __init__, Answers aren't equal")


    def test__str__(self):
        testQuestion = TestQuestion("Question?", [{"answer_text": "Answer 1", "value": 1}, {"answer_text": "Answer 2", "value": 0}])
        expected_string = "Question?\n0. Answer 1\n1. Answer 2\n"
        actual_string = testQuestion.__str__()

        self.assertEqual(actual_string, expected_string, "TestQuestion class: __str__, Test Question String Representations aren't equal")


    def test_get_all_answers(self):
        testQuestion = TestQuestion("Question?", [{"answer_text": "Answer 1", "value": 1}, {"answer_text": "Answer 2", "value": 0}])
        actual_result = testQuestion.get_all_answers()
        expected_result = [{"answer_text": "Answer 1", "value": 1}, {"answer_text": "Answer 2", "value": 0}]
        
        self.assertEqual(actual_result, expected_result, "TestQuestion class: get_all_answers, got different answers")


    def test_get_correct_answers(self):
        testQuestion = TestQuestion("Question?", [{"answer_text": "Answer 1", "value": 1}, {"answer_text": "Answer 2", "value": 0}])
        actual_result = testQuestion.get_correct_answers()
        expected_result = [{"answer_text": "Answer 1", "value": 1}]
        
        self.assertEqual(actual_result, expected_result, "TestQuestion class: get_correct_answers, got different correct answers")


    def test__is_answer_correct(self):
        testQuestion = TestQuestion("Question?", [])
        actual_result = testQuestion._TestQuestion__is_answer_correct({"answer_text": "Answer 1", "value": 1})
        expected_result = True
        
        self.assertEqual(actual_result, expected_result, "TestQuestion class: __is_answer_correct, should return True when passing true answer")

        actual_result = testQuestion._TestQuestion__is_answer_correct({"answer_text": "Answer 2", "value": 0})
        expected_result = False

        self.assertEqual(actual_result, expected_result, "TestQuestion class: __is_answer_correct, should return False when passing false answer")

        actual_result = testQuestion._TestQuestion__is_answer_correct("")
        self.assertEqual(actual_result, False, "TestQuestion class: __is_answer_correct, should return None when passing nothing")