from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ClienteForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']
        label = {
            'username': 'Nickname', 
            'first_name': 'Name', 
            'email': 'Correo electronico', 
            'password1': 'Contraseña', 
            'password2': 'Validacion contraseña', 
        }
           

