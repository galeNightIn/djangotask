# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from customuser.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    passport_img = forms.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'passport_img',
            'phone_number',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password_img = self.changed_data['passport_img']
        user.phone_number = self.changed_data['phone_number']

        if commit:
            user.save()


class EditUserForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        )
