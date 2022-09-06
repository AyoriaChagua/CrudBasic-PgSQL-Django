from venv import create
from django.urls import path
from .views import delete_task, list_tasks, create_task, get_task, update_task


urlpatterns = [
    path('', list_tasks),
    path('new/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', get_task, name='get_task'),
    path('update_task/', update_task, name='update')
]
