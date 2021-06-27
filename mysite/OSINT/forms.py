from django.forms import ModelForm, TextInput
from .models import User

#from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']

        widgets = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'aria-describedby': "emailHelp",

            }),
            "nickname": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'type': 'password',
            }),
            # "Password2":TextInput(attrs={
            #   'class':'form-control',
            #   'type':'password',
            # })
        }


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['Nickname','Email','Password']


# added 20.06 by Romarado




class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)

        widgets = {
            'email': TextInput(attrs={
                'class': "form-control",
                'type': "email",
                'id': "floatingInput",
                'placeholder': "name@example.com"

            }),
            "password": TextInput(attrs={
                 'class': 'form-control',
                    'type': 'password',
                    'id': "floatingPassword",
                    'placeholder': "Password"
            }),
            # "Password2":TextInput(attrs={
            #   'class':'form-control',
            #   'type':'password',
            # })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['id'] = 'floatingPassword'
        self.fields['password'].widget.attrs['type'] = 'password'

