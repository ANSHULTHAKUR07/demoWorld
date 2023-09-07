from typing import Any
from django import forms
from .models import ShoppingUser, Otpgenrator
import re


class UserForm(forms.ModelForm):
    cpassword = forms.CharField(max_length=50)
    class Meta:
        model = ShoppingUser
        fields = ('email', 'password','cpassword', 'first_name', 'last_name', 'phone_number', 'gender', 'state')

    def clean(self):
        data = self.cleaned_data
        print(data)

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        cpassword = data['cpassword']
        phone = data['phone_number']
        gender = data['gender']
        state = data['state']

        conditions = [
            len(email)==0 or email.isspace(),
            len(password)==0 or password.isspace(),
            len(cpassword)==0 or cpassword.isspace(),
            len(phone)==0 or phone.isspace(),
            len(first_name)== 0 or first_name.isspace(),
            len(last_name)==0 or last_name.isspace(),
            len(gender)==0 or gender.isspace(),
            len(state)==0 or state.isspace()
        ]

        if not any(conditions):
            if not first_name.isalpha():
                raise forms.ValidationError("First Name only containe alphabet")
            if not last_name.isalpha():
                raise forms.ValidationError("Last Name only containe alphabet")
            
            email_rexpression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if (re.fullmatch(email_rexpression, email)):
                pass
            else:
                raise forms.ValidationError("Invalid email")

            if len(password)<5 and len(password)>15:
                raise forms.ValidationError("Password denied: must be between 5 and 15 characters long.")
            elif re.search('[0-9]',password) is None:
                raise forms.ValidationError("Password denied: must contain a number between 0 and 9")
            elif re.search('[A-Z]',password) is None:
                raise forms.ValidationError("Password denied: must contain a capital letter.")
            elif re.search('[a-z]',password) is None:
                raise forms.ValidationError("Password denied: must contain a lowercase letter.")
            else:
                if password != cpassword:
                    raise forms.ValidationError("password did not match")
        else:
            raise forms.ValidationError('all fields are required')
        
        return data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        user.first_name = user.first_name.lower()
        if commit:
            user.save()
            print("USER)__________",user)
        
        return user