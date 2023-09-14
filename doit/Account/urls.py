from django.urls import path
from . import views as v
app_name='Account'
urlpatterns = [
    path('' , v.home_view,name="home"),
    path('login/' , v.login_view , name ="login"),
    path('signup/' , v.registration_view , name = "signup"),
    path('tasks/' , v.tasks_view , name='tasks'),
    path('log/',v.log_out ,name='log_out' ),
]
