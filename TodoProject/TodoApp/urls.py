
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classview/',views.TaskListview.as_view(),name='classview'),
    path('classdetail/<int:pk>/',views.TaskDeailview.as_view(),name='classdetail'),
    path('classupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='classupdate'),
    path('classdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='classdelete'),

]
