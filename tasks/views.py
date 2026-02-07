from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm


class IndexView(View):
    def get(self, request):
        form = TaskForm()
        active_tasks = Task.objects.filter(
            completed=False
        ).order_by('due_date')
        completed_tasks = Task.objects.filter(
            completed=True
        ).order_by('due_date')
        context = {
            'form': form,
            'active_tasks': active_tasks,
            'completed_tasks': completed_tasks
        }
        return render(request, 'tasks/index.html', context)
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        active_tasks = Task.objects.filter(
            completed=False
        ).order_by('due_date')
        completed_tasks = Task.objects.filter(
            completed=True
        ).order_by('due_date')
        context = {
            'form': form,
            'active_tasks': active_tasks,
            'completed_tasks': completed_tasks
        }
        return render(request, 'tasks/index.html', context)


class ToggleTaskView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('home')


class DeleteTaskView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('home')

    
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


