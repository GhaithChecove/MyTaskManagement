from django.shortcuts import render ,redirect 
from django.http import HttpResponse , JsonResponse 
from rest_framework.response import Response
# from .forms import NewTask_form
# Create your views here.
from .forms import *
from . import models as m
import json
from django.core import serializers
from django.template.loader import render_to_string
from django.urls import reverse
from .serializers import TaskSerializer , CategorySerializer  , NewTaskSerializer
def home(request):
    context = {}

    return render (request , 'index.html' , {'form':context})


def login(request):

    return render(request , 'login.html' , {})


# def signup(request):

#     return render (request , 'SignUp.html' , {})


# def tasks(request):
#     task_form = NewTask_form()
#     return render(request , "kanban.html" , {"task_from":task_form})

def tasks_view(request):

    '''  'account/' this is a view of main page  '''
    context={}
    user = request.user
    if user.is_authenticated:
        context['user']=user
        context['new_task_form']=NewTask_form()
        context['new_category'] = NewCategory()
        
        return render (request, "kanban.html" , context=context)
    else:
        return render(request ,'index.html' , context={})

def new_task(request):
    context = {}
    print("get into new Task function view")
    if request.method=="GET":
        new_task_form_cat=NewTask_form()
        # ser_items = CategorySerializer(new_task_form_cat , many=True)
        cat_list = list(m.Category.objects.all().values())
        print('get in if  and return data')
        return JsonResponse({'cat_list':cat_list})
    
    return redirect (reverse('new_task'))

def new_category(request):
    print('get in new category')

    if request.method=="POST":
        data={}
        if request.user.is_authenticated:
            form= request.POST
            name=form['name']
            desc = form['desc']
            cat= m.Category(cat_name=name,cat_description=desc)
            cat.save()
            data['success']= True
            data['cat']=name
            # newTask = NewTask_form()
            # data['new_task_form']= render_to_string('kanban.html',{'new_task_form':newTask})
            
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        form=NewCategory()
        print('cat is not created')
        return HttpResponse("the user isn't authorized" , {'form':form})
    



def create_task(request):
    print('task creation')
    user = request.user
    selected_cat = ""
    if request.method =="POST":
        if user.is_authenticated:
            form =request.POST
            # print(form)
            header = form['tsk_header']
            title = form['tsk_title']
            category = form['tsk_category']
            # print("category", category , type(category))
            content = form['tsk_content']
            end_time = form['end_time']
            cat = m.Category.objects.all()
            for i in cat:
                # print('typeof(i)' , type(i.id))
                if str(i.id)==category:
                    # print("printing i.id", i.id)
                    selected_cat=i
                    # print("printing cat" , selected_cat)
            
            t = m.Task(tsk_header = header , tsk_title= title , tsk_category = selected_cat ,tsk_author=user, tsk_content = content  ,tsk_end_time=end_time)
            t.save()
            # task =NewTaskSerializer(t)
            return HttpResponse(json.dumps({'message':'True' ,  'new_task':"task"}), content_type='application/json')
        return HttpResponse(json.dumps({'message':'user is not authenticated'}), content_type='application/json')


def task_stack_update(request):
    # print(m.Task.objects.all())
    all_tasks =m.Task.objects.all().values() 
    # all_tasks_authors = m.Task.objects.select_related('tsk_author' ).all().values()
    # print('this is all tasks list' , all_tasks)
    tasks = NewTaskSerializer(all_tasks)
    

    # print(tasks_author)
    print("tasks : " ,tasks)
    return HttpResponse({"message":tasks }  ,content_type = 'application/json')

def go(request):

    return render(request , 'results.html' , {})