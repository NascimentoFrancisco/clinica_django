from django.contrib.auth.forms import UserCreationForm
from django import forms
from clinic_app.models import User


class CreationUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','name', 'email',)


class ChangeUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','name', 'email',)


class CreationUserAdminForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','name', 'email', 'is_staff', 'is_superuser')


class UpdateUserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','name', 'email', 'is_staff', 'is_superuser')
