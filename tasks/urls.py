from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path(
        'completed/',
        views.CompletedTaskListView.as_view(),
        name='completed_list'
    ),
    path('all/', views.AllTasksView.as_view(), name='all_tasks'),
    path('toggle/<int:task_id>/', views.ToggleTaskView.as_view(), name='toggle_task'),
    path('delete/<int:task_id>/', views.DeleteTaskView.as_view(), name='delete_task'),
]

