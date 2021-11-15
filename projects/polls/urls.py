from django.urls import path

from . import views

# namespacing url patterns to avoid collision with the same url name from other apps
app_name = "polls"
urlpatterns = [
    # eg: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # <> captures part of url and sends it as a keyword argument to the view function
    # ex: /polls/5/
    # we can acesss 'detail' url from the template using {% url %} template tag and provide argument
    # to be inserted as question_id
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
