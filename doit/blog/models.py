from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from Account import models as am

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(verbose_name=("Category name"), max_length=200)
    cat_description  = models.CharField(verbose_name=("Category Description") ,max_length=1024)


    def __str__(self) -> str:
        return self.cat_name



class Active(models.Model):
    actv_name = models.CharField(verbose_name=("Type"), max_length=100)
    actv_description = models.TextField(verbose_name=("Description"))
    actv_start_dt = models.DateField(verbose_name=("Start Date"), auto_now=True, auto_now_add=False)
    actv_current_status = models.CharField(verbose_name=("Current Satus"), max_length=100)

    def __str__(self) -> str:
        return self.actv_name
    
    
class Suspended(models.Model):
    spnd_name = models.CharField(verbose_name=("Type"), max_length=100)
    spnd_description = models.TextField(verbose_name=("Description"))
    spnd_start_dt = models.DateField(verbose_name=("Start Date"), auto_now=True, auto_now_add=False)
    spnd_finished_dt = models.DateField(verbose_name=("Start Date"), auto_now=True, auto_now_add=False)
    spnd_issu = models.TextField(verbose_name=("Issu"))
    def __str__(self) -> str:
        return self.spnd_name


class Finished(models.Model):
    fshd_name = models.CharField(verbose_name=("Type"), max_length=100)
    fhsd_date = models.DateField(verbose_name=("Finished Date"), auto_now=True, auto_now_add=False)
    fshd_task_id= models.CharField(verbose_name=("Task id"), max_length=50)



class Task(models.Model):
    tsk_header  = models.CharField(verbose_name=("Header"), max_length=255)
    tsk_title= models.CharField(verbose_name=("Title"), max_length=255)
    tsk_author  = models.ForeignKey(am.MyUser, verbose_name=("Author"), on_delete=models.CASCADE)
    tsk_category = models.ForeignKey( Category ,verbose_name="Category" , on_delete=models.CASCADE )
    tsk_content = models.TextField(verbose_name=("Post"))
    tsk_publish_dt=models.DateField(verbose_name=("Published Date"), auto_now=True, auto_now_add=False)
    tsk_modified_dt =models.DateField(verbose_name=("Modified Date"), auto_now=True, auto_now_add=False)
    tsk_end_time = models.DateField(verbose_name=("End Date"), auto_now=False, auto_now_add=False )
    tsk_is_finished = models.BooleanField(verbose_name=("Is Finished") , default=False)
    


    def __str__(self) -> str:
        return self.tsk_title

class Stuff(models.Model):
    stf_name = models.ForeignKey(Task, verbose_name=("Task Title"), on_delete=models.CASCADE)
    stf_id = models.CharField(verbose_name=("Stuff ID"), max_length=200)


    def __str__(self) -> str:
        return self.stf_name