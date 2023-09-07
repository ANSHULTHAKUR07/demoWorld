from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Manager

class StudentBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



# Create your models here.
class Student(StudentBase):
    user_name = models.CharField(max_length=25)
    class_name = models.CharField(max_length=25)
    roll_number = models.IntegerField(null=False)
    user_age = models.IntegerField(null=False)
    user_phone = models.IntegerField(null=True)

    def __str__(self):
        return(self.user_name)
    
    class Meta:
        verbose_name = 'Student'
        db_table = 'Student'


# class Employee(AbstractUser):
#     username = None
#     email= models.EmailField(("email"), unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS=[]

#     objects = UserManager()

#     user_phone = models.IntegerField(null=True)
#     user_image = models.ImageField(upload_to='images/userProfileImages', null=False)


#     def  __str__(self):
#         return self.email
    
#     class Meta:
#         verbose_name = 'Employee'
#         db_table = 'Employee'


class StudentAttendance(Student):
    month=models.DateField()
    present_days = models.IntegerField()

    def __str__(self):
        return self.user_name
    

class PersonProxy(models.Model):
    TypeChoices = (
        ('image','img'),
        ('video','video')
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    type= models.CharField(choices=TypeChoices,max_length=5,default='image')

class PersonVideoManager(Manager):

    def create(self, *args, **kwargs):
        kwargs["video"]=kwargs.get('video')
        person = PersonProxy.objects.create(**kwargs)
        return person


class PersonVideoProxy(PersonProxy):
    class Meta:
        proxy = True

    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"
    objects = PersonVideoManager()
    







