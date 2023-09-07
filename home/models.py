from django.db import models
from django.core.validators import EmailValidator

def custom_validator(self,value):
    if value == "sfsdf":
        raise ValueError
# Create your models here.
class ContactData(models.Model):
    email = models.EmailField(max_length=80,validators=[custom_validator])
    message = models.TextField()
    phone_number = models.CharField(max_length=10)
    

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'ContactUsData'
        db_table = 'ContactUsData'

        permissions = [
            ('a_random_permission', 'it is a random permission'),
        ]


class PermissionModel(models.Model):
    class Meta:
        managed = False

        default_permissions = ()
        
        permissions = [
            ('new_permission_add', 'this is just for demo'),
        ]