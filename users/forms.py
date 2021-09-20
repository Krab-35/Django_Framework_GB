from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User
from django import forms

import hashlib
import random

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        check_alpha = data.isalpha()
        if data[0] != data[0].upper() and check_alpha is True:
            raise forms.ValidationError('Введите имя с большой буквы')
        elif data[0] == data[0].upper() and check_alpha is False:
            raise forms.ValidationError('В имени присутствуют цифры')
        elif data[0] != data[0].upper() and check_alpha is False:
            raise forms.ValidationError('Вы ввели имя с маленькой, буквы с содержанием цифр')
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        check_alpha = data.isalpha()
        if data[0] != data[0].upper() and check_alpha is True:
            raise forms.ValidationError('Введите Фамилию с большой буквы')
        elif data[0] == data[0].upper() and check_alpha is False:
            raise forms.ValidationError('В Фамилии присутствуют цифры')
        elif data[0] != data[0].upper() and check_alpha is False:
            raise forms.ValidationError('Вы ввели Фамилию с маленькой буквы, с содержанием цифр')
        return data

    def save(self):
        user = super(UserRegistrationForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        check_alpha = data.isalpha()
        if data[0] != data[0].upper() and check_alpha is True:
            raise forms.ValidationError('Введите имя с большой буквы')
        elif data[0] == data[0].upper() and check_alpha is False:
            raise forms.ValidationError('В имени присутствуют цифры')
        elif data[0] != data[0].upper() and check_alpha is False:
            raise forms.ValidationError('Вы ввели имя с маленькой буквы, с содержанием цифр')
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        check_alpha = data.isalpha()
        if data[0] != data[0].upper() and check_alpha is True:
            raise forms.ValidationError('Введите Фамилию с большой буквы')
        elif data[0] == data[0].upper() and check_alpha is False:
            raise forms.ValidationError('В Фамилии присутствуют цифры')
        elif data[0] != data[0].upper() and check_alpha is False:
            raise forms.ValidationError('Вы ввели Фамилию с маленькой буквы, с содержанием цифр')
        return data
