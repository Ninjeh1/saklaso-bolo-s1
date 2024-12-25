from django.shortcuts import render, redirect


def register_view(request):
    return render(request, 'user_form.html')

def login_view(request):
    return render(request, 'user_form.html')

def logout_view(request):
    return redirect('login_view')