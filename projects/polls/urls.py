from django.urls import path

from . import views

urlpatterns = [
    # eg: /polls/
    path("", views.index, name="index"),
    # <> captures part of url and sends it as a keyword argument to the view function
    # ex: /polls/5/
    # we can acesss 'detail' url from the template using {% url %} template tag and provide argument
    # to be inserted as question_id
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
