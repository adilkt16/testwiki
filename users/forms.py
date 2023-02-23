from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","password"] 
		widgets = {
                "password" : forms.widgets.PasswordInput(attrs={
                    "class":"",
                    "placeholder":"Enter your password"
                }) ,
				"username" : forms.widgets.TextInput(attrs={
                    "class":"",
                    "placeholder":"Username(No space)"
                }) ,
        }

