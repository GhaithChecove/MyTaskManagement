from django.urls import path 
from blog import views as v
app_name="blog"
urlpatterns = [
    path('' , v.home  ,name='home'),
    path('login/' , v.login , name ="login"),
    # path('signup/' , v.signup , name = "singup"),
    # path('tasks/' , v.tasks , name='tasks'),
    path('tasks/' , v.tasks_view ,name = 'tasks' ),
    path('create-cat/', v.new_category , name ='create_category'),
    path('tasks/new-task/' , v.new_task ,  name='new_task'),
    path('tasks/create-task/' ,v.create_task , name='create_new_task'),
    path('gh/', v.task_stack_update , name='task_stack_update'),
    path('go/' , v.go , name="go"),
]
