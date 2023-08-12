from django.urls import path
from . import views

urlpatterns = [
    
    path('addtask/',views.addtask,name='addtask'),
    path('tasklist/',views.task_list,name='tasklist'),
    path('edittask/<int:id>',views.edit_task,name='edittask'),
    path('deletetask/<int:id>',views.delete_task,name='deletetask'),
    path('markcompleted/<int:id>/', views.mark_completed, name='markcompleted'),
    path('completedtasks/',views.completed_tasks,name='completedtasks')
]


