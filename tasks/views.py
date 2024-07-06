from django.shortcuts import render, redirect
from .models import Tasks
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
# Create your views here.
def index(request):
    if request.method == 'POST':
        title       = request.POST.get('title')
        description = request.POST.get('description')
        categories  = request.POST.get('categories') 
        due_date    = request.POST.get('due_date')  
        priority    = request.POST.get('priority') 
        print(due_date)
        try:
            # Convert mm/dd/yy format to YYYY-MM-DD format
            due_date = datetime.strptime(due_date, '%Y-%m-%d')

            # now = timezone.now().replace(tzinfo=None)

            if due_date.date() < timezone.now().date():
                raise ValueError('Due date must be a future date.')

        except ValueError as e:
            if 'future date' in str(e):
                messages.error(request, str(e))
            else:
                messages.error(request, 'Invalid date format. Use YYYY-MM-DD format.')
            return redirect('tasks:index')
        date_created = timezone.now()

        Tasks.objects.create(
            title = title,
            description = description,
            due_date = due_date,
            categories = categories,
            priority = priority,
            date_created = date_created,
        )
        tasks = Tasks.objects.all()
        messages.success(request, f'Task added successfully')
        # return render (request, 'tasks/index.html', {'tasks':tasks})
        return redirect('tasks:index')
    tasks = Tasks.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})