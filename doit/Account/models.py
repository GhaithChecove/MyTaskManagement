from django.db import models
from django.contrib.auth.models import (
    BaseUserManager , AbstractBaseUser
)
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

# class User_Account(models.Model):
#     usr_first_name = models.CharField(verbose_name=("First Name"), max_length=200)
#     usr_last_name = models.CharField(verbose_name=("Last Name"), max_length=200)
#     usr_email =models.EmailField(verbose_name=("Email"), max_length=254)
#     usr_username=models.CharField(verbose_name=("Username"), max_length=200)
#     usr_password=models.CharField(verbose_name=("Password"), max_length=200)

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None) :
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email ,username,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin   = True
        user.is_staff   = True 
        user.is_superuser = True

        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(default="I",verbose_name=("First Name"), max_length=255)
    last_name =models.CharField(default="User",verbose_name=("Last Name"), max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username =models.CharField(unique=True, max_length=50)
    password = models.CharField(verbose_name=("Password"), max_length=100)
    # date_of_birth = models.DateField(auto_now=False ,auto_now_add=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_staff



