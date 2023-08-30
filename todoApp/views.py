from django.shortcuts import render
from .models import Todo

# Create your views here.

#* FBV *#

def todo_list(request):
    todos= Todo.objects.all(),
    context={
        'todos':todos
    }
    return render(request, list.html, context)
    # return render(request, list.html, 'todos':todos)
