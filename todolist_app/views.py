from django.shortcuts import render , redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
''' create task '''

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request,"New Task Added!")
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manager = request.user)
        paginator = Paginator(all_tasks,4)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request,'todolist.html',{'all_tasks':all_tasks})


''' edit task '''


def edit_task(request , task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"Task edited!")
        return redirect('todolist')      
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})



''' delete task '''



def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if (task.manager == request.user):
        task.delete()       
    else:
        messages.error(request,'Access Is Not Allowed!')     
    return redirect('todolist')



''' change the status of a task'''



def change_status(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if (task.manager == request.user):
        task.done = True if task.done == False else False
        task.save()
    else:
        messages.error(request,'Access Is Not Allowed!')
    return redirect('todolist')


''' index '''

def index(request):
    context = {
        'index_text':"Welcome to index page",
               }
    return render(request,'index.html',context)

''' other pages '''

def contact_us(request):
    context = {
        'contact_text':"Welcome to contact page",
               }
    return render(request,'contact.html',context)

def about_us(request):
    context = {
        'about_text':"Welcome to about page",
               }
    return render(request,'about.html',context)