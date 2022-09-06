from turtle import title
from django.shortcuts import render, redirect
from .models import Task

#Cuando se va importar algo desde el mimo directorio se le debe indicar con un punto

# Create your views here.
def list_tasks(request):
    # No se agrega el nombre de la carpeta templates porque django ya sabe que estan ahi las vistas
    tasks = Task.objects.all()
    return render(request,'list_tasks.html', {"tasks": tasks})

def create_task(request):
    task = Task(title = request.POST['title'], description = request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task  = Task.objects.get(id = task_id)
    task.delete()
    return redirect('/tasks/')


def get_task(request, task_id):
    task = Task.objects.get(id = task_id)
    return render(request,'list_tasks.html', {"task": task})

def update_task(request):
    id = int(request.POST['id'])
    title = request.POST['title']
    description = request.POST['description']
    print(id, title, description)
    task = Task.objects.get(id = id)
    task.title = title
    task.description = description
    return redirect('/tasks/')