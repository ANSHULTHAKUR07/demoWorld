from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.
class ShoppingUser(AbstractUser):
    username = None
    email= models.EmailField(("email"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = UserManager()

    GenderChoices = (
        ('male', "M"),
        ('female', "F")
    )

    StateChoice =(
        ('India', 'India'),
        ('Pakistan', 'Pakistan'),
        ('Nepal', 'Nepal'),
        ('Shri Lanka', 'Shri Lanka')
    ) 
    
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(choices = GenderChoices, max_length=6)
    state = models.CharField(choices= StateChoice, max_length=50)

    def __str__(self):
        return self.email
    

class Otpgenrator(models.Model):
    userid = models.ForeignKey(ShoppingUser, null=False, on_delete=models.CASCADE)
    otp = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.otp





