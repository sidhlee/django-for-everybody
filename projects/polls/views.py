from django.http import HttpResponse
from django.template import loader
from django.template.base import Template

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # find template from all templates folder
    template: Template = loader.get_template("polls/index.html")
    # create context to feed into template
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    return HttpResponse(f"You're looking at the result of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
