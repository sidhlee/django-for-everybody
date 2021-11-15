from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# ListView - display a list of objects
class IndexView(generic.ListView):
    # By default, ListView uses <app name>/<model name>_list.html
    template_name = "polls/index.html"
    # By default, this would've been "question_list"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> QuerySet[Question]:
        # Return the last 5 published questions
        return Question.objects.order_by("-pub_date")[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# DetailView - display a detail page for a particular type of object
# it calls the value captured from URL 'pk'
class DetailView(generic.DetailView):
    # question variable is automatically provided to the context
    model = Question
    # by default, DetailView uses <app name>/<model_name>_detail.html e.g. polls/question_detail.html
    # but we're overriding this with custom value
    template_name = "polls/detail.html"


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # submitted data is available under request.POST by the input name
        # this will raise KeyError if it can't find "choice" in request.POST
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        # This can result in race condition if a user retrieves a choice before the other user finishes updating it.
        # e.g. user A gets 42 before user B updates it to 43
        # now user A and B both saves 43 which should've been 44
        selected_choice.votes += 1
        selected_choice.save()

        # Must return HttpResponseRedirect after dealing with POST data to prevent
        # the user hitting the Back button and submitting the POST data twice.
        return HttpResponseRedirect(
            # just like we use url template tag to access path by its name and argument,
            # we can use reverse inside view function to access routes defined in url.py
            reverse("polls:results", args=(question.id,))
        )

    return HttpResponse(f"You're voting on question {question_id}")
