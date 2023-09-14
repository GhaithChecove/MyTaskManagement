from . import models as m
from django.forms import ModelForm , Form


class NewCategory(ModelForm):
    class Meta:
        model=m.Category
        fields="__all__"

class NewTask_form(ModelForm):
    
    class Meta:
        model=m.Task
        fields=['tsk_header' , 'tsk_title'  , 'tsk_category','tsk_content' , 'tsk_end_time' ,]





