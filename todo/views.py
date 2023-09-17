from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .form import TodoForm
from .asanaapi import * 

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos , 'title':'Todo List'})


def get_todo_by_id(request):
    if request.method == 'POST':
        todo_id = request.POST["id"]
        todo = get_object_or_404(Todo, pk=todo_id)
        data = {
            'id': todo.id,
            'title': todo.title,
            'description': todo.notes,
            'completed': todo.completed,
        }
        return JsonResponse(data)

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            obj = AsanaApi
            obj.create_asana_task(request.POST["title"],request.POST["notes"])
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form , 'title':'Create Todo List', 'action' :'create'})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo , 'title':'Do you want to delete ?'})
