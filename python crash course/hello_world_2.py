                                                # It is the second part of hello_world.py

# A Class to Test

# So, I made a Class that helps administer anonymous surveys and stored it in survey.py,

# To show that the AnonymousSurvey class works, let’s write a program that uses the class

from survey import AnonymousSurvey

# Define a question and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' anytime to quit.\n")
while True:
    response = input("Language : ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone for participating in the survey!")
my_survey.show_results()

# Testing the AnonymousSurvey Class

import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
# Check if it can store 3 rosponses...    

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
 
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()

# This works perfectly. However, these tests are a bit repetitive, so we’ll use another feature of unittest to make them more efficient.

# The setUp() method

# import unittest
# from survey import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey."""
 
#     def setUp(self):
#         """Create a survey and a set of responses for use in all test methods."""
#         question = "What language did you first learn to speak?"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']
    
#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)
    
#     def test_store_three_responses(self):
#         """Test that three individual responses are stored properly."""
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for response in self.responses:
#             self.assertIn(response, self.my_survey.responses)

# if __name__ == '__main__':
#     unittest.main()

# It will do the same work as the earlier code did.

# When you’re testing your own classes, the setUp() method can make your test methods easier to write.
# You make one set of instances and attributes in setUp() and then use these instances in all your test methods.
# This is much easier than making a new set of instances and attributes in each test method.

# REMEMBER - When a test case is running, Python prints one character for each unit test as it is 
# completed. A passing test prints a dot, a test that results in an error prints an E, and 
# a test that results in a failed assertion prints an F. This is why you’ll see a different 
# number of dots and characters on the first line of output when you run your test cases. 
# If a test case takes a long time to run because it contains many unit tests, you can 
# watch these results to get a sense of how many tests are passing.
                                                                  ### FINISHED ###