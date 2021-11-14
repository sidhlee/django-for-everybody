from django.db import models


class Question(models.Model):
    # max_length is required for CharField
    question_text = models.CharField(max_length=200)
    # optional first positional arg for human-readable field name
    # Also works as documentation
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
