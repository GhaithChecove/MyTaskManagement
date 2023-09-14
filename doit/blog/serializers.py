from rest_framework import serializers
from . import models as m 
from Account.models import MyUser
from rest_framework import generics

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=m.Category
        fields=['id' , 'cat_name' , 'cat_description']

class MyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=MyUser
        fields = ['first_name' , 'last_name' , 'username' ,]

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=m.Task
        fields=['id' , 'tsk_header' , 'tsk_title', 'tsk_author' , 'tsk_category'  , 'tsk_content' , 'tsk_status']
        depth=1


class NewTaskSerializer(serializers.ModelSerializer):

    tsk_category = CategorySerializer
    # tsk_author = My
    tsk_author = MyUserSerializer
    class Meta:
        model=m.Task
        fields = [ 'tsk_header' , 'tsk_title' , 'tsk_category' , 'tsk_content' ,'tsk_end_time','tsk_author']
        depth=1