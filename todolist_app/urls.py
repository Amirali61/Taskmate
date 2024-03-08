from django.urls import path
import todolist_app.views as views

urlpatterns = [
    path('',views.todolist,name='todolist'),
    path('delete/<task_id>',views.delete_task,name='delete_task'),
    path('edit/<task_id>',views.edit_task,name='edit_task'),
    path('change_status/<task_id>',views.change_status,name='change_status'),
]
