from django.shortcuts import render,redirect
from .forms import task_form
from .models import taskmodel

def addtask(request):
    if request.method=='POST':
        task=task_form(request.POST)
        if task.is_valid():
            task.save()
            return redirect('tasklist')
    else:       
        task=task_form()
    return render(request,'add_tasks.html',{'form':task})

def task_list(request):
     tasks = taskmodel.objects.filter(is_completed=False)
     return render(request,'show_tasks.html',{'task':tasks})

def edit_task(request,id):
    task=taskmodel.objects.get(pk=id)
    form=task_form(instance=task)
     
    if request.method == 'POST':
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form = task_form(instance=task)

    return render(request, 'edit_task.html', {'form': form})

def delete_task(request,id):
     task=taskmodel.objects.get(pk=id).delete()
     return redirect('tasklist')
    


def completed_tasks(request):
    tasks = taskmodel.objects.filter(is_completed=True)
    return render(request, 'completedtask.html', {'tasks': tasks})



def mark_completed(request, id):
    task=taskmodel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('completedtasks') 
