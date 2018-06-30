# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):

    todoList = Todo.objects.order_by('id')
    form = TodoForm()

    context = {
        'todoList': todoList,
        'form': form
    }

    return render(request, 'todos/index.html', context)

def add(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def complete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')