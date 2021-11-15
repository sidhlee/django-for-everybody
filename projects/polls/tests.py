import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):
    # Django looks for test methods that begins with "test"
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        future_time = timezone.now() + datetime.timedelta(days=7)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)


# (venv) ➜  projects git:(main) ✗ ./manage.py test polls
# Creating test database for alias 'default'...
# System check identified no issues (0 silenced).
# F
# ======================================================================
# FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
# was_published_recently() returns False for questions whose pub_date
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/hayounlee/Projects/learning/django-for-everybody/projects/polls/tests.py", line 19, in test_was_published_recently_with_future_question
#     self.assertIs(future_question.was_published_recently(), False)
# AssertionError: True is not False

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)
# Destroying test database for alias 'default'...
