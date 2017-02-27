from django.conf.urls import url


#imports views.py from mysite projects
from . import views

#sets a namespace for all of the urls. Use this in front of the name parameter in url so django knows what app view to
#create
app_name = 'polls'

urlpatterns = [
    #In http://127.0.0.1:8000/polls/, the index function in views is called
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    #In http://127.0.0.1:8000/polls/<whatever the primary key (SQL) is>/, the detail function in views is called
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    #In http://127.0.0.1:8000/polls/<whatever the primary key (SQL) is>/results/, the results function in views is called
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = 'results'),

    #In http://127.0.0.1:8000/polls/<whatever the question_id is>/vote/, the vote function in views is called
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
]
