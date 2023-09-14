from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MyUser 



class Registration_user_form (UserCreationForm):
    # email = forms.EmailField(max_length=255, required=True)
    # date_of_birth=forms.DateField( required=True)
    class Meta:
        model = MyUser
        fields = ('first_name' , 'last_name','email' , 'password1' , 'password2')


class Task_creation(forms.Form):
    t_title = forms.CharField( label ="Task Title", max_length=255, required=False)
    t_text  = forms.Textarea()


class AccountAuthenticateForm(forms.ModelForm):
    email = forms.EmailField(max_length=255  , required=False)
    class Meta:
        model = MyUser
        fields = ("email","password",)
