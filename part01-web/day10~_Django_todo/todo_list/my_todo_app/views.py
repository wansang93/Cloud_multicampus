from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'index.html', content)


def create_todo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


def delete_todo(request):
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))


def done_todo(request):
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id=done_todo_id)
    todo.is_done = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
