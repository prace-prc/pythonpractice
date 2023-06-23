from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_View(), name='index'),
    path("<int:question_id>/", views.detail, name='detail'),
    path("<int:question_id>/vote/", views.vote, name='vote'),
    path("<int:question_id>/results/", views.results, name='results'),
]