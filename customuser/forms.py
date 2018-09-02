from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from customuser.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    passport_img = forms.FileField()

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        user.save()
        user.create_profile()
        user.profile_img = self.cleaned_data.get('passport_img')
        user.profile.save()

        if commit:
            user.save()

        return user


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
