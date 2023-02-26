from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student= models.BooleanField(default=False)
    is_parent= models.BooleanField(default=False)
    is_teacher= models.BooleanField(default=False)
    is_principal= models.BooleanField(default=False)
    is_school= models.BooleanField(default=False)

class user_profile_student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,default="")
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    grade=models.CharField(max_length=50)
    school=models.CharField(max_length=200,default="")
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class user_profile_parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,default="")
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class user_profile_teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,default="")
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)
    grade=models.IntegerField(null=True)
    school=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.user.username

class user_profile_principal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,default="")
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)
    school=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.user.username

class user_profile_school(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,default="")
    school_name=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    mobile=models.CharField(max_length=15,default="")
    country=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=50,default="")
    street=models.CharField(max_length=100,default="")
    pin=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=15)
    mail=models.EmailField(max_length=50)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name