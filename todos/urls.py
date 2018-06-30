from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('add', views.add, name='add'),
    url(r'complete/(?P<todo_id>\d+)', views.complete, name='complete')
]