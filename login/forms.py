from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.forms import EmailField


class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')

        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {"username": UsernameField}


#  новая часть, чтобы попробовать реализовать текст при использовании для входа несуществующего логина
# class CustomUserErrorText(UsernameField):
#     username = UsernameField()
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if not User.objects.filter(username=username).exist():
#             raise ValidationError('User name does not exist! \nTry again;)')
#
#         return username
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         field_classes = {"username": UsernameField}
