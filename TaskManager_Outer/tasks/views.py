from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationform
from .models import Task
from django.contrib import messages

# Home page
def home(request): 
    return render(request, 'home.html')

# Dashboard
@login_required
def dashboard(request):
    if request.method == 'POST':  # ✅ FIXED: mothod → method
        title = request.POST['title']
        Task.objects.create(title=title, user=request.user)
        messages.success(request, "Task Added")
        return redirect('dashboard')
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tasks': tasks})

# Toggle task
@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('dashboard')

# Delete task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, "Task Deleted")
    return redirect('dashboard')

# Register here
def register(request):
    if request.method == 'POST':
        form = UserCreationform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationform()
    return render(request, 'register.html', {'form': form})
