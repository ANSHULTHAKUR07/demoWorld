from django.forms import ModelForm
from .models import *


class CreateForm(ModelForm):
    model = Category
    fields = '__all__'

class CreateFormProduct(ModelForm):
    model = Product
    fields = '__all__'


