from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def home(request):
    tasks = Task.objects.all()

    return render(request, 'home.html', {'tasks': tasks})

def create_task(request):

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Task Has Been Created Successfully')
            return redirect('home')
        
    return render(request, 'task_form.html', {'form': form})

def update_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'task Has Been Updated Successfully')
            return redirect('home')
    return render(request, 'task_form.html', {'task': task, 'form':form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.add_message(request, messages.SUCCESS, 'Task Has Been Deleted Successfully')
    return redirect('home')

def detail_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})