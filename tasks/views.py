from django.shortcuts import render
from django.views import View
from .models import Task


class IndexView(View):
    def get(self, request):
        active_tasks = Task.objects.filter(
            completed=False
        ).order_by('due_date')
        completed_tasks = Task.objects.filter(
            completed=True
        ).order_by('due_date')
        context = {
            'active_tasks': active_tasks,
            'completed_tasks': completed_tasks
        }
        return render(request, 'tasks/index.html', context)
  
    
class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.filter(completed=False).order_by('due_date')
        return render(request, 'tasks/task_list.html', {'tasks': tasks})
    

class CompletedTaskListView(View):
    def get(self, request):
        tasks = Task.objects.filter(completed=True).order_by('due_date')
        return render(
            request,
            'tasks/completed_task_list.html',
            {'tasks': tasks}
        )


class AllTasksView(View):
    def get(self, request):
        active_tasks = Task.objects.filter(
            completed=False
        ).order_by('due_date')
        completed_tasks = Task.objects.filter(
            completed=True
        ).order_by('due_date')
        return render(
            request,
            'tasks/all_tasks.html',
            {
                'active_tasks': active_tasks,
                'completed_tasks': completed_tasks
            }
        )


