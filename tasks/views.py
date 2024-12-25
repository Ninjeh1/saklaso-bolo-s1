from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

def create_task(request):
    return render(request, 'task_form.html')

def update_task(request,pk):
    return render(request, 'task_form.html')


def delete_task(request, pk):
    return redirect('home')

def detail_task(request, pk):
    return render(request, 'task_detail.html')