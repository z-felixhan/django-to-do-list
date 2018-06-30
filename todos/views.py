# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Todo

def index(request):

    todoList = Todo.objects.order_by('id')

    context = {
        'todoList': todoList
    }

    return render(request, 'todos/index.html', context)